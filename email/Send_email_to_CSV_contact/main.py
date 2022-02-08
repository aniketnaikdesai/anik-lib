import os
import yagmail

sender ='aniket.nd@gmail.com'
#receiver ='hahaf62189@rippb.com'
subject = 'test email'
contents = """
multiline email message body
sent via python
"""

yag = yagmail.SMTP(user=sender,password=os.getenv('PASSWORD'))
yag.send(to=receiver,subject=subject, contents=contents)

print('email sent')