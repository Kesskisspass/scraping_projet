# 
# Projet WebScraping
#

# Import des plugins nécessaires
import requests
import pyexcel as pe
from pyexcel_ods3 import save_data
from bs4 import BeautifulSoup


types = ['laptops','laptops','touch']
files = {'laptops':'computers/laptops','laptops':'computers/tablets','touch':'phones/touch'}
items_lists = []
for typ in types:

    allinone_response = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/'+files[typ])
    soup = BeautifulSoup(allinone_response.content, 'html.parser')
    items = soup.find_all('div', class_="thumbnail")

    for item in items:
        price = item.find(class_="price").text[1:]
        title = item.find('a')['title']

        items_lists.append([typ,title,price])

#print(items_lists)

save_data("scrap.ods", {"Feuille 1" :items_lists})

