#This is for greeting like Good Morning, Good Afternoon, Good Evening to the user

from datetime import datetime
from Functions.Speak import speak
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def greet_user():
    '''Greets according to the current time'''

    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?") 