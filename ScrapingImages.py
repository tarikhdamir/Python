from bs4 import BeautifulSoup
import requests
import os

url = f"https://www.shutterstock.com/ru/search/fruit"
res = requests.get(url, headers={"User-Agent": "XY"})
soup = BeautifulSoup(res.text, 'html.parser')

links = []
images = []
tags = soup.findAll("img")

for link in tags:
    src = link.attrs.get('src')
    if str(src) != "None":
        link = link.attrs.get('src')
        links.append(link)

image_count = 1

for image in links:
    with open('image_' + str(image_count) + '.jpg', 'wb') as f:
        res = requests.get(image)
        f.write(res.content)
        print("Saving image_" + str(image_count))
        image_count += 1
        if image_count > 5:
            exit(0)
