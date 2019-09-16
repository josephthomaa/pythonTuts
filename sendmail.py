 
 
 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "smartbusmonitor@gmail.com"
toaddr = "josephthomaa@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Test Subject"
body = "Hello from python"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, "")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
