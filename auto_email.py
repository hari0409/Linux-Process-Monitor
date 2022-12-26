import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart()
msg['From'] = 'invoice-intern@outlook.com'
msg['To'] = 'hari626007@gmail.com'
msg['Subject'] = 'Simple subject email in python'
message = 'here is the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('smtp-mail.outlook.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('invoice-intern@outlook.com', 'invoiceintern123')


mailserver.sendmail('invoice-intern@outlook.com','hari626007@gmail.com',msg.as_string())

mailserver.quit()
