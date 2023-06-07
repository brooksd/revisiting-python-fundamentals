from email.message import EmailMessage
from imports import password
import ssl
import smtplib

email_sender =  'vjameson644@gmail.com'
email_password = password

email_reciever = ''

subject = "Dont forget to Finish GCP DevOps"
body = """A journey of  a thousand miles begins with just one step"""

em_instance = EmailMessage()
em_instance['From'] = email_sender
em_instance['To'] = email_reciever
em_instance['subject'] = subject
em_instance.set_content(body)

def_context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=def_context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em_instance.as_string())