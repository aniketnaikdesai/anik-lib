# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:28:58 2022

@author: scyth
"""

import yagmail
import pandas as pd


sender = 'aniket.nd@gmail.com'
PASSWORD = input('Enter your password here :  ')

subject = 'Bill attached'
yag = yagmail.SMTP(user=sender,password=PASSWORD)


df = pd.read_csv('contacts.csv')

def generate_file(filename,content):
    with open(filename+'.txt','w') as file:
        file.write(str(content))


for index,row in df.iterrows():
    name = row['name']
    amount = row['amount']
    generate_file(name,amount)
    
    receiver = row['email']
    contents = f'''
    Hi {name}
    Your bill is {amount}
    this is a multiline comment
    thanks
    '''
    yag.send(to=receiver,subject=subject,contents=contents,
             attachments=(name+'.txt'))
    print(f'email sent to {name}!')

