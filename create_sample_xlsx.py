import pandas as pd

# Read the CSV file
df = pd.read_csv('sample_questions.csv')

# Save as Excel file
df.to_excel('sample_questions.xlsx', index=False)

print("Sample Excel file created: sample_questions.xlsx")