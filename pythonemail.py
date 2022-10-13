from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def send_email_attach(from_address, to_address, password, content, subject,filename, attachment):
    msg = MIMEMultipart()



    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject



    msg.attach(MIMEText(content, 'plain'))

    filename = filename
    attachment = open(attachment, 'rb')

    p = MIMEBase('application', 'octet-stream')

    p.set_payload((attachment.read()))

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename=%s" % filename)

    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', port=587)

    s.starttls()

    s.login(from_address, password)

    text = msg.as_string()

    s.sendmail(from_address, to_address, text)

    print("Email sent")

    s.quit()

def send_email(from_address, to_address, password, content, subject):
    msg = MIMEMultipart()



    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject



    msg.attach(MIMEText(content, 'plain'))


    s = smtplib.SMTP('smtp.gmail.com', port=587)

    s.starttls()

    s.login(from_address, password)

    text = msg.as_string()

    s.sendmail(from_address, to_address, text)

    print("Email sent")

    s.quit()

def main():
    from_address = str(input("What email are you sending from?"))
    print("")
    print(
        "In order to send from this email through python, you need to enable two-factor authentication on this account by going to the security section of managing your google account and then creating an app password."
        "\n You should select other for the app type and name it python to then generate an app password.  \n The password you get from this process is what you should enter below.")
    print("")
    password = str(input("What app password did you get?"))
    print("")
    to_address = str(input("What email would you like to send to?"))
    print("")
    subject = str(input("What would you like to be the subject of this email?"))
    print("")
    content = str(input("What would you like to be the content of this email?"))
    print("")

    print(" Press 1 to send an email with an attachment.")
    print(" Press 2 to send an email without an attachment.")
    value = int(input("Would you like to send an email with or without an attachment? "))
    print("")

    if value == 2:
        send_email(from_address, to_address, password, content, subject)
    elif value == 1:
        filename = str(input("What is the name of the file you are attaching?"))
        attachment = str(input("What is the path of the file you are attaching?"))
        send_email_attach(from_address, to_address, password, content, subject, "r" + filename, attachment)




main()

