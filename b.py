import selenium
import time
from selenium import webdriver
from time import sleep
import sqlite3

def flip():
	heads=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/p")
	desc=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div[contains(@class,'row')]/div/div/div")
	cli=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/span/span")
	for cll in cli:
		try:
			cll.click()
		except:
			pass	
	i=0
	for head in heads:
		aas=head.text
		while desc[i].text.isdigit():
			i=i+2
			print("skipping"+str(i))
		bas=desc[i].text
		print(aas+":"+bas+"\n")
		i=i+1

con=sqlite3.connect("scrape.db")
url='https://www.flipkart.com/'
query='mi a1'
driver = webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
driver.get(url)
time.sleep(2)
sbox=driver.find_element_by_name("q")
sbox.send_keys(query)
sub=driver.find_element_by_class_name("vh79eN").click()
time.sleep(2)
link=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/a").click()    
time.sleep(2)
link2=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/a").click()
time.sleep(2)
flip()
c=1
while c:
	try:
		nex1=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/a/span")
		i1=len(nex1)
		print(str(i1))
		for nex in nex1:
			n1=nex.text
			n1.strip()
			if "NEXT" in n1:
				print(n1)
				nex.click()
				time.sleep(5)
				flip()
				time.sleep(2)
			else:
				i1=i1-1		
			if i1==0:
				c=0
				break		
	except:
		break

#heads=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/p")
#desc=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div[contains(@class,'row')]/div/div/div")
#i=0
#for head in heads:
#	while desc[i].text.isdigit():
#		i=i+1
#		print("skipping"+i)
#	bas=desc[i].text
#	print(aas+":"+bas+"\n")
#	i=i+1
