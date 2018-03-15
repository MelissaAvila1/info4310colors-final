import requests
import csv
import time 

from BeautifulSoup import BeautifulSoup
from selenium import webdriver


list_of_rows = []
intID = 0
# while intID < 100000:
site_arr = []

with open('rawsites.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		site_arr.append(row[0])

while intID < len(site_arr):
	webpage = r"https://webcolourdata.com//" # edit me
	searchterm = site_arr[intID] # edit me

	chromedriver = "/Users/melissa/Scrape/chromedriver"
	driver = webdriver.Chrome(chromedriver)
	driver.get(webpage)

	sbox = driver.find_element_by_name("url")
	sbox.send_keys(searchterm)

	submit = driver.find_element_by_class_name("accent-bg")
	submit.click()

	time.sleep(5)
	print intID
	url =  str(driver.current_url)
	driver.quit()
	list_of_cells = []
	list_of_cells.append(url)
	list_of_rows.append(list_of_cells)
	intID = intID + 1

outfile = open("./sites.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)
