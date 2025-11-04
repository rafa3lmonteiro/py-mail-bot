#!/usr/bin/env python3

# Send email using lib smtplib and google smtp service
# Rafael Conte Monteiro - 09/2025

import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from secret import passwd

EMAIL_ADDRESS = 'your-email-here@gmail.com'
EMAIL_PASSWORD = passwd
EMAIL_TO = 'your-email-destination@gmail.com'

msg = EmailMessage()
with open('./email') as fp:
    msg.set_content(fp.read())

msg['Subject'] = 'Your email subject here'
msg['From'] = formataddr(("Rafael Conte Monteiro", EMAIL_ADDRESS))
msg['To'] = formataddr(("Recipient's name", EMAIL_TO))  # optional to include the recipient's name

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


