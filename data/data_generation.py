# 1. Load the MIMIC dataset using a suitable library like pandas:

import pandas as pd

# Load tables from the MIMIC dataset
admissions_df = pd.read_csv('ADMISSIONS.csv')
diagnoses_df = pd.read_csv('DIAGNOSES_ICD.csv')
patients_df = pd.read_csv('PATIENTS.csv')
noteevents_df = pd.read_csv('NOTEEVENTS.csv')
prescriptions_df = pd.read_csv('PRESCRIPTIONS.csv')

'''
# 2. Preprocess the dataset:

Clean and preprocess the text data.
Convert dates and other data types into appropriate formats.
Merge relevant tables using patient ID and admission ID.

'''
# 3. Define a function to create the context based on the patient's data:

def create_context(patient_data):
    context = f"{patient_data['age']} year-old {patient_data['gender']} with a history of {patient_data['medical_history']}. The patient was admitted to the hospital due to {patient_data['symptoms']}. {patient_data['diagnostics']} The primary diagnosis was {patient_data['diagnosis']}. The patient was treated with {patient_data['treatment']}."
    return context

#4. Define a function to generate questions based on the patient's data. For simplicity, let's generate a question related to the primary diagnosis:

def generate_question(patient_id):
    return f"What is the primary diagnosis of patient {patient_id}?"


#5. Iterate through the dataset, creating context-question pairs for each patient:
context_question_pairs = []

for index, row in dataset.iterrows():
    patient_data = extract_patient_data(row)  # Define a function to extract relevant patient data
    context = create_context(patient_data)
    question = generate_question(row['patient_id'])
    context_question_pairs.append((context, question))
