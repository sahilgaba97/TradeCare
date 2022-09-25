import selenium
import time
from selenium import webdriver
from time import sleep
import sqlite3
import sys
import bs4
from bs4 import BeautifulSoup
import io

def main():
	url="https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=moto"
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.get(url)
	print("\nOpening Amazon....")
	time.sleep(1)
	#link=driver.find_elements_by_xpath('//*[@id="result_0"]/div[1]/div[3]/div[1]/a')
	image=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[2]/div[1]/div[1]/a[1]/img')
	tex=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[3]/div[1]/a[1]/h2')
	for lin in image:
		print(str(lin.get_attribute('src')));
	for te in tex:
		print(str(te.text))
		

if __name__ == "__main__": main()