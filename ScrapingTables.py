from bs4 import BeautifulSoup
import csv
import requests

url = "http://pokemondb.net/pokedex/all"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

table = soup.find_all('table')[0]
table_header = table.find('thead').find_all('th')

with open('table.csv', 'a', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    header = []
    for th in table_header:
        header.append(th.text)
    print(header)
    writer.writerow(header)
    for row in table.find_all('tr'):
        body = []
        for data in row.find_all('td'):
            body.append(data.text)
        print(body)
        writer.writerow(body)
