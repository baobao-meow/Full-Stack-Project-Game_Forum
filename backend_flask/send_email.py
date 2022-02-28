import string
import random
# pip install PyEmail
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def verification_code_generator():
    all_uppercase_chars = string.ascii_uppercase
    all_lowercase_chars = string.ascii_lowercase
    all_nums = string.digits
    all_punctuation = ",.?!@#%*"

    verification_code = random.sample(all_uppercase_chars, 3) + random.sample(all_lowercase_chars, 3) + random.sample(all_nums, 3) + random.sample(all_punctuation, 1)

    # shuffle the verification code
    random.shuffle(verification_code)

    return ''.join(verification_code)


def send_verification_code(receiver_email):
    mail_host = "smtp.163.com"
    sender_address = "hibernia_sino@163.com"
    mail_authorization_code = "ShouQuan2019"
    sender = 'hibernia_sino@163.com'
    verification_code = verification_code_generator()
    content = "Dear player,\n\n Thank you for registering D4C game forum, here is your verification code (between < and >): <"+str(verification_code)+">, keep it safe and do NOT tell any one!\n\n Have a nice day!\nD4C game forum"

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = sender_address
    message['To'] = receiver_email
    message['Subject'] = Header("Verification code from D4C", 'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host, 25)  # 25 is the port of 163 email provider
        smtp.login(sender_address, mail_authorization_code)
        smtp.sendmail(sender, receiver_email, message.as_string())
        # print("Email sent successfully")
        return verification_code
    except smtplib.SMTPException as e:
        print(e)
        return -1


if __name__ == "__main__":
    print(verification_code_generator())