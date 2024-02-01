import datetime as dt
import smtplib


class SendMail:
    """
    This class take two attributes. Email address where the message is to be sent.
    The method send_mail connect to email and sent a new message.
    """
    def __init__(self, to_address, msg):
        self.to_address = to_address
        self.msg = msg

    @staticmethod
    def read_data() -> tuple[str, str]:
        with open('gmail_details.txt', 'r') as file:
            data = file.readlines()
            password = data[0]
            email = data[1]

        email_data = (password, email)
        return email_data

    def send_mail(self):
        password = self.read_data()[0]
        email = self.read_data()[1]
        date = dt.datetime.now().strftime('%d %B %Y')
        message = f'Subject: Price of items on {date} \n\nHello,\n{self.msg}'
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=self.to_address, msg=message)
        return 'Success'


