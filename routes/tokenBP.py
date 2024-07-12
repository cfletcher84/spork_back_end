from flask import Blueprint
from controllers.userController import get_token

token_blueprint = Blueprint('token_bp', __name__)



token_blueprint.route('/', methods=['POST'])(get_token)
                      