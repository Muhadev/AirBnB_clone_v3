from flask import Blueprint

# Create a Blueprint instance with url prefix /api/v1
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import (PEP8 will complain about this, ignore)
from api.v1.views.index import *
