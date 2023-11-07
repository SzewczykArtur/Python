import sqlite3

from flask import Flask, render_template, request
from flask.views import MethodView
from sqlite3 import IntegrityError

from form_class import AddCoffeehouse, DeleteCoffeehouse
from add_delete import Insert, Delete
from contact import ContactForm, SendEmail

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        connect = sqlite3.connect('instance/cafes.db')
        data = connect.execute("""
        SELECT * FROM "cafe"
        """).fetchall()
        return render_template('index.html', data=data)


class AboutPage(MethodView):

    def get(self):
        return render_template('about.html')


class InsertCoffeehouse(MethodView):

    def get(self):
        insert = AddCoffeehouse()
        return render_template('add_cafe.html', insert=insert)

    def post(self):
        result = True
        try:
            insert_cafe = AddCoffeehouse(request.form)
            cafe = Insert(name=insert_cafe.name.data,
                          map_url=insert_cafe.map_url.data,
                          img_url=insert_cafe.img_url.data,
                          location=insert_cafe.location.data,
                          has_sockets=insert_cafe.has_sockets.data,
                          has_toilet=insert_cafe.has_toilet.data,
                          has_wifi=insert_cafe.has_wifi.data,
                          can_take_calls=insert_cafe.can_take_calls.data,
                          seats=insert_cafe.seats.data,
                          coffe_price=insert_cafe.coffee_price.data)
            cafe.insert_coffeehouse()
            connect = sqlite3.connect('instance/cafes.db')
            data = connect.execute("""
                    SELECT * FROM "cafe"
                    """).fetchall()
            return render_template('index.html', result=result, data=data)
        except:
            insert = AddCoffeehouse()
            return render_template('add_cafe.html', insert=insert, result=result)


class DeleteCoffeeHouse(MethodView):

    def get(self):
        delete_form = DeleteCoffeehouse()
        return render_template('delete_cafe.html', delete_form=delete_form)

    def post(self):
        delete_form = DeleteCoffeehouse()
        delete_cafe = DeleteCoffeehouse(request.form)
        cafe = Delete(name=delete_cafe.name.data)
        result = cafe.delete_coffeehouse()
        return render_template('delete_cafe.html',delete_form=delete_form, result=result)


class ContactPage(MethodView):

    def get(self):
        contact_form = ContactForm()
        return render_template('contact.html', contact_form=contact_form)

    def post(self):
        contact_form = ContactForm()
        data_form = ContactForm(request.form)
        send_email = SendEmail(name=data_form.name.data,
                               surname=data_form.surname.data,
                               title=data_form.title.data,
                               customer_email=data_form.email.data,
                               message=data_form.message.data)
        send_email.send_email()
        send_email.add_message_to_database()
        return render_template('contact.html', contact_form=contact_form, result=True)


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/about', view_func=AboutPage.as_view('about_page'))
app.add_url_rule('/add_coffeehouse', view_func=InsertCoffeehouse.as_view('add_coffeehouse'))
app.add_url_rule('/delete_coffeehouse', view_func=DeleteCoffeeHouse.as_view('delete_coffeehouse'))
app.add_url_rule('/contact', view_func=ContactPage.as_view('contact_page'))
app.run(debug=True)
