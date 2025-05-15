import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'changeme')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
class Config:

    SECRET_KEY = os.getenv('SECRET_KEY', 'change_me')

    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:////mnt/data/app.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
'''

