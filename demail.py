import smtplib
import ssl


class demail:
    email_template = """\
            Subject: Your task is about to due
            
            check out your personal Never_Forget for more details"""

    def __init__(self, acc, psw, sendto):
        self.sender_email = acc if acc else "example@gmail.com"
        self.password = psw if psw else "123456"
        self.port = 465
        self.smtp_server = "smtp.gmail.com"

        self.receiver_email = sendto

    def send(self, msg):
        message = msg if msg else Email.email_template
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, message)
