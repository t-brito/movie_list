from flask import Flask, current_app, request
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from flask_babel import Babel
from config import Config

mongo = PyMongo()
bootstrap = Bootstrap()
babel = Babel()

def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  mongo.init_app(app)
  bootstrap.init_app(app)
  babel.init_app(app)

  from app.main import bp as main_bp
  app.register_blueprint(main_bp)

  return app

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])
