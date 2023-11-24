"""
This program is responsible for create a web, where user can upload a photo. Next this photo is divided for a colors.
User decides for how many colors is photo is change (typing delta). For example if he types 256, program give only one
color, but if 10 its generate 240 colors. Also, user gives how many colors he wants to see. When user press a
button 'RUN' on page appear a tabel (color, RGB, and how many this colors is on picture).
"""

from flask import Flask, render_template, request
from flask.views import MethodView

from formweb import UploadForm
from get_colour import ImageColor
import os

# Page initializer
app = Flask(__name__)


# Main page
class HomePage(MethodView):

    # Default page
    def get(self):
        # Adding a form
        form = UploadForm()
        # Upload a default img, which appear on page
        img_path = 'static/flower.jpg'
        # give variables to html page
        return render_template('index.html', form=form,
                               path=img_path)

    # If user make action (press Run), page change using this program
    def post(self):
        # adding a  form
        form = UploadForm()
        # Using method 'get_data' download a photo
        img_path, settings = self.get_data()

        # below code creates to variables, first is dictionary which content a colors, with number,
        # second is total number of colors
        image_dict = ImageColor(img_path, settings['delta']).color_dict()
        color_sum = ImageColor(img_path, settings['delta']).sum_of_colors()
        i = 0
        final_dict = {}
        # This loop is responsible for iterating on colors dictionary, and change number of colors to
        # percentage of color. After achieve number of colors type by user is stop and creates final dictionary
        for k, v in image_dict.items():
            if i == settings['number']:
                break
            i = i + 1
            # count how many percent of picture constitutes a given color
            percent = (v / color_sum)*100
            final_dict[k] = round(percent, 2)
        result = True
        # give variables to html page
        return render_template('index.html', form=form,
                               path=img_path, data=settings,
                               final_dict=final_dict, result=result)

    def get_data(self):
        # get data from the upload photo
        picture = request.files['file']
        # if user didn't upload a photo there's a default photo 'flower.jpg'
        if picture.filename != '':
            picture.save(os.path.join('static', 'new.jpg'))
            img_path = 'static/new.jpg'
        else:
            img_path = 'static/flower.jpg'
        # next program get datas like: delta and how many colors show
        data = UploadForm(request.form)
        settings = {'number': data.number_of_colors.data,
                    'delta': data.delta.data}
        return img_path, settings


app.add_url_rule('/', view_func=HomePage.as_view('home'))
app.run(debug=True)
