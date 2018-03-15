import requests
import csv
import time

from BeautifulSoup import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException


list_of_rows = []
toprint = False

def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)

with open('rawsites.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		url = "http://stylifyme.com/?stylify=" + row[0]
		chromedriver = "/Users/melissa/Scrape/chromedriver"
		driver = webdriver.Chrome(chromedriver)
		driver.get(url)
		try:
			html = driver.page_source
			soup = BeautifulSoup(html)
			driver.quit()

			soup = BeautifulSoup(html)
			for cont in soup.findAll("div", attrs={'class': 'grid_2'}):
				if cont.find("figure", attrs={'class': 'swatch-wrap'}):
					section = cont.find("figure", attrs={'class': 'swatch-wrap'})
					if "bg-color" in section.get('id'):
						subSection = section.find("div", attrs={'class': 'swatchholder'})
					 	# style = ((subSection['style'])[15:][:-1]) % (0, 128, 64)
						occurenceIndex = findnth(row[0], ".", 1)
						website = row[0][4:occurenceIndex]
						# color_divs = soup.find_all("div", attrs={'class': 'grid-wrapper'})
						contCaption = (section.find("figcaption")).find("span", attrs={'class': 'colour-hex'})
						caption = contCaption.text
						list_of_cells = []
						URlsub_pos = (section.text).find("http")
						URlsub = section.text[(URlsub_pos):]
						list_of_cells.append(website)
						list_of_cells.append(row[0])
						list_of_cells.append(caption)
						toprint = True
				if toprint:
					list_of_rows.append(list_of_cells)
					toprint = False
		except UnexpectedAlertPresentException:
			"Page DNE"
			driver.quit()

outfile = open("./colors_stylify.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Website", "URL", "Color"])
writer.writerows(list_of_rows)