#FBS Stats Scraper
#Version 1.1


#Fixed URL list for stat sourcing
#Iterates over table defined by class
#Appends data to list, stats
#Added arg to check_page func to allow use in multiple locations
#Added check_page to team names section


#ToDo
#Write to CSV
#Parse individual stat numbers..? i.e. penalties, yards in different cells
#Add iterator to scrape URL from CFBstats.com index for each team


import requests
from bs4 import BeautifulSoup
#import time
#import csv


def check_page(loc):
	loc.status_code # loc is the callable object requests module creates, i.e. index_page_soup
	if loc.status_code == 200:
		print()
	if loc.status_code != 200:
		print('Page Connection Error')


team_full_urls = ['http://cfbstats.com/2019/team/140/index.html', 'http://cfbstats.com/2019/team/164/index.html', 'http://cfbstats.com/2019/team/196/index.html', 'http://cfbstats.com/2019/team/288/index.html', 'http://cfbstats.com/2019/team/404/index.html', 'http://cfbstats.com/2019/team/726/index.html', 'http://cfbstats.com/2019/team/651/index.html', 'http://cfbstats.com/2019/team/663/index.html', 'http://cfbstats.com/2019/team/690/index.html', 'http://cfbstats.com/2019/team/718/index.html', 'http://cfbstats.com/2019/team/719/index.html', 'http://cfbstats.com/2019/team/128/index.html', 'http://cfbstats.com/2019/team/67/index.html', 'http://cfbstats.com/2019/team/147/index.html', 'http://cfbstats.com/2019/team/193/index.html', 'http://cfbstats.com/2019/team/234/index.html', 'http://cfbstats.com/2019/team/255/index.html', 'http://cfbstats.com/2019/team/367/index.html', 'http://cfbstats.com/2019/team/415/index.html', 'http://cfbstats.com/2019/team/457/index.html', 'http://cfbstats.com/2019/team/490/index.html', 'http://cfbstats.com/2019/team/545/index.html', 'http://cfbstats.com/2019/team/688/index.html', 'http://cfbstats.com/2019/team/746/index.html', 'http://cfbstats.com/2019/team/742/index.html', 'http://cfbstats.com/2019/team/749/index.html', 'http://cfbstats.com/2019/team/51/index.html', 'http://cfbstats.com/2019/team/311/index.html', 'http://cfbstats.com/2019/team/328/index.html', 'http://cfbstats.com/2019/team/327/index.html', 'http://cfbstats.com/2019/team/522/index.html', 'http://cfbstats.com/2019/team/521/index.html', 'http://cfbstats.com/2019/team/698/index.html', 'http://cfbstats.com/2019/team/703/index.html', 'http://cfbstats.com/2019/team/700/index.html', 'http://cfbstats.com/2019/team/768/index.html', 'http://cfbstats.com/2019/team/301/index.html', 'http://cfbstats.com/2019/team/306/index.html', 'http://cfbstats.com/2019/team/312/index.html', 'http://cfbstats.com/2019/team/392/index.html', 'http://cfbstats.com/2019/team/418/index.html', 'http://cfbstats.com/2019/team/416/index.html', 'http://cfbstats.com/2019/team/428/index.html', 'http://cfbstats.com/2019/team/463/index.html', 'http://cfbstats.com/2019/team/509/index.html', 'http://cfbstats.com/2019/team/518/index.html', 'http://cfbstats.com/2019/team/539/index.html', 'http://cfbstats.com/2019/team/559/index.html', 'http://cfbstats.com/2019/team/587/index.html', 'http://cfbstats.com/2019/team/796/index.html', 'http://cfbstats.com/2019/team/458/index.html', 'http://cfbstats.com/2019/team/229/index.html', 'http://cfbstats.com/2019/team/231/index.html', 'http://cfbstats.com/2019/team/366/index.html', 'http://cfbstats.com/2019/team/388/index.html', 'http://cfbstats.com/2019/team/419/index.html', 'http://cfbstats.com/2019/team/497/index.html', 'http://cfbstats.com/2019/team/523/index.html', 'http://cfbstats.com/2019/team/574/index.html', 'http://cfbstats.com/2019/team/664/index.html', 'http://cfbstats.com/2019/team/9/index.html', 'http://cfbstats.com/2019/team/704/index.html', 'http://cfbstats.com/2019/team/706/index.html', 'http://cfbstats.com/2019/team/772/index.html', 'http://cfbstats.com/2019/team/725/index.html', 'http://cfbstats.com/2019/team/77/index.html', 'http://cfbstats.com/2019/team/355/index.html', 'http://cfbstats.com/2019/team/400/index.html', 'http://cfbstats.com/2019/team/472/index.html', 'http://cfbstats.com/2019/team/513/index.html', 'http://cfbstats.com/2019/team/5/index.html', 'http://cfbstats.com/2019/team/47/index.html', 'http://cfbstats.com/2019/team/71/index.html', 'http://cfbstats.com/2019/team/86/index.html', 'http://cfbstats.com/2019/team/129/index.html', 'http://cfbstats.com/2019/team/204/index.html', 'http://cfbstats.com/2019/team/331/index.html', 'http://cfbstats.com/2019/team/414/index.html', 'http://cfbstats.com/2019/team/503/index.html', 'http://cfbstats.com/2019/team/519/index.html', 'http://cfbstats.com/2019/team/709/index.html', 'http://cfbstats.com/2019/team/774/index.html', 'http://cfbstats.com/2019/team/721/index.html', 'http://cfbstats.com/2019/team/66/index.html', 'http://cfbstats.com/2019/team/156/index.html', 'http://cfbstats.com/2019/team/96/index.html', 'http://cfbstats.com/2019/team/277/index.html', 'http://cfbstats.com/2019/team/466/index.html', 'http://cfbstats.com/2019/team/473/index.html', 'http://cfbstats.com/2019/team/626/index.html', 'http://cfbstats.com/2019/team/630/index.html', 'http://cfbstats.com/2019/team/465/index.html', 'http://cfbstats.com/2019/team/731/index.html', 'http://cfbstats.com/2019/team/811/index.html', 'http://cfbstats.com/2019/team/29/index.html', 'http://cfbstats.com/2019/team/28/index.html', 'http://cfbstats.com/2019/team/107/index.html', 'http://cfbstats.com/2019/team/157/index.html', 'http://cfbstats.com/2019/team/529/index.html', 'http://cfbstats.com/2019/team/528/index.html', 'http://cfbstats.com/2019/team/657/index.html', 'http://cfbstats.com/2019/team/674/index.html', 'http://cfbstats.com/2019/team/110/index.html', 'http://cfbstats.com/2019/team/732/index.html', 'http://cfbstats.com/2019/team/756/index.html', 'http://cfbstats.com/2019/team/754/index.html', 'http://cfbstats.com/2019/team/8/index.html', 'http://cfbstats.com/2019/team/31/index.html', 'http://cfbstats.com/2019/team/37/index.html', 'http://cfbstats.com/2019/team/235/index.html', 'http://cfbstats.com/2019/team/257/index.html', 'http://cfbstats.com/2019/team/334/index.html', 'http://cfbstats.com/2019/team/365/index.html', 'http://cfbstats.com/2019/team/433/index.html', 'http://cfbstats.com/2019/team/430/index.html', 'http://cfbstats.com/2019/team/434/index.html', 'http://cfbstats.com/2019/team/648/index.html', 'http://cfbstats.com/2019/team/694/index.html', 'http://cfbstats.com/2019/team/697/index.html', 'http://cfbstats.com/2019/team/736/index.html', 'http://cfbstats.com/2019/team/27/index.html', 'http://cfbstats.com/2019/team/30/index.html', 'http://cfbstats.com/2019/team/149/index.html', 'http://cfbstats.com/2019/team/253/index.html', 'http://cfbstats.com/2019/team/254/index.html', 'http://cfbstats.com/2019/team/671/index.html', 'http://cfbstats.com/2019/team/498/index.html', 'http://cfbstats.com/2019/team/646/index.html', 'http://cfbstats.com/2019/team/670/index.html', 'http://cfbstats.com/2019/team/716/index.html']


stats = []
teams = []
team_names = []


#team names only, prints team names to a list
index_url = "http://cfbstats.com/2019/team/index.html"
index_page = requests.get(index_url)
team_index_soup = BeautifulSoup(index_page.content, 'html.parser')
check_page(index_page)
conference_list = team_index_soup.find_all('div',class_='conference')
for conference in conference_list:
	conference_team_list = conference.find_all('li')
	for conference_team_list_item in conference_team_list:
		team_name = conference_team_list_item.text
		team_names.append(team_name)


#iterates over team pages to pull and print stats for each team
for i in range(len(team_full_urls)):
	url = team_full_urls[i]
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	check_page(page)
#	print(soup)
	table = soup.find_all('table', class_="team-statistics")
	print(team_names[i])
	for r in table:
		rows = r.find_all('tr')
		for c in rows:
			cells = c.find_all('td')
			for y in cells[0:2]:
				cell = y.get_text()
				print(cell)
				stats.append(cell)


#print (team_names)
#print(stats)