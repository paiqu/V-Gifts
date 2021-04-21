import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_email_gm(email, new_pswd):
    '''
    send reset code email
    '''
    # try:
    # set host and receiver
    host_name = "smtp.gmail.com"
    host_port = 465
    sender_email = 'oldjeffspectator@gmail.com'
    sender_password = 'jeffLHR123'
    receivers = email 
    # email info
    Title = 'Reset Code Sent!'
    subject = 'Here is your Temporary Password: ' + new_pswd

    message = MIMEText(subject, 'plain', 'utf-8')
    message['From'] = Header("Dear user, you have reset your password", 'utf-8')
    message['To'] =  Header(email, 'utf-8')
    message['Subject'] = Header(Title, 'utf-8')
    server = smtplib.SMTP_SSL(host_name, host_port)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receivers, message.as_string())
    server.quit()
    print("E-mail sent")
    # except:
    #     pass

if __name__ == "__main__":
    send_email_gm("haoran.lyu@student.unsw.edu.au", "123321")