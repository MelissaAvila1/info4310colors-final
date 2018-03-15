import requests
import csv

from BeautifulSoup import BeautifulSoup


list_of_rows = []
intID = 1
# while intID < 100000:
while intID < 200:
	url = 'http://webcolourdata.com/profile/' +str(intID)
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
				list_of_rows.awppend(list_of_cells)
	intID += 1

outfile = open("./colorsPagination.csv", "wb")
writer = csv.writer(outfile)
writer.writerow(["Website", "URL", "Color", "Percent"])
writer.writerows(list_of_rows)