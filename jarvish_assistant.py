import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit

# Initialize text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def processCommand(command):
    command = command.lower()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "open music" in command:
        speak("Opening YouTube Music")
        webbrowser.open("https://music.youtube.com")

    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
        else:
            speak("Please tell me which song to play.")

    else:
        speak("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    recognizer = sr.Recognizer()

    while True:
        try:
            # Listen for wake word
            with sr.Microphone() as source:
                print("Listening for 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)

                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=3
                )

            wake_word = recognizer.recognize_google(audio).lower()
            print("You said:", wake_word)

            if "jarvis" in wake_word:
                speak("Yes, I am listening.")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active, listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)

                    audio = recognizer.listen(
                        source,
                        timeout=10,
                        phrase_time_limit=10
                    )

                command = recognizer.recognize_google(audio)
                print("Command:", command)

                processCommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out.")

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError as e:
            print(f"Speech Recognition service error: {e}")

        except Exception as e:
            print(f"Error: {e}")