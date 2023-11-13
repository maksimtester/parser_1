import csv
import requests
from bs4 import BeautifulSoup

data = {}

for i in range(1, 3):
    print(f"Parsing page {i}")
    url = f"https://quotes.toscrape.com/page/{i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('span', class_ = 'text')
    authors = soup.find_all('small', class_ = 'author')
    tags = soup.find_all('div', class_="tags")

    for i in range(len(quotes)):
        author = authors[i].text
        quote = quotes[i].text
        tag = tags[i].text

        if author not in data:
            data[author] = []
        
        data[author].append([quote, tag])  # в виде списка


# Write the data to a CSV file
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Author', 'Quote', 'Tags']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for author, quotes_with_tags in data.items():
        for quote, tag in quotes_with_tags:
            writer.writerow({'Author': author, 'Quote': quote, 'Tags' : tag})