# -*- coding:utf-8 -*-
from wtforms import StringField,SubmitField,PasswordField,BooleanField
from flask_wtf import Form
from wtforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[Required()])
	remember_me = BooleanField('keep me logged in')
	submit = SubmitField('Log In')


class RegisterForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	username = StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'usernames must have only letters,numbers,dots or underscores')])
	password = PasswordField('Password',validators=[Required()])
	password2 = PasswordField('Confirm Password',validators=[Required(),EqualTo('password',message='Password must match.')])
	submit = SubmitField('Register')
	
	def validate_email(self,field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('Email already registered.')
			#return False
		#return True


	def validate_username(self,field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('username already in use.')
			#return False
		#return True


class ChangePasswordForm(Form):
	password = PasswordField('Old password',validators=[Required()])
	password2 = PasswordField('New password',validators=[Required()])
	submit = SubmitField('Change')

		

class RestPasswordForm(Form):
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	submit = SubmitField('Send')
	

class RestPw2mailForm(Form):
	password = PasswordField('Reset password',validators=[Required()])
	submit = SubmitField('Reset')














