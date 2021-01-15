#API: 10218686935504422
import json
import requests 
from bs4 import BeautifulSoup
URL = 'https://www.superheroapi.com/ids.html'

heroes_page = requests.get(URL).text
heroes_parser = BeautifulSoup(heroes_page, 'html.parser')
heroes_data = {}

for row in heroes_parser.find_all('tr'):
    ids, name = row.find_all('td')[0].get_text(), row.find_all('td')[1].get_text()
    heroes_data[name] = ids

with open('heroes_data.json', 'w+') as f:
    json_data = json.dumps(heroes_data)
    f.write(json_data)