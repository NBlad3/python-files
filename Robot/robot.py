import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()

while True:
    with speech_recognition.Microphone() as mic:
        print("I'm listening")
        audio = robot_ear.listen(mic)

    try:
        message = robot_ear.recognize_google(audio)
    except:
        message = ""

    if message == "":
        message = "Error"
    elif message == "hello":
        message = "Hello."
    elif message == "how are you":
        message = "I'm fine, how are you?"
    elif message == "how old are you":
        message = "I'm 0 years old."
    elif "time" in message:
        message = datetime.now().strftime("It's %H:%M")
    elif "day" in message:
        message = date.today().strftime("It's the %d of %B, %Y")
    elif message == "stop":
        break
    else:
        message = "Sorry. I don't understand."

    print(message)
    robot_mouth.say(message)
    robot_mouth.runAndWait()
