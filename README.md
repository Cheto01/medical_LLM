# medical_llm
Large Language Model for Biomedical


# 1. data_generation.py 

this is a simplified example, and you might need to customize the `extract_patient_data()` function based on the structure of your dataset and the type of questions you want to generate. You can expand the `generate_question()` function to create more diverse questions based on different aspects of the patient's data, such as symptoms, treatments, or lab results.

**For simplicity, let's generate a question related to the primary diagnosis:**


# 2. data_generation2.py

* To diversify questions and context, you can create a list of question templates and select different aspects of the patient's data to generate questions.

This approach will generate a diverse set of questions related to different aspects of the patient's data, such as symptoms, treatments, lab results, and medical history. You can add more question templates to the question_templates list or customize the existing templates to create even more diverse questions.


* To pair these questions with relevant contexts and extract their corresponding answers (ground truths), you can modify the `generate_question` function to return both the question and the answer. 

This approach will generate diverse question-context pairs with corresponding answers (ground truths) based on different aspects of the patient's data. You can further customize the `generate_question` function and add more question templates to create even more diverse questions and answers.

* To ensure that the answer corresponds to the randomly generated question, you need to carefully construct the question templates and map them to the correct keys in the patient data dictionary. In the example provided earlier, the question_templates list contains tuples with the question template and the corresponding key in the patient data dictionary.

When constructing the `patient_data` dictionary in the `extract_patient_data()` function, make sure to include all the relevant keys that you want to use in your question templates.