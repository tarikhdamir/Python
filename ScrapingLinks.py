from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
name = soup.select(".title")

for a_tag in soup.findAll("a"):
    href = a_tag.attrs.get("href")
    if href != "":
        print(href)
        continue
