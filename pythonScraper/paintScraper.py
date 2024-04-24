import requests
from bs4 import BeautifulSoup

URL = "https://paintpad.app/paints/vallejo-game-color"
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

s = soup.find('ul', class_='paint-collection__paints') 
content = s.find_all('span', class_='paint-swatch__manufacturer-code') 

soupText = s.get_text()
replacedSoupText = soupText.replace("  ", "")

paintListRaw = replacedSoupText.split('\n')



def listCleaner():
    cleanedList = [x for x in paintListRaw if x != ""]
    print(cleanedList)

listCleaner()