# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'asd'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'seulichao@gmail.com'
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
	FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
	
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:210013@localhost:3306/testweb'
# if you want run this, you should change the password you set	
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:210013@localhost:3306/test2'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:210013@localhost:3306/prodweb'

config = {'development':DevelopmentConfig,\
		  'testing':TestingConfig,\
		  'production':ProductionConfig,\
		  'default':DevelopmentConfig}
















	
