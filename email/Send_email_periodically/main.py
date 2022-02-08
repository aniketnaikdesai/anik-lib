import os
import yagmail
import time

sender ='aniket.nd@gmail.com'
receiver ='hahaf62189@rippb.com'
subject = 'test email'
contents = """
multiline email message body
sent via python
"""
count = 1
while True:
  yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
  yag.send(to=receiver,subject=subject+str(count), contents=contents)
  print('email sent')
  count +=1
  time.sleep(60) #seconds


