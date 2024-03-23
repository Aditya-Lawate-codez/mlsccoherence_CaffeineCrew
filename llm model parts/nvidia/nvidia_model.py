from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pretrained model and tokenizer
model_name = "NVIDIA/megatron-gpt2-large"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Tokenize input text
input_text = "Hello, how are you?"
input_tokens = tokenizer(input_text, return_tensors="pt")

# Generate output
output = model.generate(input_tokens.input_ids, max_length=50, num_return_sequences=1)
output_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:", output_text)
