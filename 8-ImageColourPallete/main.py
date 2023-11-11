from flask import Flask, render_template, request
from flask.views import MethodView
from werkzeug.utils import secure_filename

from formweb import UploadForm
from get_colour import ImageColor
import os

app = Flask(__name__)


class HomePage(MethodView):

    def get(self):
        # Add form file
        form = UploadForm()
        img_path = 'static/flower.jpg'
        return render_template('index.html', form=form,
                               path=img_path)

    def post(self):
        # add form
        form = UploadForm()
        img_path, settings = self.get_data()
        image_dict = ImageColor(img_path, settings['delta']).color_dict()
        color_sum = ImageColor(img_path, settings['delta']).sum_of_colors()
        i = 0
        final_dict = {}
        for k, v in image_dict.items():
            if i == settings['number']:
                break
            i = i + 1
            # count how many percent of picture constitutes a given color
            percent = (v / color_sum)*100
            final_dict[k] = round(percent, 2)
        result = True
        return render_template('index.html', form=form,
                               path=img_path, data=settings,
                               final_dict=final_dict, result=result)

    def get_data(self):
        # get data
        picture = request.files['file']
        if picture.filename != '':
            picture.save(os.path.join('static', 'new.jpg'))
            img_path = 'static/new.jpg'
        else:
            img_path = 'static/flower.jpg'
        data = UploadForm(request.form)
        settings = {'number': data.number_of_colors.data,
                    'delta': data.delta.data}
        return img_path, settings


app.add_url_rule('/', view_func=HomePage.as_view('home'))
app.run(debug=True)
