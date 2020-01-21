import requests
from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(requests.get('https://www.riatomsk.ru/').text, "html.parser")

soup_find = soup.find_all('div', ['newItem', 'actNew'])
posts = []

main_new = soup.find('div', ['def-main-new'])
title = main_new.find('div', 'mainTitle').text[:-5]
time = main_new.find('div', 'mainTime').text
content = main_new.find('div', 'mainAnons').text

posts.append({
                'title':title,
                'time':time,
                'content':content
            })

for i in soup_find:
        title = i.find(['div'], ['mainTitle', 'newItem-s', 'actNew-a']).text
        time = i.find(['div', 'span'], ['newItem-f', 'actNew-d']).text
        posts.append({
                        'title':title,
                        'time':time,
                        'content':'N/A'
                    })
for i in range(len(posts)):
    print(posts[i]['time'])
    print(posts[i]['title'])
    if posts[i]['content'] != "N/A":
        print(posts[i]['content'])
    print('\n')





