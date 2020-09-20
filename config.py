import os

DEBUG=True
SEND_FILE_MAX_AGE_DEFAULT = 0
base = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"# + os.path.join(base, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
