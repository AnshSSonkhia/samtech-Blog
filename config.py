import os

class Config:

    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    DEBUG="True"
    SECRET_KEY=''
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    

 # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class TestConfig():
    

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

configurations = { 'development':Config, 'test':TestConfig, "production":ProdConfig }