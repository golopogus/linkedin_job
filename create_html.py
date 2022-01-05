from send_email import send_email

def create_html(job_list):
    html = "<body><header><h1>New Hilton HR Jobs Just For You Keke!</h1>"
    a_tag = ""
    for key in job_list:
        a_tag += "<a href=" + job_list[key] + ">" + key + "</a><br>" 
    html += a_tag + "</p></header></body>"
    file = open("email.html","w")
    file.write(html)
    file.close()
    send_email()
