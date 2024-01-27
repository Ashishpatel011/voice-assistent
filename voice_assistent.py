import pyttsx3 as p
import speech_recognition as sr
from w_info import *
from w_news import *
from w_yt import *
import randfacts as rd
from w_joke import *
from w_weather import*
import datetime as dt

engine= p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',160)
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speek(text):
    engine.say(text)
    engine.runAndWait() 

def wishme():
    hour=int(dt.datetime.now().hour)
    if hour>0 and hour<12:
        return('good morning ')
    elif hour>12 and hour<16:
        return('good afternoon ')
    else:
        return('good eveaning ')
today_date=dt.datetime.now()
r=sr.Recognizer()
speek('hellow sir,'+ wishme()+ 'i am your voice assistent.')
speek('today is '+ today_date.strftime('%d') + 'of'+ today_date.strftime('%B') + ' and its currently ' + (today_date.strftime('%I')) + (today_date.strftime('%M'))+(today_date.strftime('%p')))
speek('temperature in gwalior is'+str(temp())+ 'degree celcius' +'  and with   '+str(des()))   
speek('how are you')
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening....')
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if 'what' and 'about' and 'you' in text:
    speek('i am also having a good day sir')
speek ('what can i do for you ')

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('listening....')
    audio=r.listen(source)
    text2=r.recognize_google(audio)
# to rum information from google   
if 'information' in text2:
    speek('you need information related to which topic')
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening....')
        audio=r.listen(source)
        infor=r.recognize_google(audio)
    speek('searching {} in wikipedia'.format(infor))
    assist=infow()
    assist.get_info(infor)
# to play youtube video
elif 'play' and 'video' in text2:
    speek('you want to play which video ')
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('listening....')
        audio=r.listen(source)
        vdo=r.recognize_google(audio)
    speek('playing {} in youtube'.format(vdo))
    assist=music()
    assist.play(vdo)
# to speek news
elif 'news' in text2:
    speek('i will read news for you')
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speek(arr[i]) 
# for jokes
elif 'funny' in text2:
    speek('sure sir, get ready for some CHUCKLES')
    ar=joke() 
    print(ar[0])
    speek(ar[0])
    print(ar[1])
    speek(ar[1])
# for facts
elif 'facts' or 'fact' in text2:
    speek('SURE SIR, i will read some facts for you')   
    x=rd.getFact()
    print(x) 
    speek('did you know that'+x)