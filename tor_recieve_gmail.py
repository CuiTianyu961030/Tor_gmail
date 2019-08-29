from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import imaplib
from httplib2 import socks
import socket
socket.socket = socks.socksocket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"127.0.0.1",1080)

mailserver = imaplib.IMAP4_SSL('imap.gmail.com', 993)

username = raw_input('mail_username: ')  #'cuitianyu961030@gmail.com'  #linjie900@gmail.com

password = raw_input('mail_password: ')  #'my18999170965ym'  #Goog1e051...

mailserver.login(username, password)

status, count = mailserver.select('Inbox')

status, data = mailserver.fetch(count[0], '(UID BODY[TEXT])')

print data[0][1]

mailfile = open('mailfile.txt', 'w')
mailfile.write(data[0][1])
mailfile.close()

mailserver.close()

mailserver.logout()