from flask import request, jsonify
from schemas.userSchema import user_input_schema, user_output_schema
from services import userService
from marshmallow import ValidationError

def save():
    try:
        user_data = user_input_schema.load(request.json)
        user_save = userService.save(user_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    


    return user_output_schema.jsonify(user_save), 201

def get_user(user_id):
    user = userService.get_user(user_id)
    if user:
        return user_output_schema.jsonify(user)
    else:
        resp = {
            "status": "error",
            "message": f'A user with ID {user_id} does not exist.'
        }
        return jsonify(resp), 404
