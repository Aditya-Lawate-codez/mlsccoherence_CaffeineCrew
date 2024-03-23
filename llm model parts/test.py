import speech_recognition as sr
import pyttsx3
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Load pretrained GPT-2 model and tokenizer
# tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# model = GPT2LMHeadModel.from_pretrained("gpt2")

tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
model = GPT2LMHeadModel.from_pretrained("EleutherAI/gpt-neo-1.3B")

def speech_to_text():
    with sr.Microphone() as source:
        print("Speak:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

def generate_response(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def main():
    text_to_speech("Hello! I'm your Customer Virtual Assistant. How can I assist you today?")
    while True:
        user_input = speech_to_text()
        if user_input.lower() == "exit":
            text_to_speech("Goodbye!")
            break
        
        response = generate_response(user_input)
        print("Bot:", response)
        text_to_speech(response)

if __name__ == "__main__":
    main()
