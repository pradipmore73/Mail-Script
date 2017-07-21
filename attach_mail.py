######################################################################################
#   AUTHOR  : PRADIP MORE                                                            #
#   PURPOSE : Attache File over mail and send it with subject,msg_body etc.          #
#   Tested and Works well on Python 2.7.5 / RHEL 7.2                                 #
######################################################################################

#!/usr/bin/python

import smtplib
import socket
import datetime

from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders
from email.mime.text import MIMEText

DATE = datetime.datetime.now()
HOSTNAME = socket.gethostname()
SUBJECT = "Daily Checklist for "+ HOSTNAME
EMAIL_FROM = 'abc@xyz.com'
EMAIL_SERVER = '10.10.10.10' //mail server ip
EMAIL_TO = "abc@123.com" , "xyz@123.com"
EMAIL_BODY = "Please Find Attached Daily Report for "+ HOSTNAME +" "+ DATE.strftime("%d-%m-%Y")
EMAIL_BODY = MIMEText(EMAIL_BODY)
msg = MIMEMultipart()
msg['Subject'] = SUBJECT
msg['From'] = EMAIL_FROM
msg['To'] = ', '.join(EMAIL_TO)

part = MIMEBase('application', "octet-stream")
part.set_payload(open("/sysadmin/Checklist/"+HOSTNAME+"_"+DATE.strftime("%Y%m%d_1100")+".doc", "rb").read()) //path to attach file/filename
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="Server_Report.doc"') // File Name will be displayed on mail attachment.
msg.attach(EMAIL_BODY)
msg.attach(part)

server = smtplib.SMTP(EMAIL_SERVER)
server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
