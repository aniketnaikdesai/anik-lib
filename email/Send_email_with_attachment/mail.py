# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:01:55 2022

@author: scyth
"""

import yagmail

sender ='aniket.nd@gmail.com'
receiver = 'aniket.nd@gmail.com'
#receiver = 'pilorin860@mannawo.com'

PASSWORD=input('Input your email password :  ')

subject = 'email with attachment'

contents = '''
Hi
This is a multiline content
'''

yag = yagmail.SMTP(user=sender,password=PASSWORD)

yag.send(to=receiver, subject = subject, contents = contents, 
         attachments=('./test.txt'))

print('email sent')