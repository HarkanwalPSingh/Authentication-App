from xmlrpc.client import Boolean
from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = 'Authenticator'
    DEBUG: Boolean = True

class DatabaseSettings(BaseSettings):
    DATABASE_NAME = 'flask_jwt_auth'
    SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:1234@127.0.0.1/{DATABASE_NAME}'

class JWTSettings(BaseSettings):
    JWT_SECRET_KEY = 'secret_password'