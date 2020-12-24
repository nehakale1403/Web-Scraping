# If you want to scrape any website
# 1. Use the API
# 2. HTML web scraping using some tool like bs4

# Step1: requirements
# py -m pip install requests
# py -m pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

#Step2: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

#Step3: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
#print(soup.prettify) #prettifies the content and then displayed

#Step4: HTML Tree traversal
#commonly used types of objects
# #1. tag
# print(type(title))
# #2. NavigableString
# print(type(title.string))
# #3. BeautifulSoup
# print(type(soup))
#4. comment
# markup = "<p><!--this is a comment--></p>"
# soup2 = BeautifulSoup(markup)
# print(type(soup2.p.string))

#getting the title of the html page
title = soup.title

#get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

#get all the anchor tags from the page
anchors = soup.find_all('a')
# print(anchors)

#get all the links from the page
# all_links = set() #we are making set so that the links do not get repeated
# for link in anchors:
#     if(link.get('href') !='#'):
#         linktext = "https://codewithharry.com" + link.get('href')
#         all_links.add(link)
#         print(linktext)


#get first paragraph in the html page
# print(soup.find('p')) 

#get classes of any element in the html page
# print(soup.find('p')['class'])

#find all the elements with class 'lead'
# print(soup.find_all('p', class_="lead"))

#get the text from the tags/soup
# print(soup.find('p').get_text())
# print(soup.get_text())

navbarSupportedContent = soup.find(id = 'navbarSupportedContent')

# .contents- a tag's children are available as a list ...it gets saved into the memory
# .children - a tag's children are available as a generator ....it does not get saved hence fast and efficient
# for elem in navbarSupportedContent.contents:
#     print(elem)

# for item in navbarSupportedContent.strings:
#     print(item)

# for item in navbarSupportedContent.stripped_strings:
#     print(item)

# print(navbarSupportedContent.parent)
# for item in navbarSupportedContent.parents:
#     print(item.name)

#next sibling and previous sibling

# print(navbarSupportedContent.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling) blank lines are also considered as sibling

elem = soup.select('#liginModel')
print(elem)


