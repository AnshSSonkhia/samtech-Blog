import os

class Config:
    SECRET_KEY ='1234'
    API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sam2020@localhost/blog'

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   
class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}