#!/usr/bin/env python
import smtplib

mail_server = 'localhost'
mail_server_port = 25

from_addr = 'ravi@localhost'
to_addr = 'training@localhost'

from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s\r\n\r\n' % to_addr
subject_header = 'Subject: test mail'

body = 'testing smtp server........'

email_message = '%s\n%s\n%s\n\n%s' \
                % (from_header, to_header, subject_header, body)

s = smtplib.SMTP(mail_server, mail_server_port)
s.sendmail(from_addr, to_addr, email_message)
s.quit()

