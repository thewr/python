from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, BooleanField, SelectField, TextField, RadioField, validators
from compute import compute

app = Flask(__name__)
app.secret_key = 'some_secret'

# InputForm and below is our controller
class InputForm(Form):
    float_field = FloatField(validators=[validators.InputRequired()])
    radio_field = RadioField(choices=[('radio1','firstRadio'),('radio2','secondRadio')], validators=[validators.InputRequired()])
    select_field = SelectField(choices=[('select1','select1'),('select2','select2')], validators=[validators.InputRequired()])
#    boolean_field = BooleanField( [validators.Required()])
    boolean_field = BooleanField()
    text_field = TextField([validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    result_str = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        float_val = form.float_field.data
        radio_val = form.radio_field.data
        select_val = form.select_field.data
        text_val = form.text_field.data
        boolean_val = form.boolean_field.data
        if boolean_val != True:
            print("Got to Flash")
            flash ("You must check the boolean box!")
        else:
            result_str = compute(float_val, radio_val, select_val, boolean_val, text_val)

    return render_template("view.html", template_form=form, result=result_str)

if __name__ == '__main__':
    app.run(debug=True)
