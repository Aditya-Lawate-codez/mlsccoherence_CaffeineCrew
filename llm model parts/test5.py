from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model using TensorFlow weights
tokenizer = AutoTokenizer.from_pretrained("Kaludi/Customer-Support-Assistant-V2")
model = AutoModelForSeq2SeqLM.from_pretrained("Kaludi/Customer-Support-Assistant-V2", from_tf=True)

def generate_response(user_input):
    # Tokenize the user input
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids

    # Generate a response from the model
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    
    # Decode and return the response
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

# Example usage
user_input = "I am facing issues with my laptop."
response = generate_response(user_input)
print("CVA:", response)
