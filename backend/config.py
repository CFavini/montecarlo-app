import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'change_me')
    '''
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

    SQLALCHEMY_DATABASE_URI = 'sqlite:////mnt/data/app.db'
    '''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
