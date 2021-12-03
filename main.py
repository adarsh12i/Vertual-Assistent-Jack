import datetime
import speech_recognition as s
import pyttsx3
import pywhatkit

listener = s.Recognizer()
speak = pyttsx3.init('sapi5')
voices = speak.getProperty('voices')
speak.setProperty('voice', voices[1].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak.say("I'm your created")
        speak.runAndWait()
        speak.say("Personal Assistant")
        speak.runAndWait()
        speak.say("Emilia Clarke")
        speak.runAndWait()
        speak.say("Good Morning Adarsh !")
        speak.runAndWait()
        speak.say("How was your day !")
        speak.runAndWait()

    elif hour >= 12 and hour < 18:
        speak.say("I'm your created")
        speak.runAndWait()
        speak.say("Personal Assistant")
        speak.runAndWait()
        speak.say("Emilia Clarke")
        speak.runAndWait()
        speak.say("Good afternoon Adarsh !")
        speak.runAndWait()
        speak.say("How was your day !")
        speak.runAndWait()

    else:
        speak.say("I'm your created")
        speak.runAndWait()
        speak.say("Personal Assistant")
        speak.runAndWait()
        speak.say("Emilia Clarke")
        speak.runAndWait()
        speak.say("Good Evening Adarsh !")
        speak.runAndWait()
        speak.say("How was your day !")
        speak.runAndWait()

wishMe()

def our_order():
    with s.Microphone() as input:
        print("Your Assistant Emilia Clarke is ready")
        our_input = listener.listen(input)
        text = listener.recognize_google(our_input)
        print(text)
    return text

def great():
    command = our_order()
    speak.say("good but I really missed you Adarsh")
    speak.runAndWait()
    speak.say("what can i do for you")
    speak.runAndWait()

great()

def Clarke():
    command = our_order()
    if 'yourself'in command:
        speak.say("I'm your created")
        speak.runAndWait()
        speak.say("Personal Assistant")
        speak.runAndWait()
        speak.say("Emilia Clarke")

    elif 'for me' in command:
        speak.say("I can do everything you just need to say")
        speak.runAndWait()
        speak.say("such as open any application for you")
        speak.runAndWait()
        speak.say("search any thing on Chrome")
        speak.runAndWait()
        speak.say("I can reed any text whatever you mark")
        speak.runAndWait()
        speak.say("I can play a Video song for you")
        speak.runAndWait()
        speak.say("reed or write watsup messages and mails as well")
        speak.runAndWait()
        speak.say("open web page for you set alarms")
        speak.runAndWait()
        speak.say("And many more")
        speak.runAndWait()

    elif 'play' in command:
        our_song = command.replace("then Clarke play the song","")
        speak.say("Yes Adarsh I'm playing your video song")
        speak.runAndWait()
        pywhatkit.playonyt(our_song)

    else:
        speak.say("I'm not able to here you sir")
        speak.runAndWait()

while True:
    Clarke()



