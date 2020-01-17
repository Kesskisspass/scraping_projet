# 
# Projet WebScraping
#

import requests
import pyexcel as pe
from bs4 import BeautifulSoup

scrapped_list = []
files = ['computers/laptops','computers/tablets','phones/touch']
for i in range(len(files)):
    print(f'https://www.webscraper.io/test-sites/e-commerce/allinone/{files[i]}')

allinone_response = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
soup = BeautifulSoup(allinone_response.content, 'html.parser')
items = soup.find_all('div', class_="thumbnail")

for item in items:
    price = item.find(class_="price").text[1:]
    title = item.find('a')['title']
    description = item.find('p', class_='description').text

    scrapped_list.append({
        "type": "computer",
        "title":title,
        "price": price,
        "description": description
        })
print(scrapped_list)
