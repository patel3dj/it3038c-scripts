import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r,"lxml")
tags = soup.findALL("div", {"class":re.compile('(ratings)')})
for div in tags:
    
    a = div.findALL("p",{"class":"pull-right"}))
    print(type(a[0].string))
    



#tags = soup.find_all("a",{"href":re.compile('(allinone')})


#for a in tags:
 #   print(a.get('href'))
