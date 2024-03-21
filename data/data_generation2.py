#. 0



#. 1. Define a function to select a random question template and generate a question based on the patient's data:

import random

def generate_question(patient_data):
    question_templates = [
        "What is the primary diagnosis of patient {patient_id}?",
        "What symptoms led to the admission of patient {patient_id}?",
        "What treatments were administered to patient {patient_id}?",
        "What is the age and gender of patient {patient_id}?",
        "What were the lab results for patient {patient_id}?",
        "What medications were prescribed to patient {patient_id} during their hospital stay?",
        "What is the medical history of patient {patient_id}?",
        "What imaging or diagnostic tests were performed on patient {patient_id}?",
        "What was the length of stay for patient {patient_id}?",
        "What were the discharge instructions for patient {patient_id}?",
    ]

    question_template = random.choice(question_templates)
    question = question_template.format(**patient_data)
    return question




#. 2. Iterate through the dataset, creating context-question pairs for each patient:
context_question_pairs = []

for index, row in dataset.iterrows():
    patient_data = extract_patient_data(row)  # Define a function to extract relevant patient data
    context = create_context(patient_data)
    question = generate_question(patient_data)
    context_question_pairs.append((context, question))





#****************************************************




# Modified generate_question function to return both the question and the answer:
def generate_question(patient_data):
    question_templates = [
        ("What is the primary diagnosis of patient {patient_id}?", "diagnosis"),
        ("What symptoms led to the admission of patient {patient_id}?", "symptoms"),
        ("What treatments were administered to patient {patient_id}?", "treatment"),
        ("What is the age and gender of patient {patient_id}?", "age_gender"),
        ("What were the lab results for patient {patient_id}?", "lab_results"),
        ("What medications were prescribed to patient {patient_id} during their hospital stay?", "medications"),
        ("What is the medical history of patient {patient_id}?", "medical_history"),
        ("What imaging or diagnostic tests were performed on patient {patient_id}?", "diagnostics"),
        ("What was the length of stay for patient {patient_id}?", "length_of_stay"),
        ("What were the discharge instructions for patient {patient_id}?", "discharge_instructions"),
    ]

    question_template, answer_key = random.choice(question_templates)
    question = question_template.format(**patient_data)
    answer = patient_data[answer_key]
    return question, answer



context_question_answer_triples = []

for index, row in dataset.iterrows():
    patient_data = extract_patient_data(row)  # Define a function to extract relevant patient data
    context = create_context(patient_data)
    question, answer = generate_question(patient_data)
    context_question_answer_triples.append((context, question, answer))


def extract_patient_data(row):
    patient_data = {
        'patient_id': row['patient_id'],
        'age': row['age'],
        'gender': row['gender'],
        'medical_history': row['medical_history'],
        'symptoms': row['symptoms'],
        'diagnostics': row['diagnostics'],
        'diagnosis': row['diagnosis'],
        'treatment': row['treatment'],
        'lab_results': row['lab_results'],
        'medications': row['medications'],
        'length_of_stay': row['length_of_stay'],
        'discharge_instructions': row['discharge_instructions'],
    }
    return patient_data

# When defining the question templates, make sure that the second element in each tuple corresponds to the key in the patient_data dictionary. For example:

question_templates = [
    ("What is the primary diagnosis of patient {patient_id}?", "diagnosis"),
    ("What symptoms led to the admission of patient {patient_id}?", "symptoms"),
    # ...
]

# In the generate_question function, select a random question template and its corresponding answer key, then use the patient data dictionary to retrieve the correct answer:
question_template, answer_key = random.choice(question_templates)
question = question_template.format(**patient_data)
answer = patient_data[answer_key]
