import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    "It takes microphone input from the user and returns string output"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again, please ...")
        return "None"

wishMe()
query = takeCommand()
speak(query)
