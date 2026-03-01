from transformers import LlamaForCausalLM, LlamaTokenizer
from peft import PeftModel
import torch


base_model_path = r"E:/Graduation Project/Alpaca-LoRA-MedAssist/models/alpaca-lora-7b/base_model"  
lora_adapter_path = r"E:/Graduation Project/Alpaca-LoRA-MedAssist/models/alpaca-lora-7b/adapter_model.safetensors"

tokenizer = LlamaTokenizer.from_pretrained(base_model_path, local_files_only=True)


base_model = LlamaForCausalLM.from_pretrained(
    base_model_path,
    device_map="auto",        
    torch_dtype=torch.float16,
    local_files_only=True
)


base_model = PeftModel.from_pretrained(
    base_model,
    lora_adapter_path,
    device_map="auto",
    torch_dtype=torch.float16,
    local_files_only=True
)
print(" LoRA adapter loaded successfully!")


prompt = "Explain mild headache symptoms."
inputs = tokenizer(prompt, return_tensors="pt").to(base_model.device)

output_ids = base_model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.7
)

output = tokenizer.decode(output_ids[0], skip_special_tokens=True)

print("\n>>> Prompt:")
print(prompt)
print("\n>>> Generated Output:")
print(output)