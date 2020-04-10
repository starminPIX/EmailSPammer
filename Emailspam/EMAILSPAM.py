import os
import smtplib
import getpass
import sys


server = raw_input ('gmail or yahoo: ')
user = raw_input('Username: ')
passwd = getpass.getpass('Password: ')


to = raw_input('\nTo: ')

body = raw_input('Message: ')
total = input('Number of send: ')

if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print 'Applies only to gmail and yahoo.'
    sys.exit()

print ''

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total+1):
        subject = os.urandom(9)
        msg = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
        server.sendmail(user,to,msg)
        print "\rTotal emails sent: %i" % i
        sys.stdout.flush()
    server.quit()
    print '\n Done'
except KeyboardInterrupt:
    print 'Canceled'
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print '\n The username or password incorrect