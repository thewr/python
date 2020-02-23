from flask import Flask, render_template, request
from wtforms import Form, FloatField, validators
from compute import sine_plot

app = Flask(__name__)


class InputForm(Form):
    A = FloatField(
        label='x^2 +',
        validators=[validators.InputRequired()])
    B = FloatField(
        label='x +',
        validators=[validators.InputRequired()])
    C = FloatField(
        label='x +',
        validators=[validators.InputRequired()])
      

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    result = None
    if request.method == 'POST' and form.validate():
        A = form.A.data
        B = form.B.data
        C = form.C.data
        result = sine_plot(A,B,C)

    return render_template("view.html", form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
