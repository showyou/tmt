# -*- coding: utf-8 -*-
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

if True:
#if False:
	homePath = "./"
else:
	homePath = os.path.abspath(os.path.dirname(__file__)) 


def create_message2(from_addr, to_addr, subject, body, encoding):
    # 'text/plain; charset="encoding"'というMIME文書を作ります
    msg = MIMEText(body, 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg


def send_via_gmail(user,passWord,from_addr, to_addr, msg):

	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(user, passWord)
	s.sendmail(from_addr, [to_addr], msg.as_string())
	s.close()
    
