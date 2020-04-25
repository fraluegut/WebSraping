import urllib.request

datos = urllib.request.urlopen("https://www.openwebinars.net").read().decode()

# Instalación de la librería
import sys


from bs4 import BeautifulSoup
soup =  BeautifulSoup(datos)
tags = soup("a")
for tag in tags:
    print(tag.get("href"))