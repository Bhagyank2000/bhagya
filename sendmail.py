#sending mail usuing python



import smtplib
import getpass

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='bhagyakorlahalli@gmail.com'
receiver='bharath341reddy@gmail.com'
msg='hi duffer'
p=getpass.getpass()
s.login(sender,p)
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()