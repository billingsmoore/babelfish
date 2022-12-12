#libraries
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# get user speech and turn into text

recognizer = spr.Recognizer()

mic = spr.Microphone()

with mic as source:
    print("Initializing...")
    recognizer.adjust_for_ambient_noise(source, duration=0.2)
    print("Begin speaking")
    audio = recognizer.listen(source)
    
untranslated_text = recognizer.recognize_google(audio)

# Translate Text

translator = Translator()

translated_text = translator.translate(untranslated_text, dest='es').text

# speak translated text
speak = gTTS(text=translated_text, lang='es', slow=False)

speak.save('output.mp3')

os.system('mpg123 output.mp3')