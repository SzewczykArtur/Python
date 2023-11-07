from wtforms import Form, StringField, SubmitField, validators, TextAreaField, EmailField
from wtforms.widgets import TextArea
from password import email_password, main_email
import yagmail
import sqlite3


class ContactForm(Form):
    # form for contact page
    title = StringField("Topic: ", [validators.data_required(), validators.length(max=100)])
    name = StringField("Name: ", [validators.data_required(), validators.length(max=50)])
    surname = StringField("Surname: ", [validators.data_required(), validators.length(max=50)])
    email = EmailField('Your e-mail: ', [validators.data_required(), validators.length(max=100)])
    message = TextAreaField("Your message: ", [validators.data_required(), validators.length(max=1000)], widget=TextArea(),)
    button = SubmitField('SEND')


class SendEmail:

    def __init__(self, name, surname, title, customer_email, message):
        self.name = name
        self.surname = surname
        self.title = title
        self.customer_email = customer_email
        self.message = message

    def send_email(self):
        # Autmatically send message
        msg = f"Hi {self.name},\n" \
              f"This message is send automatically, please don't reply.\n\n" \
              f"Your message is: {self.message}\n\n" \
              f"We while answer as soon as possible!\n\n" \
              f"Regards Coffee Team."
        subject = self.title
        email = yagmail.SMTP(user=main_email, password=email_password)
        email.send(to=self.customer_email,
                   subject=subject,
                   contents=msg)

    def add_message_to_database(self):
        # add message to database with all information
        connection = sqlite3.connect('instance/customer.db')
        connection.execute(f"""
        INSERT INTO "clients" ("name", "surname", "topic", "email",
        "massage") VALUES ("{self.name}", "{self.surname}",
        "{self.title}", "{self.customer_email}", "{self.message}")
        """)
        connection.commit()
        connection.close()
