import os

from starlette.config import Config

env_files = ["dev.env"]

config = Config()
for env_file in env_files:
    if os.path.exists(env_file):
        config = Config(env_file)

# Base
API_V1_PREFIX = config("API_V1_PREFIX", cast=str)
DEBUG = config("DEBUG", cast=bool)
PROJECT_NAME = config("PROJECT_NAME", cast=str)
PROJECT_DESC = config("PROJECT_DESC", cast=str)
VERSION = config("VERSION", cast=str, default="1.0.0")

DATABASE_URL = config("DATABASE_URL", cast=str)
MONGO_INITDB_DATABASE = config("MONGO_INITDB_DATABASE", cast=str)

JWT_PUBLIC_KEY = config("JWT_PUBLIC_KEY", cast=str)
JWT_PRIVATE_KEY = config("JWT_PRIVATE_KEY", cast=str)
REFRESH_TOKEN_EXPIRES_IN = config("REFRESH_TOKEN_EXPIRES_IN", cast=int)
ACCESS_TOKEN_EXPIRES_IN = config("ACCESS_TOKEN_EXPIRES_IN", cast=int)
JWT_ALGORITHM = config("JWT_ALGORITHM", cast=str)

CLIENT_ORIGIN = config("CLIENT_ORIGIN", cast=str)

# Uvicorn Config
APP_MODULE = config("APP_MODULE", cast=str, default="app.main:app")
HOST = config("HOST", cast=str, default="0.0.0.0"),
LOG_LEVEL = config("LOG_LEVEL", cast=str, default="DEBUG"),
PORT = config("PORT", cast=str)
RELOAD = config("RELOAD", cast=bool, default="True")
