import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

body = '''Hello,
This is the body of the email
sicerely yours
G.G.
'''
# put your email here
sender = 'ps6005.tec@gmail.com'
# get the password in the gmail (manage your google account, click on the avatar on the right)
# then go to security (right) and app password (center)
# insert the password and then choose mail and this computer and then generate
# copy the password generated here
password = 'erdl efrz ktcx vjtm'
# put the email of the receiver here
receiver = 'gonzalogtzr@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = 'This email has an attacment, a pdf file'

message.attach(MIMEText(body, 'plain'))

pdfname = 'imagen.pdf'

# open the file in bynary
binary_pdf = open(pdfname, 'rb')

payload = MIMEBase('application', 'octate-stream', Name=pdfname)
# payload = MIMEBase('application', 'pdf', Name=pdfname)
payload.set_payload((binary_pdf).read())

# enconding the binary into base64
encoders.encode_base64(payload)

# add header with pdf name
payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
message.attach(payload)

#use gmail with port
session = smtplib.SMTP('smtp.gmail.com', 587)

#enable security
session.starttls()

#login with mail_id and password
session.login(sender, password)

text = message.as_string()
session.sendmail(sender, receiver, text)
session.quit()
print('Mail Sent')