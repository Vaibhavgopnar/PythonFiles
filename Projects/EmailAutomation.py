import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('vaibhavgp7436@gmail.com','V2169@gp')
subject = "test python"
body = "I Love Python"
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['gopnarvm2169@gmail.com','vaibhavpatil7754@gmail.com']
ob.sendmail('vaibhavgp7436@gmail.com',listadd,message)
print("sent mail")
ob.quit()