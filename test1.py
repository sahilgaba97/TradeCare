import selenium
import time
from selenium import webdriver
from time import sleep
import bs4
import _mysql
import sys

from bs4 import BeautifulSoup
def main():
	try:
    	con = _mysql.connect('localhost', 'test','tes','scraper')
        
    	con.query("SELECT * from spec")
    	result = con.use_result()
    
   		print ("MySQL version: %s" %result.fetch_row()[0])
    
	except (_mysql.Error, e):
  
    	print ("Error %d: %s" % (e.args[0], e.args[1]))
    	sys.exit(1)


	print("a")
	url2="https://www.amazon.in/Apple-MacBook-Air-13-3-inch-Integrated/dp/B073Q5R6VR/ref=sr_1_2?s=computers&ie=UTF8&qid=1512392575&sr=1-2&keywords=laptop"
	driver = webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
	driver.get(url2)
	link=driver.find_element_by_xpath("//*[@id='seeMoreDetailsLink']").click()    	
	time.sleep(2)
	tr=driver.find_elements_by_xpath('//*[@id="prodDetails"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr')
	i=1;
	#get prooduct no from here
	try:
		con = _mysql.connect('localhost', 'test','tes','scraper')
    	with con:
    		cur=con.cursor()
    		cur.execute("insert into table product(pname) values('"+pname+"')")
    	con.query("SELECT max(pno) from product") 
    	result = con.use_result()
  		print ("MySQL version: %s" %result.fetch_row()[0])
    
	except (_mysql.Error, e):  
    	print ("Error %d: %s" % (e.args[0], e.args[1]))
    	sys.exit(1)

	for se in tr:
		sr=driver.find_element_by_xpath('//*[@id="prodDetails"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr['+str(i)+']/td[1]')
		s=sr.text	
		sr1=driver.find_element_by_xpath('//*[@id="prodDetails"]/div/div[1]/div[1]/div[2]/div/div/table/tbody/tr['+str(i)+']/td[2]')
		s1=sr1.text	
		i=i+1;
		try:
			con = _mysql.connect('localhost', 'test','tes','scraper')
        	with con:
        		cur = con.cursor()
    			cur.execute("insert into table spec values();")	
			
if __name__ == "__main__": main()