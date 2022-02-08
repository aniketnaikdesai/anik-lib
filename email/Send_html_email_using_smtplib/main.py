# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:29:06 2022

@author: scyth
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


sender ='scythe_sec@outlook.com'
receiver ='yavibit214@mannawo.com'

password = input('Enter your password here :  ')

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'Hello Again - Html email'

body = '''
<h1>Hi There!</h1>
<h2>There are cats and dogs</h2>
bye bye thank you
'''

mimetext = MIMEText(body,'html')
message.attach(mimetext)


server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
message_text = message.as_string()
server.sendmail(sender,receiver,message_text)
server.quit()

print('email sent!')