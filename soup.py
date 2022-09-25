from selenium import webdriver
from time import sleep
import sqlite3
import sys
import bs4
from bs4 import BeautifulSoup

soup=BeautifulSoup(open('C:\Project\Html\index.html'),'html.parser')
i=0;
while i<10:
	soup.find(id="a"+str(i)).string.replaceWith("Text")
	soup.find(id="i"+str(i)).string.replaceWith("Text")
	i=i+1;
with open('C:\Project\Html\index.html', "w") as file:
    file.write(str(soup))
		