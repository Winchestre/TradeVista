from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField, EmailField, BooleanField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed
from market_square.models import User


class RegistrationForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists!')

    first_name = StringField(label='First Name:', validators=[Length(min=2, max=50), DataRequired()])
    last_name = StringField(label='Last Name:', validators=[Length(min=2, max=50), DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1', message='Passwords must match'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Click here to login')

class SellerLoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    user_id = StringField(label='User ID:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Click here to login')


class ProductForm(FlaskForm):
    product_name = StringField(label='Name of Product', validators=[DataRequired()])
    current_price = FloatField(label='Current Price', validators=[DataRequired()])
    previous_price = FloatField(label='Previous Price', validators=[DataRequired()])
    in_stock = IntegerField(label='In Stock', validators=[DataRequired(), NumberRange(min=0)])
    product_picture = FileField(label='Product Picture', validators=[DataRequired()])
    flash_sale = BooleanField(label='Flash Sale')
    owner_id = HiddenField()

    add_product = SubmitField(label='Add Product')
    update_product = SubmitField(label='Update')
    

class ProfilePictureForm(FlaskForm):
    profile_picture = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Upload')


class ProductProfilePictureForm(FlaskForm):
    profile_picture = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    submit = SubmitField('Upload')