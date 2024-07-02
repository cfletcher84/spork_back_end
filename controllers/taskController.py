from flask import request, jsonify
from schemas.taskSchema import task_schema, tasks_schema
from services import taskService
from marshmallow import ValidationError

def find_all():
    tasks = taskService.find_all()
    return tasks_schema.jsonify(tasks), 200