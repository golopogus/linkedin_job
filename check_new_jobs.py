import json
import os
import re

def check_new_jobs(job_dict):
    new_job = False
    temp_job_dict = {}
    for job in job_dict: 
        job_url = job_dict[job]
        print(job_url)
        job_id_start = job_url.find("externalApply/") + 14
        job_id_end = job_url[job_id_start:].find("?") + job_id_start
        job_id = job_url[job_id_start:job_id_end]
        temp_job_dict[job] = job_id

    file_check = "all_jobs_sent.json"
    if os.stat(file_check).st_size == 0:
        file = open("all_jobs_sent.json","w")
        json.dump(temp_job_dict,file)
        new_job = True
    else:
        file_temp = open("all_jobs_sent.json","r")
        all_jobs_dict = json.load(file_temp)

        file = open("all_jobs_sent.json","w")

        for job in temp_job_dict: 
            if temp_job_dict[job] not in all_jobs_dict.values():
                #print(all_jobs_dict.values())
                all_jobs_dict[job] = temp_job_dict[job]
                new_job = True
        
        json.dump(all_jobs_dict, file)
    
    file.close()
    #print(new_job)
    return new_job
# job_d = {"Senior Director, HR & Workplace Communications": "https://www.linkedin.com/jobs/view/senior-director-hr-workplace-communications-at-hilton-2853130842?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=nGS3JxQ9Ea4hT6q8yXf3JA%3D%3D&position=2&pageNum=0&trk=public_jobs_jserp-result_search-card", "Senior Analyst, Corporate Compensation": "https://www.linkedin.com/jobs/view/senior-analyst-corporate-compensation-at-hilton-2835695096?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=0WOClW8Ei34OO7zqXj0pyA%3D%3D&position=8&pageNum=0&trk=public_jobs_jserp-result_search-card", "Manager, Labor Relations": "https://www.linkedin.com/jobs/view/manager-labor-relations-at-hilton-2818547379?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=Z2b%2BhPK8Vyffy2SoH0Tzwg%3D%3D&position=7&pageNum=0&trk=public_jobs_jserp-result_search-card", "Learning Experience Analyst": "https://www.linkedin.com/jobs/view/learning-experience-analyst-at-hilton-2821289916?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=MD0Fvk%2BCDdWHarslzZTQUA%3D%3D&position=5&pageNum=0&trk=public_jobs_jserp-result_search-card", "Vice President, HR Consulting": "https://www.linkedin.com/jobs/view/vice-president-hr-consulting-at-hilton-2830956162?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=%2FGephsugC2MQ7Jr9Aj4XNQ%3D%3D&position=3&pageNum=0&trk=public_jobs_jserp-result_search-card", "Senior Specialist, HR Consulting": "https://www.linkedin.com/jobs/view/senior-specialist-hr-consulting-at-hilton-2829302207?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=j6vaz9FZN1ZAGbZ%2FAVJJ6g%3D%3D&position=4&pageNum=0&trk=public_jobs_jserp-result_search-card", "Senior Analyst, Executive Compensation": "https://www.linkedin.com/jobs/view/senior-analyst-executive-compensation-at-hilton-2840393829?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=IOS4T4Yr0iiJj6Q8CE77cA%3D%3D&position=9&pageNum=0&trk=public_jobs_jserp-result_search-card", "Director, Human Resources Consulting": "https://www.linkedin.com/jobs/view/director-human-resources-consulting-at-hilton-2821289925?refId=Pynyp7pI1LX6Xs5DkiHFQg%3D%3D&trackingId=av2doQeJQCaMKYYQP8W%2FoA%3D%3D&position=1&pageNum=0&trk=public_jobs_jserp-result_search-card"}
# check_new_jobs(job_d)