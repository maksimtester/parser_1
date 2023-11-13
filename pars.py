import requests
from bs4 import BeautifulSoup

for i in range(1, 3):
    print(f"Parsing page {i}")
    url = f"https://quotes.toscrape.com/page/{i}" # определяем URL адрес
    response = requests.get(url) # делаем запрос на по этому URL
    soup = BeautifulSoup(response.text, 'lxml') # распознает HTML  документ
    quotes = soup.find_all('span', class_ = 'text')
    authors = soup.find_all('small', class_ = 'author')

    dt = {}

    for i in range(len(quotes)):
        dt[authors[i].text] = quotes[i].text

    print(dt)



