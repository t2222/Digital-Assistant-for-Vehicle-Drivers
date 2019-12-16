import os
print ("1. Tech News\n")
print ("2. Top News\n")
print ("3. Football News\n")
print ("4. Cricket News\n")
num=int(input("Enter option:"))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR = "cd "+BASE_DIR
os.system(DIR)
if num==1:
    if os.path.exists('tech.csv'):
        os.system('del tech.csv')
    os.system('scrapy crawl tech -o tech.csv')
    os.system('start tech.csv')
elif num==2:
    if os.path.exists('news.csv'):
        os.system('del news.csv')
    os.system('scrapy crawl news -o news.csv')
    os.system('start news.csv')
elif num==3:
    if os.path.exists('football.csv'):
        os.system('del football.csv')
    os.system('scrapy crawl football -o football.csv')
    os.system('start football.csv')
else:
    if os.path.exists('cricket.csv'):
        os.system('del cricket.csv')
    os.system('scrapy crawl cricket -o cricket.csv')
    os.system('start cricket.csv')
