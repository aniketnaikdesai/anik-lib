import os
import yagmail
import time
from datetime import datetime as dt
from pytz import timezone

tz = timezone('EST')

sender ='aniket.nd@gmail.com'
receiver ='hahaf62189@rippb.com'
subject = 'test email'
contents = """
multiline email message body
sent via python
"""


count = 1
while True:
  now = dt.now(tz)
  if now.hour == 4 and now.minute == 29:
    yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
    yag.send(to=receiver,subject=subject+str(count), contents=contents)
    print('email sent')
    count +=1
    time.sleep(60) #seconds



