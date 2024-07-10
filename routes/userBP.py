from flask import Blueprint
from controllers.userController import save, get_user

user_blueprint = Blueprint('user_bp', __name__)

user_blueprint.route('/', methods=['POST'])(save)
user_blueprint.route('/<user_id>', methods=['GET'])(get_user)