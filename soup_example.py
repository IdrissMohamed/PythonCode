from bs4 import BeautifulSoup
import urllib

url = "https://en.wikipedia.org/wiki/Super_Mario"

page = urllib.urlopen(url)

data = str(page.readlines())

soup = BeautifulSoup(data)

# Prints out the content of an anchor tag followed by it's href
for link in soup.find_all('a'):
    print(str(link.contents) + " => " + str(link.get('href')))
    
# Prints out the total number of divs on the page
print("The page contains " + str(len(soup.find_all('div'))) + " divs")
