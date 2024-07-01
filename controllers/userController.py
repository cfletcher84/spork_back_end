from flask import request, jsonify
from schemas.userSchema import user_schema
from services import userService
from marshmallow import ValidationError

def save():
    try:
        user_data = user_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    user_save = userService.save(user_data)

    return user_schema.jsonify(user_save), 201

