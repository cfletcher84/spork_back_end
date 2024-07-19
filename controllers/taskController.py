from flask import request, jsonify
from schemas.taskSchema import task_schema, tasks_schema, user_task_schema
from services import taskService
from marshmallow import ValidationError
from auth import token_auth
from models.task import Task
from database import db

def find_all():
    tasks = taskService.find_all()
    print(tasks)
    return tasks_schema.jsonify(tasks), 200

# @token_auth.login_required
def save():
    try:
        task_data = task_schema.load(request.json)
        task_save = taskService.save(task_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    return task_schema.jsonify(task_save), 201

def get_user_tasks(user_id):
    task = taskService.get_user_tasks(user_id)
    print(f'{task} for {user_id}')
    if task:
        return tasks_schema.jsonify(task)
    else:
        resp = {
            "status": "error",
            "message": f'The user id {user_id}, has no activities completed.'
        }
        return jsonify(resp), 404