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
	query=str(sys.argv[1])
	url="http://www.amazon.in"
	print(str(sys.argv[1]))
	driver=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.get(url)
	print("\nOpening Amazon....")
	time.sleep(1)
	sbox=driver.find_element_by_id('twotabsearchtextbox')
	sbox.send_keys(query)
	print("\nEntering Queries....")
	go=driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input').click()
	time.sleep(2)
	#link=driver.find_elements_by_xpath('//*[@id="result_0"]/div[1]/div[3]/div[1]/a')
	link=driver.find_elements_by_xpath('//li[contains(@id,"result_")]/div[1]/div[3]/div[1]/a')
	for lin in link:
		lin
		print(str(lin.get_attribute('href')));

if __name__ == "__main__": main()