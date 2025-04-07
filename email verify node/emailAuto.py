# credit https://www.youtube.com/watch?v=g_j6ILT-X0k The PyCoach "how to send emails with python[new method 2023]"

import sys
from email.message import EmailMessage
import ssl
import smtplib

# Get email and verification code from the command line arguments
email_receiver = sys.argv[1]  # First argument (email)
verification_code = sys.argv[2]  # Second argument (code)

email_sender = 'codeVerifyAuto@gmail.com'
email_password = 'jxdc eicr zvyl iagr'

# Set the email subject and body
subject = 'Verification Code'
body = f"Your verification code is {verification_code}."

# Create the email message
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Set up secure SSL context
context = ssl.create_default_context()

# Send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print(f"Verification code {verification_code} sent to {email_receiver}")
