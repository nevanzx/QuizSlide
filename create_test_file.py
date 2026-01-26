import pandas as pd

# Sample data
data = {
    'Subject Code': ['CS101', 'CS101', 'CS101', 'CS101', 'CS101', 'CS101', 'CS101'],
    'Description': ['Introduction to Programming', 'Introduction to Programming', 'Introduction to Programming', 
                   'Introduction to Programming', 'Introduction to Programming', 
                   'Introduction to Programming', 'Introduction to Programming'],
    'Exam Period': ['Midterm', 'Midterm', 'Midterm', 'Finals', 'Finals', 'Finals', 'Finals'],
    'Learning Outcome': ['LO1', 'LO1', 'LO1', 'LO2', 'LO2', 'LO2', 'LO2'],
    'Topic': ['Basic Syntax', 'Basic Syntax', 'Basic Syntax', 'Loops', 'Loops', 'Functions', 'Functions'],
    'QUESTION': [
        'What is a variable?',
        'Which symbol is used for assignment in most languages?',
        'What does the term \'syntax\' refer to?',
        'Which loop executes at least once?',
        'What is the purpose of a loop?',
        'What is a function?',
        'Which keyword is used to define a function in Python?'
    ],
    'Type of Question': ['Multiple Choice', 'Multiple Choice', 'Multiple Choice', 
                         'Multiple Choice', 'Multiple Choice', 'Multiple Choice', 'Multiple Choice'],
    'Taxonomy': ['Understanding', 'Application', 'Understanding', 'Knowledge', 'Understanding', 'Understanding', 'Knowledge'],
    'Choice A': ['Storage unit', '=', 'Grammar rules of a programming language', 'while', 'To repeat code', 'A reusable block of code', 'def'],
    'Choice B': ['A mathematical operator', '+', 'Computer memory', 'for', 'To store data', 'A variable', 'func'],
    'Choice C': ['A loop structure', '-', 'The CPU', 'do-while', 'To define functions', 'A loop', 'function'],
    'Choice D': ['A conditional statement', '*', 'The hard drive', 'foreach', 'To create variables', 'A conditional statement', 'define'],
    'Answer': ['A', 'A', 'A', 'C', 'A', 'A', 'A'],
    'Correct answer in Words': ['Storage unit', 'Equals sign', 'Grammar rules of a programming language', 
                                'do-while', 'To repeat code', 'A reusable block of code', 'def']
}

df = pd.DataFrame(data)
df.to_excel('test_sample.xlsx', index=False)
print("Excel file 'test_sample.xlsx' created successfully!")