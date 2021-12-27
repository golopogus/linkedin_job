import requests
import os
import os.path
import time
from check_if_hr import check_if_hr
from create_html import create_html
from check_new_jobs import check_new_jobs
from os import path
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

URL = "https://www.linkedin.com/jobs/search?keywords=Hilton%2BHuman%2BResources&location=Herndon%2C%2BVirginia%2C%2BUnited%2BStates&geoId=104624893&distance=25&f_C=2449&currentJobId=2823230746&position=10&pageNum=0"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find_all("ul", class_="jobs-search__results-list")[0]

jobs = results.find_all("a", class_="base-card__full-link")

job_dict = {}

for job in jobs:
    time.sleep(1)
    job_url = job.get("href")
    job_title = job.find("span")
    if check_if_hr(job_url):
        job_text_split = job_title.text.split()
        job_text = ' '.join(job_text_split)
        job_dict[job_text] = job_url

check_new_jobs(job_dict)
#create_html(job_dict)

    







