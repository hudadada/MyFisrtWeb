from flask import Blueprint

home_blue = Blueprint('home',__name__)

from .views import *