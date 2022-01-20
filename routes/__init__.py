from flask import Blueprint

from . import UserRouting
from . import PlantRouting
from . import AlertRouting

blueprint = Blueprint('my_blueprint', __name__)
