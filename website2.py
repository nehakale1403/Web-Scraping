import json
import requests
from bs4 import BeautifulSoup

url = "https://www.instructables.com/Hydraulic-Craft-Stick-Box/"

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')

#header title
header_title = soup.title
print(header_title.string)

#youtube_url
anchors = soup.find_all('a')
ytlink=None
for link in anchors:
    proper_link = str(link.get('href'))
    if "youtube" in proper_link:
        ytlink = proper_link

#image url
images = soup.find_all('img')
imglist = []
for image in images:
    imglist.append(image['src'])

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
steplist = []
for step_title in step_titles:
    steplist.append(step_title.string)

dictionary = {
    "header_title" : header_title.string,
    "youtube_url" : ytlink,
    "image_url" : imglist,
    "view_count" : view_count.string,
    "favourite_count" : favourite_count.string,
    "comments_count" : comments_count.string,
    "step_titles" : steplist
}

with open("sample2.json", "w") as outfile:
    json.dump(dictionary, outfile)


