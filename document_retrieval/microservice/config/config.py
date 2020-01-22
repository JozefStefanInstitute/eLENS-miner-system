# Configuration script
# Retrieves the hidden variables from the .env
# file and creates the configuration objects -
# one for each environment.

import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CORS = {
        'origins': os.getenv('CORS_ORIGINS').split(',') if os.getenv('CORS_ORIGINS') else None
    }

class ProductionConfig(Config):
    """Production configuration"""
    ENV='production'
    SECRET_KEY=os.getenv('PROD_SECRET_KEY')
    DATABASE={
        'database': os.getenv('PROD_PG_DATABASE'),
        'password': os.getenv('PROD_PG_PASSWORD')
    }

class DevelopmentConfig(Config):
    """Development configuration"""
    ENV='development'
    DEBUG = True
    SECRET_KEY=os.getenv('DEV_SECRET_KEY')
    DATABASE={
        'database': os.getenv('DEV_PG_DATABASE'),
        'password': os.getenv('DEV_PG_PASSWORD')
    }

class TestingConfig(Config):
    """Testing configuration"""
    ENV='testing'
    TESTING = True
    SECRET_KEY=os.getenv('TEST_SECRET_KEY')
    DATABASE={
        'database': os.getenv('TEST_PG_DATABASE'),
        'password': os.getenv('TEST_PG_PASSWORD')
     }