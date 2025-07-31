import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit

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
    # elif "52 bar" in c:
    #     webbrowser.open("https://www.youtube.com/watch?v=4DfVxVeqk2o&list=RD4DfVxVeqk2o&start_radio=1&pp=ygUHNTIgYmFyc6AHAQ%3D%3D")
    # elif "play tere liye" in c:
    #     speak("Opening Google")
    #     webbrowser.open("https://www.youtube.com/watch?v=3W7I6beLnkk&list=RD3W7I6beLnkk&start_radio=1&pp=ygUKdGVyZSBsaXllZaAHAQ%3D%3D")
    # elif "play ishq " in c:
    #     speak("Opening Google")
    #     webbrowser.open("https://youtu.be/hHuG7FIKgtc?list=RDhHuG7FIKgtc")
    # elif "play paro" in c:
    #     speak("Opening Google")
    #     webbrowser.open("https://www.youtube.com/watch?v=Es4NrOnoNb4&list=RDEs4NrOnoNb4&start_radio=1&pp=ygUOcGFybyB1bnBsdWdnZWSgBwE%3D")
    elif "play" in c:
        song = c.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    else:
        print("NOTHING MATCH")
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    recognizer = sr.Recognizer() 

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for ' hey Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print(f"You said: {word}")


                with sr.Microphone() as source:
                        print("Jarvis Active, listening for command...")
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        audio = recognizer.listen(source, timeout=9, phrase_time_limit=9)
                        command = recognizer.recognize_google(audio)
                        print(f"Command: {command}")

                        processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
