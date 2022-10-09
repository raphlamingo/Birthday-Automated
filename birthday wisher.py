import smtplib
import random
import datetime as dt
import pandas as pd

#'panda documentation#
dates = pd.read_csv('birthdays.csv')
birth= dates.to_dict(orient='records')

f = random.randint(1,3)


# datetime
today = dt.datetime.now()
date_month = today.day
monthss = today.month



my_mail = '#insert email'
password = 'password.'

for d in birth:
    if d['month'] == monthss and d['day'] == date_month:
        with open(f'letter_{f}.txt', mode='r') as messages:
            mail = messages.read()
            new_mail = mail.replace('[NAME]',d['name'] )
        send_to = d['email']
        with smtplib.SMTP('smtp.gmail.com') as new:
            new.starttls()
            new.login(user=my_mail, password=password)
            new.sendmail(from_addr=my_mail, to_addrs=send_to,msg=f'Subject: IM TRYING OUT A NEW PROJECT\n\n{new_mail}')





