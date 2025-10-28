import speech_recognition as sr
from random import choice
from datetime import datetime
from Functions.utils import opening_text
from Functions.Speak import speak

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    # Option to use text input for testing (set to True for debugging)
    USE_TEXT_INPUT = False
    
    if USE_TEXT_INPUT:
        query = input("Enter your command: ")
        print(f"User typed: {query}")
        if not ('exit' in query.lower() or 'stop' in query.lower()):
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
        return query

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        
        if not ('exit' in query.lower() or 'stop' in query.lower()):
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 or hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except sr.UnknownValueError:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    except sr.RequestError as e:
        speak('Sorry, there was an error with the speech recognition service.')
        print(f"Speech recognition error: {e}")
        query = 'None'
    except Exception as e:
        speak('Sorry, something went wrong. Could you please try again?')
        print(f"Unexpected error: {e}")
        query = 'None'
    
    return query
