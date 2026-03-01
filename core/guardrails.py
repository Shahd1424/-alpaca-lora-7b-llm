from config import DISALLOWED_KEYWORDS, MEDICAL_DISCLAIMER

def violates_safety(text: str) -> bool:
    text_lower = text.lower()
    for k in DISALLOWED_KEYWORDS:
        if k in text_lower:
            return True
    return False

def sanitize_output(text: str) -> str:
    for k in DISALLOWED_KEYWORDS:
        text = text.replace(k, "[unsafe-content-blocked]")
    return text

def validate_output(output: str) -> str:
    if violates_safety(output):
        output = sanitize_output(output)
    return output + "\n\n" + MEDICAL_DISCLAIMER