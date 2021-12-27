import requests
import os
import os.path
from os import path
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def check_if_hr(job_url):

    URL = job_url

    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find("ul", class_="description__job-criteria-list")         

    job_type = results.find_all("span", class_="description__job-criteria-text description__job-criteria-text--criteria")[2]

    job_type_text = job_type.text.split()

    if job_type_text[0] == 'Human' and job_type_text[1] == 'Resources':
        return(True)
