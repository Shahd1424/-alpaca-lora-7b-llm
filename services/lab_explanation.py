from core.llm_client import generate_response
from core.prompts import lab_prompt

def explain_labs(labs: dict):
    prompt = lab_prompt(labs)
    context = {"prefix": "Avoid diagnosis or treatment."}
    return generate_response(prompt, context)