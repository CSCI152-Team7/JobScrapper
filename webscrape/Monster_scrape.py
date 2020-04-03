# Name: Fausto Preciado
# Date: 3/26/20
# Description: Project for CSCI-152, job scrapper.
# Scrapping the monster job website.

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import pandas as pd

#Enter the location on the command prompt.
location = input("Enter the city to search:")

webUrl = 'https://www.monster.com/jobs/search/?q=Computer-Science&where=' + location
content = requests.get(webUrl)
print(webUrl)

