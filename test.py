import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

def sendEmailTest():
    fromaddr = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASSWORD')
    # import pdb
    # pdb.set_trace()
    emailList = ["mp367981@gmail.com", "iamoneofmyownkind@gmail.com"]

    for dest in emailList:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = dest
        msg['Subject'] = "Reminder from Manish"
        body = "<h1>Hi, its time to drink water</h1>"
        msg.attach(MIMEText(body, 'html'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, password)
        text = msg.as_string()
        s.sendmail(fromaddr, dest, text)
        s.quit()
