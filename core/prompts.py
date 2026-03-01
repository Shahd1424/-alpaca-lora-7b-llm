def symptom_prompt(symptoms):
    return f"""
You are a medical assistant AI. Explain the symptoms safely.

Symptoms: {symptoms}

Explain:
- Possible interpretations (not diagnoses)
- What these symptoms *could be related to* in general
- When a doctor visit is advised
Avoid:
- Diagnosis
- Emergency instructions
- Treatment
"""

def lab_prompt(labs):
    return f"""
You are a medical lab explainer AI.

Lab values: {labs}

Explain in simple language:
- What each value means
- If it is high/low in general terms
- Possible harmless reasons
Avoid:
- Diagnosis
- Medical treatment
"""

def next_steps_prompt(context):
    return f"""
Provide safe next steps based on this context:

Context: {context}

Include:
- Lifestyle advice
- Monitoring advice
- When to see a doctor

Avoid:
- Treatment
- Drug prescriptions
- Emergency instructions
"""
