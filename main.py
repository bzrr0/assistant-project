import speech_recognition as sr

#Recognizer
r = sr.Recognizer()

#Microphone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) # Microphone as sound source
        print(r.recognize_google(audio, language='pt-br'))
...