tables = soup.findAll('table') #Retreives only HTML tables.
page.content # Retrieves *everything.*
links = soup.find_all('a') #Finds all 'a' tags.
data_tr = soup.find_all('tr') #Finds all rows inside an html table.
data_th = soup.find_all('th') #Finds all html table headers.
Data_td = soup.find_all('td') #Finds all data inside an html table.
html_page = soup.prettify() 
print(html_page) #Prints HTML source code.

Strip HTML tags from data
soup = BeautifulSoup(html_page)
clear_text = (soup.get_text()) 
print(clear_text)
or via attribute of Soup Object: print(soup.text)
