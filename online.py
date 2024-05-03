import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib


EMAIL = "iamashish761@gmail.com"
PASSWORD = "vpxjoaukdfpgmzxe"

def find_my_ip():
    ip_address = requests.get('https://api.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

def send_email(receiver_add, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)

        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(EMAIL, PASSWORD)
            s.send_message(email)

        return True
    except Exception as e:
        print("Error:", e)
        return False


# newss
def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey"
                          f"=c153f2d358604006a01da61ca705ec2b").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]


# weatherr
key='6df5771e86fcd7302e7024df221ac938'
api_address='https://api.openweathermap.org/data/2.5/weather?q=gwalior&appid='+key
json_data=requests.get(api_address).json()

def temp():
    temprature=round(json_data["main"]["temp"]-273,1)
    return temprature
def des():
    description=json_data['weather'][0]['description']
    return description
