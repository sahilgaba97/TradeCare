import selenium
import time
from selenium import webdriver
from time import sleep
def ama():
	nodes=driver.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/span[contains(@class,'a-size-base review-text')]")
	#div[contains(@class,'row')]
	print(str(len(nodes)))
	for head in nodes:
		aas=head.text
		print(aas+"\n")

#url='https://www.amazon.in/Logitech-G102-Optical-Gaming-Mouse/dp/B01MYPU20Z/ref=sr_1_1?ie=UTF8&qid=1507185650&sr=8-1&keywords=logitech+g102'
#url='https://www.amazon.in/Logitech-G102-Optical-Gaming-Mouse/product-reviews/B01MYPU20Z/ref=dpx_acr_txt?showViewpoints=1'
url='https://www.amazon.in/Captcha-Screen-Bluetooth-SAMSUNG-assorted/product-reviews/B01NAK3RZM/ref=dpx_acr_txt?showViewpoints=1'
driver = webdriver.Chrome('c:/chrome_driver/chromedriver.exe')
driver.get(url)
#do=driver.find_element_by_id('acrCustomerReviewLink').get_attribute('href')
#driver.get(do)
ama()
c=1
while c:
	try:
		nex=driver.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/span/div/ul/li[contains(@class,'a-last')]/a").click()
		time.sleep(2)		
		ama()
	except:
		c=0
		break	