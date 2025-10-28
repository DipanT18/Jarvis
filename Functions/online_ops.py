import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config

#Getting my IP address
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

#Searching on wikipedia
def search_on_wikipedia(query):
    try:
        results = wikipedia.summary(query, sentences=2)
        return results
    except wikipedia.exceptions.DisambiguationError as e:
        # If multiple pages found, use the first option
        results = wikipedia.summary(e.options[0], sentences=2)
        return results
    except wikipedia.exceptions.PageError:
        # If no page found, try searching for similar pages
        try:
            search_results = wikipedia.search(query, results=1)
            if search_results:
                results = wikipedia.summary(search_results[0], sentences=2)
                return results
            else:
                return f"Sorry, I couldn't find any information about '{query}' on Wikipedia."
        except:
            return f"Sorry, I couldn't find any information about '{query}' on Wikipedia."
    except Exception as e:
        return f"Sorry, there was an error searching Wikipedia: {str(e)}"

#Playing youtube video
def play_on_youtube(video):
    try:
        kit.playonyt(video)
        return f"Playing '{video}' on YouTube"
    except Exception as e:
        print(f"Error playing YouTube video: {e}")
        return f"Sorry, I couldn't play '{video}' on YouTube"

#For google search
def search_on_google(query):
    try:
        kit.search(query)
        return f"Searching for '{query}' on Google"
    except Exception as e:
        print(f"Error searching Google: {e}")
        return f"Sorry, I couldn't search for '{query}' on Google"

#Sending whatsapp message
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+977{number}", message)

#For sending email
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

#For getting news
NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    try:
        news_headlines = []
        res = requests.get(
            f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
        
        if "articles" in res and res["articles"]:
            articles = res["articles"]
            for article in articles:
                news_headlines.append(article["title"])
            return news_headlines[:5]
        else:
            return ["Sorry, I couldn't fetch the latest news at the moment."]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return ["Sorry, I couldn't fetch the latest news at the moment."]

#Getting weather information
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    try:
        res = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
        
        if "weather" in res and "main" in res:
            weather = res["weather"][0]["main"]
            temperature = res["main"]["temp"]
            feels_like = res["main"]["feels_like"]
            return weather, f"{temperature}℃", f"{feels_like}℃"
        else:
            return "Unknown", "N/A", "N/A"
    except Exception as e:
        print(f"Error fetching weather: {e}")
        return "Unknown", "N/A", "N/A"

#Getting random jokes
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

#Getting random advice
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

#Getting trending movies
def get_trending_movies():
    try:
        # Using TMDB API for trending movies (you may need to get an API key)
        # For now, returning a sample list
        trending_movies = [
            "Spider-Man: No Way Home",
            "The Batman",
            "Doctor Strange in the Multiverse of Madness",
            "Top Gun: Maverick",
            "Black Panther: Wakanda Forever"
        ]
        return trending_movies
    except Exception as e:
        print(f"Error fetching trending movies: {e}")
        return ["Unable to fetch trending movies at the moment"]
