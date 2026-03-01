import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
from core.guardrails import validate_output
from config import LLM_MODEL_PATH, MAX_TOKENS, TEMPERATURE

print(" Loading local LLM model...")

tokenizer = LlamaTokenizer.from_pretrained(f"{LLM_MODEL_PATH}/base_model")
model = LlamaForCausalLM.from_pretrained(
    f"{LLM_MODEL_PATH}/base_model",
    torch_dtype=torch.float16,
    device_map="auto"
)

model.load_adapter(f"{LLM_MODEL_PATH}/adapter_model.bin", adapter_name="alpaca-lora")

print(" Model loaded.")


def generate_response(prompt: str, context: dict) -> str:
    full_prompt = context.get("prefix", "") + "\n" + prompt

    inputs = tokenizer(full_prompt, return_tensors="pt").to(model.device)

    output_ids = model.generate(
        **inputs,
        max_new_tokens=MAX_TOKENS,
        temperature=TEMPERATURE
    )

    output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return validate_output(output)