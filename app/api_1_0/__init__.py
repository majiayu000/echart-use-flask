from flask import Blueprint


bp = Blueprint('api1_1', __name__)

from app.api_1_0 import routes