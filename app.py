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
    right_code = ''.join(list(verify('http://125.221.35.100/CheckCode.aspx', 'model/SVC_Model_zf.pkl')))
    with open("right_code.txt",'a+') as f:
        f.write(right_code+'\n')
    form = ReviewForm(request.form)
    return render_template('index.html', right_code=right_code, form=form)


@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    review = request.form['right_code_view']
    with open('right_code.txt', 'r+') as f:
        f_list = f.readlines()
        f_list_len = len(f_list)
        f_list[f_list_len - 1] = review+'\n'
        with open('right_code.txt', 'w+') as f_w:
            for i in range(f_list_len):
                f_w.writelines(f_list[i])
            f.close()
    return render_template('result.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
