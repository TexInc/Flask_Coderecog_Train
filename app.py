from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
from predict_func import verify
import os
import pickle

app = Flask(__name__)

class ReviewForm(Form):
    right_code_view = TextAreaField('', [validators.DataRequired(), validators.length(max=4)])


@app.route('/')
def index():
    right_code = ''.join(list(verify('http://221.234.230.29/CheckCode.aspx', 'model/SVC_Model_zf.pkl')))
    print(right_code)
    form = ReviewForm(request.form)
    return render_template('index.html', right_code=right_code)


@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['right_code_view']
        return render_template('')



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
