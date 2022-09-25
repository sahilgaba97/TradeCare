import selenium
import time
from selenium import webdriver
from time import sleep
import sqlite3
import sys
import bs4
from bs4 import BeautifulSoup
import io

def flip(driver,soup):
	heads=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/p")
	desc=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div[contains(@class,'row')]/div/div/div")
	cli=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span")
	for cll in cli:
		try:
			cll.click()
		except:
			pass	
	i=0
	i1=0
	c="i"
	bas="ss"
	for head in heads:
		aas=head.text
		while desc[i].text.isdigit():
			i=i+2
			print("skipping"+str(i))
		bas=desc[i].text
		bas = bas.encode('ascii', 'replace')
		#print(aas+":"+bas+"\n")
		soup.find(id=c+str(i1)).string.replaceWith(str(bas))
		i=i+1
		i1=i1+1


def ama(driver,soup):
	nodes=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/span[contains(@class,'a-size-base review-text')]")
	#div[contains(@class,'row')]
	print(str(len(nodes)))
	i=0
	c="a"
	aas="a"
	for head in nodes:
		aas=head.text
		soup.find(id=c+str(i)).string.replaceWith(str(aas))
		i=i+1
		print(aas+"\n")

		
def main():
	soup=BeautifulSoup(open('C:\Project\Html\index.html'),'html.parser')
	query=str(sys.argv[1])
	
	
	print("\nOpening WebDriver....")
	url="http://www.amazon.in"
#	query=str(sys.argv[1])
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
	link=driver.find_element_by_xpath('/html/body/div/div/div/div/div/div/div/div/div/ul/li/div/div/div/div/div/div/a').get_attribute('href')
	driver.get(link)
	time.sleep(2)
	do=driver.find_element_by_id('acrCustomerReviewLink').get_attribute('href')
	print("\nSelecting appropriate link....")
	driver.quit()
	driver1=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver1.get(do)
	time.sleep(2)
	ama(driver1,soup)
	driver1.quit()
	

	url2='https://www.flipkart.com/'
	driver = webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	print("\nOpening Flipkart....")
	driver.get(url2)
	time.sleep(3)
	sbox=driver.find_element_by_name("q")
	print("\nEntering Queries....")
	try:
		s1=driver.find_element_by_class_name("_2AkmmA _28YdH8")
		s1.send_keys("")
	except:
		print("exception: no cross detected")
	sbox.send_keys(query)
	sub=driver.find_element_by_class_name("vh79eN").click()
	time.sleep(2)
	print("\nSelecting link....")
	link=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/a").get_attribute('href')    	
	driver.quit()
	driver1=webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver1.get(link)
	time.sleep(2)
	link2=driver1.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div/div[1]/div/div[2]/div[12]/a").click()    	
	time.sleep(1)
#	link=driver1.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/a").click()    
#	time.sleep(2)
#	link2=driver.find_element_by_xpath("//*[@id='container']/div/div[1]/div/div/div/div[1]/div/div[2]/div[12]/a").get_attribuet('href')
#	time.sleep(2)
	flip(driver1,soup)

	with open('C:\Project\Html\index.html', "w", encoding='utf-8') as file:
  		file.write(str(soup))
    
    #c=1
	#while c:
	#		nex=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/span/div/ul/li[contains(@class,'a-last')]/a").click()
	#		time.sleep(2)		
	#		ama()
	#	except:
	#		c=0
	#		break			

if __name__ == "__main__": main()	
