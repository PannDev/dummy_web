from email.message import EmailMessage
from pass import password

import ssl
import smtplib

email_sender = 'dryhezelnut@gmail.com'
email_password = password

email_receiver = ''

subject = "hai"
body = """"
lol
"""

em = EmailMessage()
em['From'] = email_sender
em['to'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL
