from flask import Flask, render_template, request
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap5

from datetime import datetime as dt
from music_data import Database
today = [int(dt.now().strftime('%Y')), int(dt.now().strftime('%m')), int(dt.now().strftime('%d'))]
app = Flask(__name__)
app.secret_key = "some secret key"
boostrap = Bootstrap5(app)


class MusicForm(FlaskForm):
    year = IntegerField('Year:', validators=[DataRequired(), NumberRange(min=2000, max=today[0])], default=2023)
    month = IntegerField('Month:', validators=[DataRequired(), NumberRange(min=1, max=12)], default=10)
    day = IntegerField('Day:', validators=[DataRequired(), NumberRange(min=1, max=31)], default=10)
    submit = SubmitField("Button", render_kw={"class": "btn btn-secondary btn-block"})


class MainPage(MethodView):

    def get(self):
        form = MusicForm()
        return render_template('index.html', form=form)

    def post(self):
        form = MusicForm()
        year = form.year.data
        month = form.month.data
        day = form.day.data
        if year == today[0] and month >= today[1] and day > today[2]:
            text = "Wrong day"
            return render_template('index.html', form=form, text=text)
        else:
            if month < 10:
                month = f'0{month}'
            if day < 10:
                day = f'0{day}'
            date = f'{year}-{month}-{day}'
            data = Database(date).check_data()
            text = "Good"
            return render_template('index.html', form=form, songs=data, text=text)


app.add_url_rule('/', view_func=MainPage.as_view('home'))
app.run(debug=True)
