from tkinter import N
import queries
import requests
from bs4 import BeautifulSoup

#this file is for webscraping data

url = 'https://www.bjjheroes.com/a-z-bjj-fighters-list'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="tablepress-104")

#SQL queries
connection = queries.create_database_connection("localhost", "root", queries.pw, "bjj")
#this query creates the athletes table with all the columns.
create_table_query = ("CREATE TABLE athletes("
                      "id int PRIMARY KEY,"
                      "First_Name text,"
                      "Last_Name text,"
                      "Nickname text,"
                      "Team text)")


row = 2
rowData = results.find(class_="row-"+str(row))
print(rowData)
while rowData is not None:
    print("row-"+str(row))
    firstName = rowData.find(class_="column-1").find("a").string
    print(firstName)
    lastName = rowData.find(class_="column-2").find("a").string
    print(lastName)
    nickName = rowData.find(class_="column-3")
    if nickName is not None:
        print(nickName.string)
    else:
        print("ERROR: EMPTY DATA")
    team = rowData.find(class_="column-4")
    if team is not None:
        print(team.string)
    else:
        print("ERROR: EMPTY DATA")
    link = "https://www.bjjheroes.com" + rowData.find(class_="column-1").find("a")['href']
    print(link)
    print()
    row += 1
    rowData = results.find(class_="row-"+str(row))