from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, IntegerField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    profil_picture = FileField(label='Upload a profil picture')
    phone = StringField(label='Phone number')
    password = PasswordField(label='Password', validators=[DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class ProductForm(FlaskForm):
    name = StringField(label='Product Name', validators=[DataRequired()])
    category = StringField(label='Product Category', validators=[DataRequired()])
    description = TextAreaField(label='Description', validators=[DataRequired()])
    price = FloatField(label='Price', validators=[DataRequired()])
    quantity = IntegerField(label='Quantity', validators=[DataRequired()])
    submit = SubmitField(label='Add Product')

class ModifyProfileForm(FlaskForm):
    username = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email()])
    profil_picture = FileField(label='upload new profil picture')
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Register')

class ModifyPasswordForm(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired()])
    new_password = PasswordField(label='New Password', validators=[DataRequired()])
    confirm_new_password = PasswordField(label='Confirm new Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField(label='Apply')

