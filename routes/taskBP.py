from flask import Blueprint
from controllers.taskController import find_all

task_blueprint = Blueprint('task_bp', __name__)

task_blueprint.route('/', methods=['GET'])(find_all)
