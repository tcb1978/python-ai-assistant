import speech_recognition as sr

class SpeechProcessing:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            audio = None
            try:
                audio = self.recognizer.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                return ""
            except Exception as e:
                print(f"An error occurred while listening: {e}")
                return ""
            if audio is None:
                print("No audio received")
                return ""
            print("Processing audio...")
            audio = self.recognizer.listen(source, timeout=5)
            text = ""

            try:
                print("Recognizing...")
                text = self.recognizer.recognize_google(audio)
                print(f"You said: {text}")
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception:
                print("An error occurred.")

            return text

    def speak(self):
        pass