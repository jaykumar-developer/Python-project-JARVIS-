import speech_recognition as sr
import webbrowser
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        speak("Opening Google")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        speak("Opening Google")
        webbrowser.open("https://linkedin.com")
    elif "open music" in c:
        speak("Opening Google")
        webbrowser.open("https://music.youtube.com/")
    elif "play one thousand miles" in c:
        speak("Opening Google")
        webbrowser.open("https://youtu.be/OeLC1sc6ckg?si=dT2GgYIpGl1MDWjj")
    elif "play tere liye" in c:
        speak("Opening Google")
        webbrowser.open("https://www.youtube.com/watch?v=3W7I6beLnkk&list=RD3W7I6beLnkk&start_radio=1&pp=ygUKdGVyZSBsaXllZaAHAQ%3D%3D")
    elif "play millionaire " in c:
        speak("Opening Google")
        webbrowser.open("https://youtu.be/XO8wew38VM8?si=_R1QBtuZH7wUi2nY")
    elif "play paro" in c:
        speak("Opening Google")
        webbrowser.open("https://www.youtube.com/watch?v=Es4NrOnoNb4&list=RDEs4NrOnoNb4&start_radio=1&pp=ygUOcGFybyB1bnBsdWdnZWSgBwE%3D")
    else:
        print("NOTHING MATCH")
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    recognizer = sr.Recognizer() 

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print(f"You said: {word}")

                if "jarvis" in word.lower():
                    speak("Ya")

                    with sr.Microphone() as source:
                        print("Jarvis Active, listening for command...")
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")

                        processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
