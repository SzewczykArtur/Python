from wtforms import Form, IntegerField, StringField, BooleanField, SubmitField, validators


class AddCoffeehouse(Form):
    id = IntegerField()
    name = StringField('Name: ', [validators.data_required(), validators.length(max=200)])
    map_url = StringField('Map url:', [validators.data_required(), validators.length(max=500)])
    img_url = StringField('IMG url:', [validators.data_required(), validators.length(max=500)])
    location = StringField('Location:', [validators.data_required(), validators.length(max=200)])
    has_sockets = BooleanField('Has sockets:')
    has_toilet = BooleanField('Has toilet:')
    has_wifi = BooleanField('Has WIFI:')
    can_take_calls = BooleanField('Cane take calls:')
    seats = StringField('Seats: ', [validators.data_required(), validators.length(max=20)])
    coffee_price = StringField('Coffe price: ', [validators.data_required(), validators.length(max=20)])
    button = SubmitField('Add new coffeehouse')


class DeleteCoffeehouse(Form):
    name = StringField('Name: ')
    button = SubmitField('Delete coffeehouse')
