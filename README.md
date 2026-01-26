# Quiz HTML Slide Generator

This application generates timed HTML slides from Excel files containing quiz questions. It allows users to select specific topics and set timers for each question.

## Features

- Upload Excel files with quiz questions
- Select specific topics to include in the quiz
- Set custom timer duration for each question
- Generate HTML slides with automatic progression
- View all correct answers at the end
- Keyboard navigation (arrow keys)

## Excel File Format

Your Excel file must contain the following columns:

- Subject Code
- Description
- Exam Period
- Learning Outcome
- Topic
- QUESTION
- Type of Question
- Taxonomy
- Choice A
- Choice B
- Choice C
- Choice D
- Answer
- Correct answer in Words

## Installation

1. Clone or download this repository
2. Install required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

### In VSCode:

1. Open the project folder in VSCode
2. Open a terminal in VSCode
3. Run the application:

```bash
python app.py
```

4. Open your browser and navigate to `http://127.0.0.1:5000`

### In Termux (Android):

1. Install Python if not already installed:

```bash
pkg install python
```

2. Install pip packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

4. Access the application in your browser at `http://127.0.0.1:5000`

## Usage

1. Upload your Excel file using the main page
2. Select the topics you want to include in the quiz
3. Set the time limit for each question
4. Click "Generate Quiz Slides"
5. Navigate through the slides using the buttons or arrow keys
6. The final slide shows all correct answers

## Project Structure

```
Quiz HTML Maker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── sample_questions.xlsx  # Sample Excel file for testing
├── uploads/              # Temporary storage for uploaded files
└── templates/            # HTML templates
    ├── index.html        # Home page
    ├── select_topics.html # Topic selection page
    └── quiz.html         # Quiz slides page
```

## Dependencies

- pandas: For reading Excel files
- openpyxl: For Excel file support
- flask: For web interface