#scrapping the data from the jobs website 
import requests
from bs4 import BeautifulSoup
url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
#use text property get the html code otherwise it returns the status code 
data=requests.get(url).text
bs=BeautifulSoup(data,"lxml")
jobs=bs.find_all('li',class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    published_date=job.find('span',class_='sim-posted').span.text
    if 'few' in published_date:
        company_name=job.find('h3',class_='joblist-comp-name').text.strip()
        skills=job.find('span',class_='srp-skills').text.strip()
        print(f''' Company-name:{company_name}  required_skills:{skills}''')
        print('')

