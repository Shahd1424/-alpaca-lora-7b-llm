from core.llm_client import generate_response
from core.prompts import next_steps_prompt

def get_next_steps(context: dict):
    prompt = next_steps_prompt(context)
    ctx = {"prefix": "Provide only safe lifestyle & monitoring advice."}
    return generate_response(prompt, ctx)