import requests
import re
import string
from bs4 import BeautifulSoup

print("Welcome to YT Scraper v0.1!")
print("---------------------------")
subtitle_link = "http://video.google.com/timedtext?lang=en&v="
yt_url_base = "www.youtube.com/watch?v="
def create_link():
    url = input("Please enter the video URL: ")
    v = "?v="
    if v in url:
        video_code = url.split(v,1)[1]
        global vc
        vc = video_code
        return subtitle_link + video_code
    else:
        print("Sorry - I don't seem to recognise that link, please try again.")
        create_link()

def create_search_term():
    return input("Please enter a word or phrase to search for: ")

def convert_s_to_m(seconds):
    se = seconds + 1
    return seconds + ", " + se

html = requests.get(create_link()).text

soup = BeautifulSoup(html, "lxml")

print("")
results = soup.find_all(string=re.compile(create_search_term()))
print("")
for element in results:
    parent_e = element.parent
    time = parent_e['start']
    sentence = str(parent_e.text).replace('&#39;', '\'')

    time_string = str(time)[:-3]
    print("Sentence: " + sentence),
    print("Link: " + yt_url_base + vc + "&t=" + time_string + "s")
    print("")





















######
