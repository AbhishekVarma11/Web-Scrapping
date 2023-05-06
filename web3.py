#scrapping the data from the jobs website 
import requests
from bs4 import BeautifulSoup
import time
url="https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation="
#use text property get the html code otherwise it returns the status code 
data=requests.get(url).text
bs=BeautifulSoup(data,"lxml")
unfamiliar_skills=input("enter the skills that you are not familiar with:")
print('Filtering out the Skills....')
def find_jobs():
    jobs=bs.find_all('li',class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            if unfamiliar_skills not in skills.lower():         
                more_info=job.header.h2.a['href']#for accessing the attribute 
                with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company-name:{company_name.strip()}")
                    f.write(f"required_skills:{skills.strip()}")
                    f.write(f'More Info:{more_info}')
                print(f'file saved {index}')

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        time.sleep(time_wait*10)