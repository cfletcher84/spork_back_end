from flask import Blueprint
from controllers.spoonsController import save
from controllers.userController import get_user
from services.userService import update_spoons

spoons_blueprint = Blueprint('spoons_bp', __name__)

spoons_blueprint.route('/', methods=['POST'])(save)
spoons_blueprint.route('/<user_id>', methods=['GET'])(get_user)