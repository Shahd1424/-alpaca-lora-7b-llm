import os

# LLM SETTINGS

LLM_MODEL_PATH = r"E:\Graduation Project\Alpaca-LoRA-MedAssist\models\alpaca-lora-7b"
TEMPERATURE = 0.3
MAX_TOKENS = 350


DISALLOWED_KEYWORDS = [
    "diagnose", "diagnosis", "prescribe", "treatment",
    "emergency instruction", "drug", "medication"
]

MEDICAL_DISCLAIMER = (
    " This is not medical advice. Please consult a licensed physician for diagnosis or treatment."
)