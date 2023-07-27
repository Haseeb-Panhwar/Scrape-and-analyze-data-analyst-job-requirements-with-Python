import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def getContent(title,loc):
    url = 'https://www.linkedin.com/jobs/search?keywords='+title+'&location='+loc+'%3D103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
    #r = requests.get(url)
    driver = webdriver.Chrome('D:\Work\Webscraping_Project\Scrape-and-analyze-data-analyst-job-requirements-with-Python\env\chromedriver.exe') 
    driver.get(url) 
    time.sleep(5) 
    html = driver.page_source
    return html

data = getContent('Software Engineer','Karachi Sindh')

import csv
jobs = []
header = ["Title","Company","Location","Link"]
soup = bs(data,'html.parser')
titles = soup.find_all('h3',class_="base-search-card__title")
company = soup.find_all('h4',class_="base-search-card__subtitle")
links = soup.find_all('a',class_="base-card__full-link absolute top-0 right-0 bottom-0 left-0 p-0 z-[2]")
loc = soup.find_all('span',class_="job-search-card__location")

'''print(len(links))
for item in (range(len(links))):
    print("\n")
    print(links[item].get('href'))'''

for item in range(len(titles)):
    job = { }
    job['Title']=(titles[item].get_text(strip=True,separator = ' ').encode('utf-8'))
    job['Company']=(company[item].get_text(strip=True,separator = ' ').encode('utf-8'))
    job['Location']=(loc[item].get_text(strip=True,separator=' ').encode('utf-8'))
    job['Link']=(links[item].get('href').encode('utf-8'))
    jobs.append(job)

print(jobs)

with open('jobs.csv','w') as f:
    writer = csv.DictWriter(f,fieldnames=header)
    writer.writeheader()
    writer.writerows(jobs)


'''with open('jobs.csv','r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)'''
        