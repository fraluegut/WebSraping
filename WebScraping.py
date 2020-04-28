import urllib.request

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
print(textourl)

from bs4 import BeautifulSoup
soup = BeautifulSoup(textourl, "html.parser")

soup.find_all("div")[1].findChildren()