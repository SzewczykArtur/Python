from flask import Flask, render_template, request
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField,ValidationError
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

from database import Database, UpdateDatabase, AdminUpdate
from create_password import check_password, generate_password_hash
from check_box import confirm, update_account

# MethodView automatically sets View.methods based on the methods defined by the class.
# It even knows how to handle subclasses that override or define other methods.


class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message="Wrong email! Use @ and '.'")])
    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                 Length(min=8, max=20, message='Must be between 8 and 20 characters long')])
    submit = SubmitField(label='Log In')


class RegisterForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message="Wrong email! Use @ and '.'")])
    password = PasswordField(label='Password',
                             validators=[
                                 DataRequired(),
                                 Length(min=8, max=20, message='Must be between 8 and 20 characters long')])
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[
                                         DataRequired(),
                                         Length(min=8, max=20,message='Must be between 8 and 20 characters long')])
    submit = SubmitField(label='Register')


class AdminButton(FlaskForm):
    delete_button = SubmitField(label='Delete Account')
    update_button = SubmitField(label='Update data', id='0')


app = Flask(__name__)
app.secret_key = "some secret string"
bootstrap = Bootstrap5(app)


class LoginPage(MethodView):
    """
    This class replies for create a login page. It requires for user to type login and password to open main page.
    Before user will be transferred to main page, program checks if data is correct.
    Also user can register new account by clicking on the link.
    """
    def get(self):
        form = MyForm()
        return render_template('login_page.html', form=form)

    def post(self):
        form = MyForm()
        user = form.email.data
        password = form.password.data
        datas = Database('instance/data.sql').read_data()

        # print(user == 'admin@gmai.com')
        # print(check_password(datas[user]['password'], password))
        # Check if admin is login
        if user == 'admin@gmail.com' and check_password(datas[user]['password'], password):
            # print('admin')
            form = AdminButton()
            datas = Database('instance/data.sql').read_data()
            # for data in datas:
                # print(datas[data])
            return render_template('admin_page.html', text='Hello admin!', datas=datas, form=form)

        if user in datas:
            # Check if user is in database
            # print(datas[user]['password'])
            if check_password(datas[user]['password'], password):
                # print(user)
                return render_template('index.html', text='Correct data!')
            else:
                text = 'Wrong data!'
                return render_template('login_page.html', form=form, text=text, email=user)
        else:
            # if this user not exist. Program opens a register page.
            register_form = RegisterForm()
            # print('Register page')
            return render_template('register_page.html', register_form=register_form, text='')
        # return render_template('login_page.html', form=form)


class RegisterPage(MethodView):
    """
    This class create a register page. Where user can create new account. This data is safe to database.
    """

    def get(self):
        register_form = RegisterForm()
        print('Register page')
        return render_template('register_page.html', register_form=register_form, text='')

    def post(self):
        form = MyForm()
        register_form = RegisterForm()

        # Get data from inputs and read database
        datas = Database('instance/data.sql').read_data()
        email = register_form.email.data
        password = register_form.password.data
        confirm_password = register_form.confirm_password.data

        if email not in datas:
            # Check if this user is already sing. If not
            result = True
            while result:
                if password == confirm_password:
                    # Check if both passwords are identical, if so, it hashs password and add to database
                    hash_password = generate_password_hash(password)
                    UpdateDatabase(file='instance/data.sql', email=email, password=hash_password).add_new_user()
                    result = False
                else:
                    text = 'Both passwords are different. Please submit the same passwords'
                    return render_template('register_page.html', register_form=register_form, text=text)

            text = 'Your account is successfully create. Please sing up!!!'
            return render_template('login_page.html', form=form, text=text)

        else:
            # if this user already exist, user is transferred to login page
            text = 'This user already exist, please log in!'
            return render_template('login_page.html', form=form, text=text)


class MainPage(MethodView):

    def get(self):
        return render_template('index.html')


class AdminPage(MethodView):

    def get(self):
        return render_template('admin_page.html')

    def post(self):
        datas = Database('instance/data.sql').read_data()
        button_update = request.form.get('update')
        button_delete = request.form.get('delete')
        account_name = ''

        if button_update:
            # This part of program allow admin to change specific user data.
            for data in datas:
                if datas[data]['id'] == int(button_update):
                    account_name = data
            check = update_account(account_name)

            if check[0] == 1:
                if len(check[1]) >= 3:
                    new_email = check[1]
                    AdminUpdate('instance/data.sql', int(button_update)).update_email(new_email)
                    datas = Database('instance/data.sql').read_data()

                if len(check[2]) >= 3:
                    new_password = generate_password_hash(check[2])
                    AdminUpdate('instance/data.sql', int(button_update)).update_password(new_password)
                    datas = Database('instance/data.sql').read_data()
            return render_template('admin_page.html', text='Hello admin!', datas=datas)

        if button_delete:
            # check if admin press delete button. If so, program show new window, where admin have to confirm that he
            # delete this account
            text = ''
            for data in datas:
                # check which account is deleting
                if datas[data]['id'] == int(button_delete):
                    text = data

            if confirm(text) == 1:
                # if admin confirm, program delete this user, also refresh his page
                delete_account = AdminUpdate(file='instance/data.sql', id=int(button_delete))
                delete_account.delete_account()
                datas = Database('instance/data.sql').read_data()
                return render_template('admin_page.html', datas=datas)

        return render_template('admin_page.html', text='Hello admin!', datas=datas)


app.add_url_rule('/', view_func=LoginPage.as_view('login'))
app.add_url_rule('/register', view_func=RegisterPage.as_view('Register'))
app.add_url_rule('/home', view_func=MainPage.as_view('home'))
app.add_url_rule('/admin', view_func=AdminPage.as_view('admin_page'))
app.run(debug=True)


# if __name__ == ' __main__':
#     web_main()
