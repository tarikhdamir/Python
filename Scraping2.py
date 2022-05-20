# Importing Libraries
import csv
import requests
from bs4 import BeautifulSoup

pages = 3

for page in range(1, pages + 1):
    # Fetching Whole Source Code
    URL = f"http://quotes.toscrape.com/page/{page}"
    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    # Finding total number of quotes
    length = len(soup.select(".text"))

    with open('quotes.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([page])

    # Running a Loop and Fetching Quote and Author Name
    for i in range(0, length):
        quote = soup.select(".text")[i].get_text().strip()
        quote = quote.replace('“', "")
        quote = quote.replace('”', "")
        author = soup.select('.author')[i].get_text().strip()
        with open('quotes.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([quote + " " + author])
