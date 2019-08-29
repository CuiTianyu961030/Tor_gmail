import smtplib
import sys
import email.mime.text
from httplib2 import socks
import socket
socket.socket = socks.socksocket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)

# my test mail
mail_username = raw_input('mail_username: ')#'cuitianyu961030@gmail.com'  #linjie900@gmail.com
mail_password = raw_input('mail_password: ')#'my18999170965ym'  #Goog1e051...
from_addr = mail_username
to_addrs = ('bridges@torproject.org')

# HOST & PORT
HOST = 'smtp.gmail.com'
PORT = 25

# Create SMTP Object
smtp = smtplib.SMTP()
print 'connecting ...'

# show the debug log
smtp.set_debuglevel(1)

# connet
try:
    print smtp.connect(HOST, PORT)
except:
    print 'CONNECT ERROR ****'
# gmail uses ssl
smtp.starttls()
# login with username & password
try:
    print 'loginning ...'
    smtp.login(mail_username, mail_password)
except:
    print 'LOGIN ERROR ****'
# fill content with MIMEText's object
msg = email.mime.text.MIMEText('get bridges')
msg['From'] = from_addr
msg['To'] = to_addrs
msg['Subject'] = 'get bridges'
print msg.as_string()
smtp.sendmail(from_addr, to_addrs, msg.as_string())
smtp.quit()