import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand ")


def speechtxt(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',130)
    engine.say(x)
    engine.runAndWait()


if __name__ == '__main__':
    

    if "hey peter" in sptext().lower():
        speechtxt("welcome sir")
        while True:
            
            data1 = sptext().lower()

            if "your name" in data1:
                name = "my name is peter"
                speechtxt(name)

            elif "old are you" in data1:
                age = "i am two years old"
                speechtxt(age)

            elif 'time' in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtxt(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtxt(joke_1)
            elif 'play song' in data1:
                add = "C:/Web-Workshop/challenge3"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[2]))

            elif "exit" in data1:
                speechtxt("thank you")
                break
            else:
                speechtxt("result not found")

            time.sleep(10)



    else:
        print("Thanks")
