import speech_recognition as sr
import os
import keyboard
import subprocess as sp
import imdb
import pyttsx3 as p
import datetime as dt
import webbrowser as wb
from online import *
import wolframalpha as w
engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

listening = False

def start_listening():
    global listening
    listening = True
    print("started listening")

def pause_listening():
    global listening
    listening = False
    print("stopped listening")

keyboard.add_hotkey('alt+k', start_listening)
keyboard.add_hotkey('alt+p', pause_listening)

# Greeting message according to time
def wish_me():
    hour = dt.datetime.now().hour
    if 0 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 16:
        return "Good afternoon"
    else:
        return "Good evening"

# Take user input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 8000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
        return ""

if __name__ == '__main__':
    speak(f"Hello sir, {wish_me()} I am alex, your virtual assistant.")
    speak("How may i assist you?")
    while True:
        if listening:
            query = take_command()
            sites = [
                ["instagram", "https://www.instagram.com"],
                ["facebook", "https://www.facebook.com"],
                ["spotify", "https://open.spotify.com/playlist/37i9dQZF1E3adjRREOCkuP"],
                ["whatsapp", "https://web.whatsapp.com/"]
            ]

            for site in sites:
                if f"open {site[0]}" in query:
                    speak(f"Opening {site[0]} sir...")
                    wb.open(site[1])

            apps = [
                ["powerpoint",
                    r'"C:\Program Files (x86)\Microsoft Office\root\Office16\POWERPNT.EXE"'],
                ["document file",
                    r'"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"'],
                ["zoom", r'"C:\Users\ashish patel\AppData\Roaming\Zoom\bin\Zoom.exe"']
            ]
            for app in apps:
                if f"open {app[0]}" in query:
                    speak(f"Opening {app[0]} sir...")
                    os.system(app[1])

            if "time" in query:
                today_date = dt.datetime.now()
                speak('Sir, it\'s currently ' + today_date.strftime('%I:%M %p'))

            elif "date" in query:
                today_date = dt.datetime.now()
                speak('Today is ' + today_date.strftime('%d') +
                      ' of ' + today_date.strftime('%B'))

            elif "weather" in query:
                speak('according to today weather report the')
                speak('Temperature in Gwalior is ' + str(temp()) +
                      ' degree Celsius' + ' and with ' + str(des()))

            elif "open youtube" in query:
                speak("What do you want to play on youtube sir?")
                video = take_command().lower()
                speak(f"i am  playing {video} on youtube")
                youtube(video)

            elif "open google" in query:
                speak(f"What do you want to search on google sir")
                query = take_command().lower()
                speak(f"i am  searching {query} on google")
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want to search on wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to wikipedia,{results}")
                speak("I am printing in on terminal")
                print(results)

            elif "send email" in query or "email" in query or "send the email" in query:
                try:
                    speak("On what email address do you want to send sir?. Please enter in the terminal")
                    receiver_add = input("Enter the email address of the reciver: ")
                    speak("What should be the subject sir?")
                    subject = take_command().capitalize()
                    speak("What is the message ?")
                    message = take_command().capitalize()
                    if send_email(receiver_add, subject, message):
                        speak("I have sent the email sir")
                        print("I have sent the email sir")
                    else:
                        speak("something went wrong Please check the error log")
                        print("Something went wrong. Please check the error log.")
                except KeyboardInterrupt:
                    print("\nProcess interrupted.")

            elif "give me news" in query:
                speak(f"I am reading out the latest headline of today,sir")
                speak(get_news())
                speak("I am printing it on screen sir")
                print(*get_news(), sep='\n')

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)
            elif "play music" in query:
                speak("playing music  sir")
                music = "C:\\Users\\ashish patel\\OneDrive\\Desktop\\music1.mp3"
                os.startfile(music)
            elif "open notepad" in query:
                speak("Opening Notepad for you sir")
                notepad_path = "C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)
            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')
            elif 'movie' in query:
                movies_db= imdb.IMDb()
                speak("Please tell me the movie name:")
                text = take_command()
                movies = movies_db.search_movie(text)
                speak("searching for" + text)
                speak("I found these")
                for movie in movies:
                    title = movie["title"]
                    year = movie["year"]
                    speak(f"{title}-{year}")
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    rating = movie_info["rating"]
                    cast = movie_info.get('cast', [])
                    cast_names = [actor["name"] for actor in cast[:5]]  # Get names of first two cast members
                    cast_string = ", ".join(cast_names)
                    plot = movie_info.get('plot outline', 'plot summary not available')
                    speak(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {cast_string}. "
                          f"The plot summary of movie is {plot}")
                    speak('i am printing on terminal')
                    print(f"{title} was released in {year} has imdb ratings of {rating}.\n It has a cast of {cast_string}. \n"
                          f"The plot summary of movie is {plot}")
            elif "stop" in query.lower():
                hour = dt.datetime.now().hour
                if hour >= 21 and hour < 6:
                    speak("Good night sir,take care!")
                else:
                    speak("Have a good day sir!")
                    exit()
