from bs4 import BeautifulSoup
import requests
import psycopg2
from bs4 import BeautifulSoup

url = 'https://www.gismeteo.ru/weather-bishkek-5327/10-days/'
chart_data = ''

response = requests.get(url)
sup = BeautifulSoup(response.text, 'html.parser')
pogoda = sup.find_all('div', class_='widget-row-chart widget-row-chart-temperature row-with-caption')


chart_data += pogoda + '.\n'
