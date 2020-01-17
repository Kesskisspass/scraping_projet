# =============================================================================
# Beautiful Soup
# =============================================================================
import requests
from bs4 import BeautifulSoup

# perdu_response = requests.get('http://perdu.com')

# soup = BeautifulSoup(perdu_response.content,'html.parser')

#print(f'Titre de la page : {soup.title.text}')

# boursorama = requests.get('https://www.boursorama.com/bourse/devises/cryptomonnaies-bitcoin-euro-BTC-EUR/')
# soup2 = BeautifulSoup(boursorama.content,'html.parser')
# fpi = soup2.find_all('div', class_='c-faceplate__values')
# cours_eur = fpi[0].find_all('span', class_= 'c-instrument')

# prix_eur_ttc = cours_eur[0].text
# variation_eur = cours_eur[1].text
# print(f'Le cours du bitcoin est de {prix_eur_ttc} Euros, et sa variation de {variation_eur}')

seloger = requests.get('https://www.seloger.com/list.htm?projects=2,5&types=1,2&natures=1,2,4&places=[{ci:640122}]&price=300000/600000&enterprise=0&qsVersion=1.0')
soup3 = BeautifulSoup(seloger.content,'html.parser')
test = soup3.find_all('div', class_= re.compile("block__ShadowedBlock"))
print(test)