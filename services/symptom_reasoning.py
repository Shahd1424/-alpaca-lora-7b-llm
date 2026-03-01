from core.llm_client import generate_response
from core.prompts import symptom_prompt

def analyze_symptoms(symptoms: dict):
    prompt = symptom_prompt(symptoms)
    context = {"prefix": "You must avoid diagnosis."}
    return generate_response(prompt, context)