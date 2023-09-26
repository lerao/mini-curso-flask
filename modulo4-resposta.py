from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta_aqui'

# Defina seu formulário usando FlaskForm
class Form(FlaskForm):
    name = StringField('Nome', validators=[InputRequired()])
    email = StringField('E-mail', validators=[InputRequired()])
    message = TextAreaField('Mensagem', validators=[InputRequired()])

@app.route("/", methods=['GET', 'POST'])
def index():
    form = Form()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        print(f"Nome: {name}")
        print(f"E-mail: {email}")
        print(f"Mensagem: {message}")

    return render_template("index.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)