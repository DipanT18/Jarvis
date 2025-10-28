#This file contains speech engine configuration constants
#The actual engine is initialized in Speak.py

from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')