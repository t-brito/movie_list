from flask import Blueprint

bp = Blueprint('main', __name__)

# bottom import, to prevent circular dependencies
from app.main import routes
