from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import regexp, EqualTo
from app.models import User

class LoginForm(FlaskForm):
  User_Email = StringField('Email')
  Password = PasswordField('Password')
  remember_me = BooleanField('Remember Me')
  submit =SubmitField('Login')


class CreateAccount(FlaskForm):
  First_name = StringField('First Name')
  Last_name = StringField('Last Name')
  Email = StringField('Email')
  Password = PasswordField('Password')
  Confirm_Password = PasswordField('Confirm Password', validators=[EqualTo('Password')])
  submit = SubmitField('CreateAccount')