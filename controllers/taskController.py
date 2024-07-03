from flask import request, jsonify
from schemas.taskSchema import task_schema, tasks_schema
from services import taskService
from marshmallow import ValidationError

def find_all():
    tasks = taskService.find_all()
    return tasks_schema.jsonify(tasks), 200

def save():
    try:
        task_data = task_schema.load(request.json)
        task_save = taskService.save(task_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    


    return task_schema.jsonify(task_save), 201