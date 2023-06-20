from datetime import datetime
import speech_recognition as sr
import pyttsx3
import openai
import os
from dotenv import load_dotenv
load_dotenv()


vi = "com.apple.voice.compact.en-ZA.Tessa"

# Local speech engine initialisation
engine = pyttsx3.init()
# voices = engine.getProperty('voices') # 0 = male, 1 = female
engine.setProperty('voice', vi) 
activationWord = 'computer' #Single word

def speak(text, rate = 130):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()

def parseCommand():
        listener = sr.Recognizer()
        speak('Listening for a command')
        print('Listening for a command')

        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source,duration=1)
            listener.pause_threshold = 0.5
            input_speech = listener.listen(source)
        try:
            print('Recognizing speech...')
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f'The input speech was: {query}')

        except Exception as exception:
            print('I did not quite catch that')
            speak('I did not quite catch that')
            print(exception)
            

            return 'None'

        return query

def query_openai(prompt = ""):
    openai.organization = 'org-1M2cbgdjE36l16JJYvDlGPpI'
    openai.api_key = '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'
     #Temperature is a measure of randonmess
     #Max_tokens is the number of tokens to generate
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=200,

    )

    return response.choices[0].text

# Main loop
if __name__ == '__main__': 
    speak('Good Evening, Natural Learning Youth Assistant Powering up in 5, 4, 3, 2, 1. All Systems Go, Project Nyla Online sir', 150)
""" voices = engine.getProperty('voices')
  
for voice in voices:
    # to get the info. about various voices in our PC 
    print("Voice:")
    print("ID: %s" %voice.id)
    print("Name: %s" %voice.name)
    print("Age: %s" %voice.age)
    print("Gender: %s" %voice.gender)
    print("Languages Known: %s" %voice.languages) """
 
while True:
        # Parse as a list
        query = parseCommand().lower().split()

        if query[0] in activationWord:
            query.pop(0)

            # Set commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Hello, Oak 10 Gold!')
                else:
                    query.pop(0) # Remove 'say'
                    speech = ' '.join(query) 
                    speak(speech)
            if query[0] == 'who':
                if 'you' in query:
                    speak('I am version 2 of Project N Y L A or Nyla for short. I am a python based Artificial Assistant that can do a number of things but i primarily serve as a base for Oakland Cohorts to create with!', 150)
                else:
                    query.pop(0) # Remove 'who'
                    speech = ' '.join(query) 
                    speak(speech)
                    print(speech)

            # Query OpenAI
            if query[0] == 'insight':
                query.pop(0) # Remove 'insight'
                query = ' '.join(query)
                speech = query_openai(query)
                speak("Ok")
                speak(speech)
                print(speech)

            # Note taking
            if query[0] == 'log':
                speak('Ready to record your note')
                newNote = parseCommand().lower()
                now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(now)
                    newFile.write(' ')
                    newFile.write(newNote)
                speak('Note written')

            if query[0] == 'exit':
                speak('Goodbye')
                break
