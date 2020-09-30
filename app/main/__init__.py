from flask import Blueprint
main = Blueprint('main',__name__)
# from app import app
from . import views
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# track_modifications = app.config.setdefault['SQLALCHEMY_TRACK_MODIFICATIONS', True]

app = Flask(__name__)
app.config['SECRET_KEY']='1234'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True