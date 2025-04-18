import random
import pyttsx3
import speech_recognition as sr
import pickle

# List of words for the spelling bee practice
word_list = ["ship", "tank"]

# Initialize TTS engine
engine = pyttsx3.init()

# Function to speak a word
def speak_word(word):
    engine.say(word)
    engine.runAndWait()

# Function to listen and recognize the user's spelling
def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please spell the word:")
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            return None

# Main practice loop
def spell_bee_practice():
    while True:
        word = random.choice(word_list)
        speak_word(word)
        #print(f"Spell the word: {word}")  # For testing purposes, remove in real scenario
        user_spelling = listen_and_recognize()
        
        if user_spelling is None:
            print("Sorry, I didn't catch that. Please try again.")
            continue

        # Print the recognized result
        print(f"You spelled: {user_spelling}")
        
        # Normalize the words by removing spaces
        normalized_user_spelling = user_spelling.replace(" ", "").lower()
        normalized_word = word.replace(" ", "").lower()

        if normalized_user_spelling == normalized_word:
            speak_word("Correct!")
            print("Correct!")
        else:
            speak_word("Sorry, Its incorrect!")
            print(f"Incorrect. The correct spelling is {word}.")

        # Option to continue or quit
        cont = input("Do you want to continue? (Y/N): ")
        if cont.lower() != 'y':
            break

# Run the spelling bee practice
spell_bee_practice()
