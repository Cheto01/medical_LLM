# 0

# 1. returns the available question templates and their corresponding answer keys based on the patient's data

def available_question_templates(patient_data):
    all_templates = [
        ("What is the primary diagnosis of patient {patient_id}?", "diagnosis"),
        # ... add all other question templates and answer keys ...
    ]

    available_templates = []
    for question_template, answer_key in all_templates:
        if patient_data.get(answer_key) is not None:
            available_templates.append((question_template, answer_key))

    return available_templates

# 2. Update the generate_question function to use the available question templates based on the patient's data:

import random

def generate_question(patient_data, seed=None):
    available_templates = available_question_templates(patient_data)
    if seed is not None:
        random.seed(seed)  # Set the seed for deterministic randomness
    question_template, answer_key = random.choice(available_templates)
    question = question_template.format(**patient_data)
    answer = patient_data[answer_key]
    return question, answer

# 3. Define a function generate_n_question_answers that generates n pairs of question-answers for each patient:

def generate_n_question_answers(patient_data, n, seed=None):
    questions_answers = []
    for i in range(n):
        question, answer = generate_question(patient_data, seed=seed)
        questions_answers.append((question, answer))
    return questions_answers

# 4. Iterate through the dataset, creating context-question-answer triples for each patient:
context_question_answer_triples = []

for index, row in dataset.iterrows():
    patient_data = extract_patient_data(row)  # Define a function to extract relevant patient data
    context = create_context(patient_data)
    n_question_answers = generate_n_question_answers(patient_data, n=3, seed=index)  # Change n to desired number of pairs
    for question, answer in n_question_answers:
        context_question_answer_triples.append((context, question, answer))

# 5. Read the data and preprocess

import pandas as pd

# Load the NOTEEVENTS table from the MIMIC dataset
noteevents_df = pd.read_csv('NOTEEVENTS.csv')

# 6. Create a medical abbreviation dictionary and their meaning

medical_abbreviations = {
    'abd': 'abdomen',
    'abx': 'antibiotics',
    'ac': 'before meals',
    'adl': 'activities of daily living',
    'af': 'atrial fibrillation',
    'aki': 'acute kidney injury',
    'bid': 'twice daily',
    'bp': 'blood pressure',
    'bpm': 'beats per minute',
    'c/o': 'complains of',
    'cabg': 'coronary artery bypass graft',
    'cad': 'coronary artery disease',
    'chf': 'congestive heart failure',
    'ckd': 'chronic kidney disease',
    'copd': 'chronic obstructive pulmonary disease',
    'cpr': 'cardiopulmonary resuscitation',
    'ct': 'computed tomography',
    'cv': 'cardiovascular',
    'cxr': 'chest x-ray',
    'dm': 'diabetes mellitus',
    'dvt': 'deep vein thrombosis',
    'dx': 'diagnosis',
    'ed': 'emergency department',
    'ekg': 'electrocardiogram',
    'gi': 'gastrointestinal',
    'h/o': 'history of',
    'hr': 'heart rate',
    'htn': 'hypertension',
    'icu': 'intensive care unit',
    'iv': 'intravenous',
    'mi': 'myocardial infarction',
    'mri': 'magnetic resonance imaging',
    'na': 'sodium',
    'ngt': 'nasogastric tube',
    'nihss': 'national institutes of health stroke scale',
    'np': 'nurse practitioner',
    'nsr': 'normal sinus rhythm',
    'n/v': 'nausea and vomiting',
    'o2': 'oxygen',
    'od': 'once daily',
    'otc': 'over the counter',
    'pe': 'pulmonary embolism',
    'po': 'by mouth',
    'prn': 'as needed',
    'pt': 'patient',
    'qid': 'four times daily',
    'r/o': 'rule out',
    'ra': 'room air',
    'rr': 'respiratory rate',
    'rt': 'respiratory therapy',
    'rx': 'prescription',
    'sob': 'shortness of breath',
    'stat': 'immediately',
    'tid': 'three times daily',
    'uti': 'urinary tract infection',
    'vs': 'vital signs',
    'wbc': 'white blood cell',
    'w/o': 'without',
}

def replace_abbreviations(text, abbreviations):
    words = text.split()
    replaced_words = [abbreviations.get(word, word) for word in words]
    replaced_text = ' '.join(replaced_words)
    return replaced_text


# 7. preprocess and clean the data

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    # Remove any personally identifiable information (PII)
    text = re.sub(r'\[\*\*(.*?)\*\*\]', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters, numbers, and extra whitespace
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

    # Replace medical abbreviations with their meanings
    preprocessed_text = replace_abbreviations(preprocessed_text, medical_abbreviations)


    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join the tokens back into a single string
    preprocessed_text = ' '.join(tokens)

    return preprocessed_text

# 8. Apply the preprocess function
noteevents_df['preprocessed_text'] = noteevents_df['TEXT'].apply(preprocess_text)

