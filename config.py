import os
class Config:
    SECRET_KEY = 'lorraine'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://lorraine:gift1234@localhost/pitching'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
     #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_USERNAME='lorrainechepkemoi4@gmail.com'
    MAIL_PASSWORD='epxsnxehdzksryik'
    pass
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    '''
    Dev config class to be used during development process
    '''
    DEBUG = True
    
      

config_options = {
'development':DevConfig,
'production':ProdConfig

}