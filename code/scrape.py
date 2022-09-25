import requests
import urllib.request
from bs4 import BeautifulSoup
url = 'https://www.flipkart.com/mi-a1-gold-64-gb/product-reviews/itmexnsr2cwzbfht?pid=MOBEX9WXZCZHWXUZ'
re=urllib.request.urlopen(url)
soup=BeautifulSoup(re)
print(soup)