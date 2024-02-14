import time
import datetime
import pyttsx3
import speech_recognition as sr

master="vishnu"
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:      
        print("listening")
        r.pause_threshold=0.5
        audio=r.listen(source)

    try:
        query=r.recognize_google(audio,language="en-in")
        print(query)

    except Exception as e:
        print(" can you repeat it again")
        query=None

    return query

def listennnn():
        query=takecommand()
        query=query.lower()
        print(query)
        listennnn()

listennnn()
