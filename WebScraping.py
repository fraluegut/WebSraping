import urllib.request
from urllib.request import urlopen as uReq
datos = urllib.request.urlopen("https://www.openwebinars.net").read().decode()
#datos = urllib.request.urlopen("https://www.tripadvisor.es/").read().decode()
# Instalación de la librería
import sys

print("Datos: ")
#print(datos)



from bs4 import BeautifulSoup
soup =  BeautifulSoup(datos, "html.parser")
tags = soup("a")
for tag in tags:
    print("Href: " )
    print(tag.get("href"))


#Nuevo caso

#Librerías
import requests
url = "https://www.tripadvisor.es/Search?q=Sevilla&searchSessionId=023C7BAC6242C6185DAAD2551B7C57301587902270767ssid&searchNearby=false&sid=86088E5D3B33B29AB8D62D604F45C3861587902276346&blockRedirect=true&ssrc=h&rf=1"
peticion_hoteles = requests.get(url)
textourl = peticion_hoteles.text

print("Hoteles: ")
#print(textourl)

from bs4 import BeautifulSoup as bs
soup = bs.BeautifulSoup(textourl, "html.parser")
"""
#soup.find_all("div")[1].findChildren()

print("Cosas nuevas: ")
new_url = "https://hipertextual.com/2018/10/juegos-windows-linux"
uClient = uReq(url)
page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")
a = soup.find_all("")
print(a)
"""
print("1")
for url in soup.find_all('a'):
    print(url.get('href'))

#table = soup.table
#table = soup.find('table')

table_rows = table.find_all('tr')
print("Tablas: ")
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)