# -*- coding: utf-8 -*-
"""FBS_Scraper.py

FBS Scraper Tool
 Version 1.1

 Introduction
This tool uses BeautifulSoup4 to scrape CFBstats.com to obtain NCAA Div. Ia football statistics.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd


class Scraper:

  def check_page(loc):
    try:
      loc.status_code # loc is the callable object requests module creates, i.e. index_page_soup
      if loc.status_code == 200:
        #print('Connected')
        pass
      if loc.status_code != 200:
        print('Page Connection Error')
    except:
      print('An error occured while attempting to connect to the website. ')
  
  def soup_recipe(address):
    url = address
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    Scraper.check_page(page)
    return soup


team_full_urls = ['http://cfbstats.com/2019/team/140/index.html', 'http://cfbstats.com/2019/team/164/index.html', 'http://cfbstats.com/2019/team/196/index.html', 'http://cfbstats.com/2019/team/288/index.html', 'http://cfbstats.com/2019/team/404/index.html', 'http://cfbstats.com/2019/team/726/index.html', 'http://cfbstats.com/2019/team/651/index.html', 'http://cfbstats.com/2019/team/663/index.html', 'http://cfbstats.com/2019/team/690/index.html', 'http://cfbstats.com/2019/team/718/index.html', 'http://cfbstats.com/2019/team/719/index.html', 'http://cfbstats.com/2019/team/128/index.html', 'http://cfbstats.com/2019/team/67/index.html', 'http://cfbstats.com/2019/team/147/index.html', 'http://cfbstats.com/2019/team/193/index.html', 'http://cfbstats.com/2019/team/234/index.html', 'http://cfbstats.com/2019/team/255/index.html', 'http://cfbstats.com/2019/team/367/index.html', 'http://cfbstats.com/2019/team/415/index.html', 'http://cfbstats.com/2019/team/457/index.html', 'http://cfbstats.com/2019/team/490/index.html', 'http://cfbstats.com/2019/team/545/index.html', 'http://cfbstats.com/2019/team/688/index.html', 'http://cfbstats.com/2019/team/746/index.html', 'http://cfbstats.com/2019/team/742/index.html', 'http://cfbstats.com/2019/team/749/index.html', 'http://cfbstats.com/2019/team/51/index.html', 'http://cfbstats.com/2019/team/311/index.html', 'http://cfbstats.com/2019/team/328/index.html', 'http://cfbstats.com/2019/team/327/index.html', 'http://cfbstats.com/2019/team/522/index.html', 'http://cfbstats.com/2019/team/521/index.html', 'http://cfbstats.com/2019/team/698/index.html', 'http://cfbstats.com/2019/team/703/index.html', 'http://cfbstats.com/2019/team/700/index.html', 'http://cfbstats.com/2019/team/768/index.html', 'http://cfbstats.com/2019/team/301/index.html', 'http://cfbstats.com/2019/team/306/index.html', 'http://cfbstats.com/2019/team/312/index.html', 'http://cfbstats.com/2019/team/392/index.html', 'http://cfbstats.com/2019/team/418/index.html', 'http://cfbstats.com/2019/team/416/index.html', 'http://cfbstats.com/2019/team/428/index.html', 'http://cfbstats.com/2019/team/463/index.html', 'http://cfbstats.com/2019/team/509/index.html', 'http://cfbstats.com/2019/team/518/index.html', 'http://cfbstats.com/2019/team/539/index.html', 'http://cfbstats.com/2019/team/559/index.html', 'http://cfbstats.com/2019/team/587/index.html', 'http://cfbstats.com/2019/team/796/index.html', 'http://cfbstats.com/2019/team/458/index.html', 'http://cfbstats.com/2019/team/229/index.html', 'http://cfbstats.com/2019/team/231/index.html', 'http://cfbstats.com/2019/team/366/index.html', 'http://cfbstats.com/2019/team/388/index.html', 'http://cfbstats.com/2019/team/419/index.html', 'http://cfbstats.com/2019/team/497/index.html', 'http://cfbstats.com/2019/team/523/index.html', 'http://cfbstats.com/2019/team/574/index.html', 'http://cfbstats.com/2019/team/664/index.html', 'http://cfbstats.com/2019/team/9/index.html', 'http://cfbstats.com/2019/team/704/index.html', 'http://cfbstats.com/2019/team/706/index.html', 'http://cfbstats.com/2019/team/772/index.html', 'http://cfbstats.com/2019/team/725/index.html', 'http://cfbstats.com/2019/team/77/index.html', 'http://cfbstats.com/2019/team/355/index.html', 'http://cfbstats.com/2019/team/400/index.html', 'http://cfbstats.com/2019/team/472/index.html', 'http://cfbstats.com/2019/team/513/index.html', 'http://cfbstats.com/2019/team/5/index.html', 'http://cfbstats.com/2019/team/47/index.html', 'http://cfbstats.com/2019/team/71/index.html', 'http://cfbstats.com/2019/team/86/index.html', 'http://cfbstats.com/2019/team/129/index.html', 'http://cfbstats.com/2019/team/204/index.html', 'http://cfbstats.com/2019/team/331/index.html', 'http://cfbstats.com/2019/team/414/index.html', 'http://cfbstats.com/2019/team/503/index.html', 'http://cfbstats.com/2019/team/519/index.html', 'http://cfbstats.com/2019/team/709/index.html', 'http://cfbstats.com/2019/team/774/index.html', 'http://cfbstats.com/2019/team/721/index.html', 'http://cfbstats.com/2019/team/66/index.html', 'http://cfbstats.com/2019/team/156/index.html', 'http://cfbstats.com/2019/team/96/index.html', 'http://cfbstats.com/2019/team/277/index.html', 'http://cfbstats.com/2019/team/466/index.html', 'http://cfbstats.com/2019/team/473/index.html', 'http://cfbstats.com/2019/team/626/index.html', 'http://cfbstats.com/2019/team/630/index.html', 'http://cfbstats.com/2019/team/465/index.html', 'http://cfbstats.com/2019/team/731/index.html', 'http://cfbstats.com/2019/team/811/index.html', 'http://cfbstats.com/2019/team/29/index.html', 'http://cfbstats.com/2019/team/28/index.html', 'http://cfbstats.com/2019/team/107/index.html', 'http://cfbstats.com/2019/team/157/index.html', 'http://cfbstats.com/2019/team/529/index.html', 'http://cfbstats.com/2019/team/528/index.html', 'http://cfbstats.com/2019/team/657/index.html', 'http://cfbstats.com/2019/team/674/index.html', 'http://cfbstats.com/2019/team/110/index.html', 'http://cfbstats.com/2019/team/732/index.html', 'http://cfbstats.com/2019/team/756/index.html', 'http://cfbstats.com/2019/team/754/index.html', 'http://cfbstats.com/2019/team/8/index.html', 'http://cfbstats.com/2019/team/31/index.html', 'http://cfbstats.com/2019/team/37/index.html', 'http://cfbstats.com/2019/team/235/index.html', 'http://cfbstats.com/2019/team/257/index.html', 'http://cfbstats.com/2019/team/334/index.html', 'http://cfbstats.com/2019/team/365/index.html', 'http://cfbstats.com/2019/team/433/index.html', 'http://cfbstats.com/2019/team/430/index.html', 'http://cfbstats.com/2019/team/434/index.html', 'http://cfbstats.com/2019/team/648/index.html', 'http://cfbstats.com/2019/team/694/index.html', 'http://cfbstats.com/2019/team/697/index.html', 'http://cfbstats.com/2019/team/736/index.html', 'http://cfbstats.com/2019/team/27/index.html', 'http://cfbstats.com/2019/team/30/index.html', 'http://cfbstats.com/2019/team/149/index.html', 'http://cfbstats.com/2019/team/253/index.html', 'http://cfbstats.com/2019/team/254/index.html', 'http://cfbstats.com/2019/team/671/index.html', 'http://cfbstats.com/2019/team/498/index.html', 'http://cfbstats.com/2019/team/646/index.html', 'http://cfbstats.com/2019/team/670/index.html', 'http://cfbstats.com/2019/team/716/index.html']


stats = []
teams = []
team_names = []


#team names only, prints team names to a list
team_index_soup = Scraper.soup_recipe('http://cfbstats.com/2019/team/index.html')
conference_list = team_index_soup.find_all('div',class_='conference')
for conference in conference_list:
	conference_team_list = conference.find_all('li')
	for conference_team_list_item in conference_team_list:
		team_name = conference_team_list_item.text
		team_names.append(team_name)


#iterates over team pages to pull and print stats for each team
for i in range(len(team_full_urls)):
  soup_stuff = Scraper.soup_recipe(team_full_urls[i])
#	print(soup)
  table = soup_stuff.find_all('table', class_="team-statistics")
	#print(team_names[i])
  for r in table:
    rows = r.find_all('tr')
    for c in rows:
      cells = c.find_all('td')
      for y in cells[0:2]:
        cell = y.get_text()
        split_cell = cell.split('-')
        w = 0
        for x in split_cell:
          stats.append(split_cell[w])
          w += 1

        #print(cell)
        #stats.append(split_cell)

t= 0 
p = 0
q= 66


list_of_lists = []
for i in team_names:
  c = 0
  list_for_df = []
  list_for_df.append(team_names[t]) # Appends to list
  for v in stats[p:q]:
    list_for_df.append(stats[c])
    c += 1
  list_of_lists.append(list_for_df)
  t += 1
  p += 66
  q += 66



df = pd.DataFrame(list_of_lists)
df.drop(columns=[1, 3, 4, 7, 9, 10, 11, 15, 17, 18, 19, 23, 25, 27, 28, 29, 35, 37, 38, 41, 43, 44, 45, 49, 51, 52, 53, 57, 59, 60, 63, 64, 65], axis=1, inplace=True)
df.columns = ['Team', 'Scoring: Pts/Game', 'Scoring: Games', 'Scoring: Points','First Downs: Total', 'First Downs: Rushing', 'First Downs: Passing', 'First Downs: By Penalty', 'Rushing Yards/Attempt', 'Rushing: Attempts', 'Rushing: Yards', 'Rushing: TDs', 'Passing: Rating', 'Passing: Yards', 'Passing: Attempts', 'Passing: Completions', 'Passing: Interceptions', 'Passing: TDs', 'Total Offense:  Yrds/Play', 'Punt Returns: Yards/Return', ' Punt Returns: Returns', 'Punt Returns: Yards', 'Punt Returns: TDs', 'Kickoff Returns: Yards/Return', 'Kickoff Returns: Returns', 'Kickoff Returns: Yards', 'Kickoff Returns: TDs', 'Kickoff Returns:', 'Punting: Yards/Punt', 'Punting: Punts', 'Punting: Yards', 'Interceptions: Returns', 'Interceptions: Yards', 'Interceptions: TDs']


csv_string = df.to_csv()

f = open("FBSstats.csv", "w")
f.write(csv_string)
f.close()

#@title Download File
from google.colab import files

files.download('FBSstats.csv')
