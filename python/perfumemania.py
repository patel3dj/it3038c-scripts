import requests, re 
from bs4 import BeautifulSoup 
 
data  = requests.get("https://www.microcenter.com/product/626571/acer-nitro-xv272u-vb").content  
soup = BeautifulSoup(data, 'html.parser')  
details = soup.find("h1")
print(details)