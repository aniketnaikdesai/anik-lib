# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:48:31 2022

@author: scyth
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


sender = 'scythe_sec@outlook.com'
receiver = 'yavibit214@mannawo.com'

PASSWORD = input('Enter your password here :  ')


message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = ' Hi there again! HTML+Attachment'

body = '''
<h1> Big Title</h1>
<h2> Small Title</h2>
Text body
'''

mimetext = MIMEText(body,'html')
message.attach(mimetext)

attachment_path = 'test.txt'
attachment_file = open(attachment_path,mode='rb')
payload =  MIMEBase('application', 'octate-stream')
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', 
                   filename=attachment_path)
message.attach(payload)


server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender, PASSWORD)
message_text = message.as_string()
server.sendmail(sender, receiver, message_text)
server.quit()
print('email sent!')








