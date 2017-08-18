# STEP ONE
import requests # import the requests library
from bs4 import BeautifulSoup # import the BeautifulSoup library

tripadvisor_page = 'https://www.tripadvisor.com/Guide-g187323-k123-Berlin.html'
# save the request that we grab from the webpage
request = requests.get(tripadvisor_page)

# Use BeautifulSoup to parse the DOM tree from the request's HTML text
soup = BeautifulSoup(request.text, 'html.parser')

attractions_HTML = soup.find_all('div', attrs={'class': 'heading'})
types_HTML = soup.find_all('div', attrs={'class': 'subheading'})
description_HTML = soup.find_all('p', attrs={'class': 'description-text quoted'})


tips = []
#soup.find_all('div', attrs={'class': 'tip-text'})
for ultag in soup.find_all('ul', {'class': 'tip-list'}):
	tipStr = ''
	for litag in ultag.find_all('li'):

		tipStr = tipStr + ' - ' + litag.text + '\n'

	print tipStr
	tips.append(tipStr.strip())




hours = ['']
for divtag in soup.find_all('div', {'class': 'stay'}):
	for hr in divtag.findAll('span', {'class': None}):
		hours.append(hr.text);
#soup.findAll('ul', 'li', 'div', 'span', attrs={'class': None})
#hours = soup.findAll('stay', {'class': ''}).string.strip()
#hours = soup.select("p.item-details-content.stay.span")
# [<p class="body strikeout"></p>]


attractions = ['']
for attraction in attractions_HTML:
	attractions.append(attraction.text)

types = ['']
for t in types_HTML:
	types.append(t.text)

descriptions = ['']
for des in description_HTML:
	descriptions.append(des.text)







import pandas as pd
ptsOfInterest = pd.DataFrame({
        "Attraction": attractions, 
        "Type": types, 
        "Description": descriptions, 
        "Tip": tips,
        "Time": hours
    }
)


#print ptsOfInterest
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
ptsOfInterest.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
