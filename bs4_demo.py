from bs4 import BeautifulSoup
import urllib.request


local_filename, headers = urllib.request.urlretrieve('http://www.kbb.com/')
html = open(local_filename)

soup = BeautifulSoup(html, "html.parser")

# print(soup.prettify())

scripts = soup("script")
for script in scripts:
	if("'currentview': 'home'" in script.text):
		print(script)
	
print(len(scripts))	
# links = soup.find_all('a')

# for link in links:
    # print(link.get('href'))
	
# print(len(links))