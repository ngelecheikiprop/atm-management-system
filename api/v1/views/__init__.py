"""Initialize Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.callback import *
from api.v1.views.dashboard  import *
from api.v1.views.pi import *
