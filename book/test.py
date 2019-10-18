from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html,"html.parser")
namelist = soup.findAll("span",{"class":"green"})
for name in namelist:
    print(name.text)