from wtforms import Form, SubmitField, IntegerField, validators


class UploadForm(Form):
    number_of_colors = IntegerField('Numbers of colors: ', validators=[validators.data_required(), validators.length(3)], default=10)
    delta = IntegerField('Delta: ', validators=[validators.data_required(), validators.length(3)], default=20)
    button = SubmitField('Run')
