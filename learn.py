#USE BS4 ON "https://www.sciencedirect.com/search?qs=" qs -> keyword or google lmao
#re.compile("^http://")
import webbrowser as wb
from bs4 import BeautifulSoup
from urllib.parse import urlparse
#import pyshorteners
import requests
#mport re


URL = "https://www.google.com/search?q="
#type_tiny = pyshorteners.Shortener()

while True:

	keyword = input("Enter the keyword: ").replace(" ", "+")
	URL += keyword
	page = requests.get(URL).text

	soup = BeautifulSoup(page, 'lxml')
	url_lst = []

	i = 0
	for link in soup.findAll('a'):
		if i == 5:
			break
		if "www" and "https" in link.get('href'):
			#tiny = type_tiny.tinyurl.short(link.get('href'))
			parts = urlparse(link.get('href'))
			query = parts.query.split('&')
			if query[0][-3:] != "jpg":
				#print(query[0])
				try:
					idx = query[0].index('h')
					url_lst.append(query[0][idx:])
				#print(tiny)
					i += 1
				except ValueError:
					if "https" in query[0]:
						url_lst.append(query[0])
						i += 1
					else:
						pass

	print(url_lst)
	f = open('test.txt', 'w')
	choice = input("Do you want to open the link? [add index]: ").lower()
	inputs = choice.split(" ")
	if inputs[0] == "n":
		pass
	if inputs[0] == "y":
		#link_idx = int(input("Which link do you want to open: "))
		open_link = wb.open(url_lst[int(inputs[1])])

	#geeks = requests.get(first_link).text
	#soup_ = BeautifulSoup(geeks, 'lxml')
	#for i in soup_.findAll('p'):
	#	print(i.text)
	#	#f.write(i.text)

	#for url in url_lst:
		#page_ = requests.get(url).text
		#sub_soup = BeautifulSoup(page, 'lxml')
		#for p in sub_soup.findAll('p'):
		#	print(p.text)
