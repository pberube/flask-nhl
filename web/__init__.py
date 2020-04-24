from flask import Blueprint


blueprint_web = Blueprint(
     'web',
     __name__,
     template_folder='templates',
     static_folder='static')

from .views import home
