from flask import Blueprint
from controllers.taskController import find_all, save, get_user_tasks, get_between_tasks

task_blueprint = Blueprint('task_bp', __name__)

task_blueprint.route('/', methods=['GET'])(find_all)
task_blueprint.route('/', methods=['POST'])(save)
task_blueprint.route('/<user_id>', methods=['GET'])(get_user_tasks)
task_blueprint.route('/bydate/<user_id>', methods=['GET'])(get_between_tasks)