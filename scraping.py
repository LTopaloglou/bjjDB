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
create_athl_list = ("CREATE TABLE athletes("
                      "id int PRIMARY KEY,"
                      "First_Name text,"
                      "Last_Name text,"
                      "Nickname text,"
                      "Team text)")

create_match_record = ("CREATE TABLE $("
                       "Opponent text,"
                       "Outcome text,"
                       "Method text,"
                       "Event text,"
                       "Division text,"
                       "Stage text,"
                       "Year int)")


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

    #Now scrape the athlete's page using link
    athPage = requests.get(link)
    athSoup = BeautifulSoup(athPage.content, "html.parser")
    record = athSoup.find(class_="fighter_info_plug")
    #some athlete pages do not have a record so this if statement is required
    if record is not None:
        wins = record.find(class_="Win_title").find("em").string
        loss = record.find(class_="Win_title_lose").find("em").string
        wins = wins.replace("WINS", "")
        loss = loss.replace("LOSSES", "")
        #iterate through record here
        history = athSoup.find("tbody").find_all("tr")
        for match in history:
            #print(match.prettify())
            tds = match.find_all("td")
            if tds is not None:
                #for td in tds:
                #    print(td.string)
                print(tds[1])
                opponent = tds[1].find("span").string
                outcome = tds[2].string
                method = tds[3].string
                event = tds[4].string
                weight = tds[5].string
                stage = tds[6].string
                year = tds[7].string
                print(opponent)
                print(outcome)
                print(method)
                print(event)
                print(weight)
                print(stage)
                print(year)
            print()
        
    else:
        wins = "0"
        loss = "0"
        subs = "0"
    totalMatches = int(wins) + int(loss)
    print(wins)
    print(loss)
    if totalMatches > 0:    
        winrate = int(wins)/totalMatches * 100
    else:
        winrate = 0;
    print(int(winrate))


    #now get next athlete
    print()
    row += 1
    rowData = results.find(class_="row-"+str(row))
