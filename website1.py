import json
import requests
from bs4 import BeautifulSoup

url = "https://www.instructables.com/Building-a-Self-Driving-Boat-ArduPilot-Rover/"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

#header title
header_title = soup.title
print(header_title.string)

#youtube_url
anchors = soup.find_all('a')
for link in anchors:
    proper_link = str(link.get('href'))
    if "youtube" in proper_link:
        print(proper_link)

#image url
images = soup.find_all('img')
for image in images:
    print(image['src']+'\n')

#view count
view_count = soup.find('p', class_="svg-views view-count")
print(view_count.string)

#favourite count
favourite_count = soup.find('p', class_ = "svg-favorite active favorite-count")
print(favourite_count.string)

#comments count
comments_count = soup.find('p', class_ = "svg-comments active comment-count")
print(comments_count.string)

#step titles

step_titles = soup.find_all('h2', class_="step-title")
for step_title in step_titles:
    print(step_title.string)


