import requests
from bs4 import BeautifulSoup

#this file is for webscraping data

url = 'https://www.bjjheroes.com/a-z-bjj-fighters-list'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="tablepress-104")

firstNames = results.find_all("td", class_="column-1")
lastNames = results.find_all("td", class_="column-2")
nickNames = results.find_all("td", class_="column-3")
teams = results.find_all("td", class_="column-4")

for firstName in firstNames:
    print(firstName.find("a").string)