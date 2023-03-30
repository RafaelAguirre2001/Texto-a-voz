import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)

engine.setProperty('volumen', 0.5)

engine.say('Hola mundo')

engine.runAndWait()