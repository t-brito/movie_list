import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  # WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or SECRET_KEY
  MONGO_USERNAME = os.environ.get('MONGO_USERNAME') or 'user'
  MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD') or 'pass'
  MONGO_HOST = os.environ.get('MONGO_HOST') or 'localhost'
  MONGO_PORT = os.environ.get('MONGO_PORT') or 27017
  MONGO_DBNAME = os.environ.get('MONGO_DBNAME') or 'test'
  MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://{}:{}@{}:{}/{}'.format(
    MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST, MONGO_PORT, MONGO_DBNAME)
  # MONGO_AUTH_SOURCE = MONGO_DBNAME
  LANGUAGES = ['en', 'pt']
  OMDB_API_KEY = os.environ.get('OMDB_API_KEY') or None
