# 
# Projet WebScraping
#

# Import des plugins nécessaires
import requests
import pyexcel as pe
from pyexcel_ods3 import save_data
from bs4 import BeautifulSoup


types = ['laptops','laptops','touch']
files = {'laptops':'computers/laptops','tablets':'computers/tablets','touch':'phones/touch'}

# Création de l'objet liste qui contiendra tous mes items
items_lists = []

# On boucle sur les types de matériel
for typ in types:

    # On génère l'url à scrapper
    allinone_response = requests.get('https://www.webscraper.io/test-sites/e-commerce/allinone/'+files[typ])
    
    # On fait la requete
    soup = BeautifulSoup(allinone_response.content, 'html.parser')

    # On récupère chaque item
    items = soup.find_all('div', class_="thumbnail")

    # On récupère les infos de chaque item et on les met dans une liste
    for item in items:
        price = item.find(class_="price").text[1:]
        title = item.find('a')['title']

        items_lists.append([typ,title,price])

#print(items_lists)

# On exporte notre liste de liste dans un fichier .ods
save_data("scrap.ods", {"Feuille 1" :items_lists})