class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///dev.db'

class TestingConfig(Config):
    DEBUG = True
    DATABASE_URI = 'sqlite:///test.db'

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URI = 'sqlite:///prod.db'