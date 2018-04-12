import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
    
class Config1:
    SECRET_KEY = os.getenv('SECRET_KEY', 'hard to guess string')
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() in \
                            ['true', 'on', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'litiandlut')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'litian19871001')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MIAL_SENDER = 'litiandlut@gmail.com'
    FLASKY_ADMIN = os.getenv('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
class DevelopmentConfig1(Config1):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL', 'sqlite:///'+
                                        os.path.join(basedir, 'data-dev.sqlite')) 
    
class TestingConfig1(Config1):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///'+
                                        os.path.join(basedir, 'data-test.sqlite'))
    
class ProductionConfig1(Config1):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///'+
                                        os.path.join(basedir, 'data.sqlite'))
    
    

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
