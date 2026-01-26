import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for, flash
import random
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Define expected columns
EXPECTED_COLUMNS = [
    'Subject Code', 'Description', 'Exam Period', 'Learning Outcome', 
    'Topic', 'QUESTION', 'Type of Question', 'Taxonomy', 
    'Choice A', 'Choice B', 'Choice C', 'Choice D', 'Answer', 
    'Correct answer in Words'
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'excel_file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['excel_file']
    
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    
    if file and file.filename.lower().endswith(('.xlsx', '.xls')):
        # Save the file temporarily
        filepath = os.path.join('uploads', file.filename)
        os.makedirs('uploads', exist_ok=True)
        file.save(filepath)
        
        try:
            # Read the Excel file
            df = pd.read_excel(filepath)
            
            # Check if all required columns exist
            missing_cols = [col for col in EXPECTED_COLUMNS if col not in df.columns]
            if missing_cols:
                flash(f'Missing required columns: {", ".join(missing_cols)}')
                return redirect(url_for('index'))
            
            # Extract unique topics
            unique_topics = df['Topic'].dropna().unique().tolist()
            
            # Store the dataframe in session or temporary storage
            # For simplicity, we'll save it as a JSON file temporarily
            data_dict = df.to_dict('records')
            data_json = json.dumps(data_dict)
            
            return render_template('select_topics.html', 
                                 topics=unique_topics, 
                                 data=data_json,
                                 total_questions=len(df))
        except Exception as e:
            flash(f'Error reading Excel file: {str(e)}')
            return redirect(url_for('index'))
    else:
        flash('Invalid file format. Please upload an Excel file (.xlsx or .xls)')
        return redirect(url_for('index'))

@app.route('/generate', methods=['POST'])
def generate_quiz():
    try:
        # Get form data
        selected_topics = request.form.getlist('topics')
        timer_duration = int(request.form.get('timer_duration', 60))  # Default 60 seconds
        num_questions_str = request.form.get('num_questions', '').strip()

        if not selected_topics:
            flash('Please select at least one topic')
            return redirect(url_for('index'))

        # Get the data from form
        data_json = request.form.get('data')
        if not data_json:
            flash('No data available')
            return redirect(url_for('index'))

        # Convert JSON back to DataFrame
        data_list = json.loads(data_json)
        df = pd.DataFrame(data_list)

        # Filter questions by selected topics
        filtered_df = df[df['Topic'].isin(selected_topics)]

        if filtered_df.empty:
            flash('No questions found for the selected topics')
            return redirect(url_for('index'))

        # Limit the number of questions if specified
        if num_questions_str:
            try:
                num_questions = int(num_questions_str)
                if num_questions < 1:
                    flash('Number of questions must be at least 1')
                    return redirect(url_for('index'))

                if len(filtered_df) > num_questions:
                    # Randomly select the specified number of questions
                    filtered_df = filtered_df.sample(n=num_questions, random_state=42)
            except ValueError:
                flash('Invalid number of questions specified')
                return redirect(url_for('index'))

        # Generate quiz slides
        quiz_data = {
            'questions': [],
            'answers': []
        }

        for _, row in filtered_df.iterrows():
            question_data = {
                'question': row['QUESTION'],
                'choices': [
                    {'label': 'A', 'text': row['Choice A']},
                    {'label': 'B', 'text': row['Choice B']},
                    {'label': 'C', 'text': row['Choice C']},
                    {'label': 'D', 'text': row['Choice D']}
                ],
                'answer': row['Answer'],
                'correct_answer_text': row['Correct answer in Words']
            }
            quiz_data['questions'].append(question_data)
            quiz_data['answers'].append({
                'question': row['QUESTION'],
                'answer': row['Answer'],
                'correct_answer_text': row['Correct answer in Words']
            })

        # Shuffle questions
        random.shuffle(quiz_data['questions'])

        # Render the quiz template
        return render_template('quiz.html',
                             questions=quiz_data['questions'],
                             answers=quiz_data['answers'],
                             timer_duration=timer_duration)
    except Exception as e:
        flash(f'Error generating quiz: {str(e)}')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)