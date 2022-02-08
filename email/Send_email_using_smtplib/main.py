# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:08:05 2022

@author: scyth
"""

import smtplib

sender ='scythe_sec@outlook.com'
receiver ='yavibit214@mannawo.com'

password = input('Enter your password here :  ')

message = '''\
Subject: Hello Hello

This is a test email!
multiline comment
thank you
'''

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender,password)
server.sendmail(sender,receiver,message)
server.quit()

print('email sent!')