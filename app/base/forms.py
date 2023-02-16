from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

## login and registration


class LoginForm(FlaskForm):
    username = StringField('Username', id='username_login')
    password = PasswordField('Password', id='pwd_login')
