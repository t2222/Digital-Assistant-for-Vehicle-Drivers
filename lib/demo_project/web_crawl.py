"""
@author: Porosh
"""
import os
import pyttsx3
import time
import speech_recognition as sr

eng=pyttsx3.init()
def speak(text):
    try:
        eng.setProperty('rate',150);eng.setProperty('volume',.9)
        eng.say(text)
        eng.runAndWait()
    except:
        pass


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

def web_crawling():
    speak("Say your option, we have Top News, Tech News, Football news and Cricket news or you can give input manually.")
    print ("1. Tech News\n")
    print ("2. Top News\n")
    print ("3. Football News\n")
    print ("4. Cricket News\n")
    num=int(input("Enter option:"))
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DIR = "cd "+BASE_DIR
    lines=""
    engine=""
    os.system(DIR)
    
    os.chdir('C:/Users\Tousif/Digital Assistant/lib/demo_project/')
    
     
    if num==1:
        if os.path.exists('tech.csv'):
            os.system('del tech.csv')
        os.system('scrapy crawl tech -o tech.csv')
        os.system('start tech.csv')
        DIR = BASE_DIR+"\\tech.csv"
        with open(DIR) as f:
            # if the `q` key was pressed, break from the loop
            lines=f.readlines()
            
    elif num==2:
        if os.path.exists('news.csv'):
            os.system('del news.csv')
        os.system('scrapy crawl news -o news.csv')
        os.system('start news.csv')
        DIR = BASE_DIR+"\\news.csv"
        with open(DIR) as f:
            lines=f.readlines()
            
    elif num==3:
        if os.path.exists('football.csv'):
            os.system('del football.csv')
        os.system('scrapy crawl football -o football.csv')
        os.system('start football.csv')
        DIR = BASE_DIR+"\\football.csv"
        with open(DIR) as f:
            lines=f.readlines()
            
    elif num==4:
        if os.path.exists('cricket.csv'):
            os.system('del cricket.csv')
        os.system('scrapy crawl cricket -o cricket.csv')
        os.system('start cricket.csv')
        DIR = BASE_DIR+"\\cricket.csv"
        with open(DIR) as f:
            lines=f.readlines()
            
    #lines.replace("\t","")
    val=""
    for x in lines:
        val=val+x
    #val.replace("\t","")
    print(val)
    eng.say(val)
    eng.runAndWait()
    
    key = engine.waitKey(1) & 0xFF
         
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        eng.stop()
    
    
   
    
    