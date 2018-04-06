# -*- coding:utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = 'asd'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxxxxx@localhost:3306/testweb'
# if you want run this, you should change the password you set	
class TestingConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxxxxx@localhost:3306/test2'

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:xxxxxx@localhost:3306/prodweb'

config = {'development':DevelopmentConfig,\
		  'testing':TestingConfig,\
		  'production':ProductionConfig,\
		  'default':DevelopmentConfig}
















	
