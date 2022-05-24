from bs4 import BeautifulSoup
import requests
import csv


def amazon(book):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    book = book.replace(" ", '+')
    url = f'https://www.amazon.com/s?k={book}&ref=nb_sb_noss_2'
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    length = len(soup.select(".a-size-medium"))
    print(res)
    for i in range(length):
        price = soup.select(".a-spacing-top-small .a-price-whole")[i].get_text().strip()
        currency = soup.select(".a-spacing-top-small .a-price-symbol")[i].get_text().strip()
        name = soup.select(".a-size-medium.a-color-base.a-text-normal")[i].get_text().strip()
        link = soup.select("h2 .a-link-normal.a-text-normal")[i].attrs.get("href")
        print(name + ' ' + price + currency + '\namazon.com' + link)


amazon(input("Enter the book name:\n"))
