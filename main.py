import pandas as ps
from sendemail import send_email
df = ps.read_csv('data.csv',engine='python')
list = []
for email in df.email:
    list.append(email)
print (list)
for mail in list:
    send_email(
        subject="testing the automation",
        name="anuj",
        receiver_email=mail,
    )
    print(f"email successfully sent to: {mail} ")
