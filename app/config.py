import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', "mysql+pymysql://root:checkmysql@localhost:3306/etl_project")

def get_config(environment="development"):
    if environment == "development":
        return DevelopmentConfig