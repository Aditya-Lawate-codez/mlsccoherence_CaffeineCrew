import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import googletrans as translator
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Define language codes
languages = {
    "english": "en",
    "hindi": "hi"
}

# Initialize recognizer, translator, and tokenizer
recognizer = sr.Recognizer()
detected_language = ""
tokenizer = AutoTokenizer.from_pretrained("Kaludi/Customer-Support-Assistant-V2")
model = AutoModelForSeq2SeqLM.from_pretrained("Kaludi/Customer-Support-Assistant-V2", from_tf=True)

def generate_response(user_input):
    """Generates a response using the transformer model"""
    input_ids = tokenizer(user_input, return_tensors="pt").input_ids
    output = model.generate(input_ids, max_length=50, num_return_sequences=1)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response

def speak(text, lang_code):
    """Converts text to speech and plays the audio"""
    tts = gTTS(text=text, lang=lang_code)
    tts.save("output.mp3")
    playsound("output.mp3")

def detect_language():
    """Listens for user input and detects language"""
    global detected_language
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        detected_language = translator.Translator().detect(text).lang
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    return text

def translate_and_speak(text, target_lang):
    """Translates text to the target language and speaks it"""
    translation = translator.Translator().translate(text, dest=target_lang)
    speak(translation.text, translation.src)

def main():
    """Main loop for interaction"""
    user_input = detect_language()
    
    # Determine language based on detection or default to English
    language = languages.get(detected_language, languages["english"])
    
    speak(f"Hello, how can I help you today? (English or हिंदी)", language)

    while True:
        user_input = detect_language()
        if user_input.lower() == "exit":
            speak("Thank you for using our virtual assistant. Goodbye!", language)
            break
        else:
            # Get response from transformer model
            response = generate_response(user_input)
            speak(response, language)

if __name__ == "__main__":
    main()
