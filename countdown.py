import time
import pyttsx3

engine = pyttsx3.init()

def countdown(seconds):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1

    print("Goodnight!")
    speak_text = "Goodnight!"
    engine.say(speak_text)
    engine.runAndWait()

try:
    while True:
        total_seconds = int(input("I'll leave in : "))
        countdown(total_seconds)
except ValueError:
    print("Please enter a valid integer for seconds.")
    