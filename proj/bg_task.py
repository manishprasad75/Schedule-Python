from proj.tasks import celery
from datetime import datetime
from test import sendEmailTest
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


@celery.task(soft_time_limit=300)
def show_current_time(*args, **kwargs):
    print("[show_current_time] : {}".format(datetime.utcnow()))


@celery.task(name='add task')
def add(x, y):
    raise Exception("Some Exception x={}, y={}".format(x, y))
    return x + y


@celery.task(name='mul task')
def mul(x, y):
    return x * y


@celery.task
def xsum(numbers):
    return sum(numbers)

@celery.task
def sendEmail():
    sendEmailTest()
    # emailList = ["mp367981@gmail.com", "iamoneofmyownkind@gmail.com"]
    #
    # for dest in emailList:
    #     s = smtplib.SMTP('smtp.gmail.com', 587)
    #     s.starttls()
    #     s.login("sender_email_id", "sender_email_id_password")
    #     message = "Message_you_need_to_send"
    #     s.sendmail("sender_email_id", dest, message)
    #     s.quit()

