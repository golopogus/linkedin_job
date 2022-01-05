import smtplib
import ssl
from email.mime.text import MIMEText  # New line
from email.utils import formataddr  # New line

def send_email():
    # User configuration
    sender_email = "keke4hilton@gmail.com"
    sender_name = "keke4hilton"
    password = "keke4hilton123@!"

    # receiver_emails = ["keke4hilton@gmail.com"]
    # receiver_names = ["Keke Jam"]

    receiver_emails = ["kzellmer01@saintmarys.edu"]
    receiver_names = ["Keke Jam"]
    # Email text
    email_html = open('email.html')
    email_body = email_html.read()

    for receiver_email, receiver_name in zip(receiver_emails, receiver_names):
       # print("Sending the email...")
        # Configurating user's info
        msg = MIMEText(email_body, 'html')
        msg['To'] = formataddr((receiver_name, receiver_email))
        msg['From'] = formataddr((sender_name, sender_email))
        msg['Subject'] = 'Newest Hilton HR Jobs!'
        try:
            # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
            server = smtplib.SMTP('smtp.gmail.com', 587)
            # Encrypts the email
            context = ssl.create_default_context()
            server.starttls(context=context)
            # We log in into our Google account
            server.login(sender_email, password)
            # Sending email from sender, to receiver with the email body
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print('Email sent!')
        except Exception as e:
            print(f'Oh no! Something bad happened!n {e}')
        finally:
            print('Closing the server...')
            server.quit()