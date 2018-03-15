import requests
import csv
import time

from BeautifulSoup import BeautifulSoup
from selenium import webdriver

##UNFINISHED

list_of_rows = []




with open('sites.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		url = row[0]
		print url
		chromedriver = "/Users/melissa/Scrape/chromedriver"
		driver = webdriver.Chrome(chromedriver)
		driver.get(url)
		html = driver.page_source
		soup = BeautifulSoup(html)
		driver.quit()

		if soup.find("section", attrs={'class': 'info'}):
			section = soup.find("section", attrs={'class': 'info'})
			if section.find("h1").text:
				website = (section.find("h1").text).encode('ascii', 'ignore')
				# color_divs = soup.find_all("div", attrs={'class': 'grid-wrapper'})
				containerH = soup.find("div", attrs={'class': 'grid-wrapper'})

				for subContainer in containerH.findAll("div", attrs={'class': 'colour-component'}):
					percent = subContainer.find("span", attrs={'class': 'percentage'}).text
					for colorContainer in subContainer.findAll("div", attrs={'class': 'colour-strip'}):
					 list_of_cells = []
					 URlsub_pos = (section.text).find("http")
					 URlsub = section.text[(URlsub_pos):]
					 list_of_cells.append((website).encode('ascii', 'ignore'))
					 list_of_cells.append((URlsub.encode('utf8')))
					 list_of_cells.append(((colorContainer['style'])[17:][:-1].encode('utf8')))
					 list_of_cells.append((percent).encode('utf8'))
					 print list_of_cells
					list_of_rows.append(list_of_cells)
			else:
				print "Can't find header"
		else:
			print "Cant find section"

outfile = open("./colors2.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Website", "URL", "Color", "Percent"])
writer.writerows(list_of_rows)
