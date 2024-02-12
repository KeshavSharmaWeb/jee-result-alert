import requests
from playsound import playsound
import bs4
import time

url = "https://jeemain.nta.ac.in/"


def new():
    str_html = bs4.BeautifulSoup(requests.get(url).content, features="lxml")

    news = str_html.find("div", attrs={"class": "news-eve-scroll pr-2"})

    a = list(news.find_all("li"))

    if a.__len__() > 18:
        playsound("resulttt.mp3")
        print("AA GYAAAAA")
    else:
        print("nhi aaya")
        print(a.__len__())

    time.sleep(60)
    new()
new()
