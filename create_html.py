def create_html(job_list):
    html = "<body>"
    a_tag = ""
    for key in job_list:
        a_tag += "<a href=" + job_list[key] + ">" + key + "</a><br>" 
    html += a_tag + "</p></body>"
    file = open("email.html","w")
    file.write(html)
    file.close()