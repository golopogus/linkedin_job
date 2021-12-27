import json

def check_new_jobs(job_dict):
    file = open("all_jobs_sent.json")
    all_jobs_dict = json.load(file)
    print(all_jobs_dict)
    
    # for job in job_dict:
    #     if job_dict[job] in job_dict.values():
    #         print(text)
    #         file.close()

job_d = {"1":"2","3":"4"}           
check_new_jobs(job_d)