from bs4 import BeautifulSoup
import requests
import pandas

response = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=")
print(response.status_code)
#soup = BeautifulSoup(response.text,'lxml') # < - tenho de ver isso do lxml
#jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')