import requests
import re
from bs4 import BeautifulSoup

print("Welcome to YT Scraper v0.1!")
v = ""
url = ""
term = ""
video_code = ""
subtitle_link = "http://video.google.com/timedtext?lang=en&v="
def create_link():
    url = input("Please enter the video URL: ")
    v = "?v="
    if v in url:
        video_code = url.split(v,1)[1]
        global subtitle_link + video_code
        print(subtitle_link)
    else:
        print("Sorry - I don't seem to recognise that link, please try again.")
        create_link()

def create_search_term():
    term = input("Please enter a word or phrase to search for: ")

def convert_s_to_m(seconds):
    se = seconds + 1
    return seconds + ", " + se

create_link()
create_search_term()
print("------")
print(subtitle_link)
print("http://video.google.com/timedtext?lang=en&v=qh5AdVTJgvo")

'''
html = requests.get("http://video.google.com/timedtext?lang=en&v=qh5AdVTJgvo").text

soup = BeautifulSoup(html, "lxml")

aaa = soup.find_all(string=re.compile('w'))
#print(aaa)
for element in aaa:
    b = element.parent
    time = b['start']
    d_time = double(time)
    sentence = b.text
    print("---")
'''
