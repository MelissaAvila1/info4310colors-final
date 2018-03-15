import requests
import csv
import time 

from BeautifulSoup import BeautifulSoup
from selenium import webdriver


list_of_rows = []
intID = 0
# while intID < 100000:
site_arr = ["google.com", "bbc.com"]




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
	driver.switch_to_window(driver.window_handles[-1])


	url =  str(driver.current_url)
	driver.quit()
	
	response = requests.get(url)
		

	
	html = response.content


	soup = BeautifulSoup(html)
	if soup.find("section", attrs={'class': 'info'}):
		section = soup.find("section", attrs={'class': 'info'})
		if section.find("h1").text:
			website = section.find("h1").text
			# color_divs = soup.find_all("div", attrs={'class': 'grid-wrapper'})
			containerH = soup.find("div", attrs={'class': 'grid-wrapper'})

			for subContainer in containerH.findAll("div", attrs={'class': 'colour-component'}):
				percent = subContainer.find("span", attrs={'class': 'percentage'}).text
				for colorContainer in subContainer.findAll("div", attrs={'class': 'colour-strip'}):
				 list_of_cells = []
				 URlsub_pos = (section.text).find("http")
				 URlsub = section.text[(URlsub_pos):]
				 list_of_cells.append(website)
				 list_of_cells.append(URlsub)
				 list_of_cells.append((colorContainer['style'])[17:][:-1])
				 list_of_cells.append(percent)
				list_of_rows.append(list_of_cells)
	indID += 1

outfile = open("./colors.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Website", "URL", "Color", "Percent"])
writer.writerows(list_of_rows)
