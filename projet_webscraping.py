# 
# Projet WebScraping
#

import requests
import pyexcel as pe
from pyexcel_ods3 import save_data
from bs4 import BeautifulSoup

scrapped_list = []
types = ['laptops','laptops','touch']
files = {'laptops':'computers/laptops','laptops':'computers/tablets','touch':'phones/touch'}

for typ in types:

    allinone_response = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/'+files[typ])
    soup = BeautifulSoup(allinone_response.content, 'html.parser')
    items = soup.find_all('div', class_="thumbnail")

    for item in items:
        price = item.find(class_="price").text[1:]
        title = item.find('a')['title']

        scrapped_list.append({
            "type": typ,
            "title":title,
            "price": price
            })

sheet = pe.get_sheet(records = scrapped_list)
save_data("scrap.ods",sheet)
#save_data("your_file.ods", sheet)
print(sheet)