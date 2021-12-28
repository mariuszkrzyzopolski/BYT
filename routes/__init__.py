from flask import Blueprint

from . import UserRouting
from . import PlantRouting

blueprint = Blueprint('my_blueprint', __name__)
