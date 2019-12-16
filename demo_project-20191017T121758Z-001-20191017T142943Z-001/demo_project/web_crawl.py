"""
@author: Porosh
"""
import os
import pyttsx3
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
if num==1:
    if os.path.exists('tech.csv'):
        os.system('del tech.csv')
    os.system('scrapy crawl tech -o tech.csv')
    os.system('start tech.csv')
    engine = pyttsx3.init()
    DIR = BASE_DIR+"\\tech.csv"
    with open(DIR) as f:
        lines=f.readlines()
elif num==2:
    if os.path.exists('news.csv'):
        os.system('del news.csv')
    os.system('scrapy crawl news -o news.csv')
    os.system('start news.csv')
    DIR = BASE_DIR+"\\news.csv"
    engine = pyttsx3.init()
    with open(DIR) as f:
        lines=f.readlines()
elif num==3:
    if os.path.exists('football.csv'):
        os.system('del football.csv')
    os.system('scrapy crawl football -o football.csv')
    os.system('start football.csv')
    DIR = BASE_DIR+"\\football.csv"
    engine = pyttsx3.init()
    with open(DIR) as f:
        lines=f.readlines()
elif num==4:
    if os.path.exists('cricket.csv'):
        os.system('del cricket.csv')
    os.system('scrapy crawl cricket -o cricket.csv')
    os.system('start cricket.csv')
    DIR = BASE_DIR+"\\cricket.csv"
    engine = pyttsx3.init()
    with open(DIR) as f:
        lines=f.readlines()
#lines.replace("\t","")
val=""
for x in lines:
    val=val+x
#val.replace("\t","")
print(val)
engine.say(val)
engine.runAndWait()