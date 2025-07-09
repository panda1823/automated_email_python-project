import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = 'vallip214@gmail.com'
password = 'fbypxovnlidkwvpd'  # Consider using environment variables for security

# Email content
from_email = 'vallip214@gmail.com'
to_email = 'sakinaladeepika19@gmail.com'
subject = 'Automated Email'
body = 'This is a test email sent from a Python script!'

# Create a multipart email
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Attach the body to the email
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP(smtp_server, smtp_port)
# Send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
    server.login(username, password)
    server.send_message(msg)
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
finally:
    server.quit()




