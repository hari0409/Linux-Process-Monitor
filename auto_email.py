import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate

def send_email(message,pid):
    msg = MIMEMultipart()
    msg['From'] = 'invoice-intern@outlook.com'
    msg['To'] = 'hari626007@gmail.com'
    msg['Subject'] = f"Resource over usage for PID: {pid}"
    msg.attach(MIMEText(message))

    files=[f"./complete/{pid}.txt",f"./logs/{pid}.csv"]
    for f in files:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        msg.attach(part)

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