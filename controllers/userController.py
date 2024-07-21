from flask import request, jsonify
from schemas.userSchema import user_input_schema, user_output_schema, user_login_schema
from services import userService
from marshmallow import ValidationError
from database import db
from models.user import User
from sqlalchemy.orm import Session


def save():
    try:
        user_data = user_input_schema.load(request.json)
        user_save = userService.save(user_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except ValueError as err:
        return jsonify({"error": str(err)}), 400
    


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
    
def get_token():
    try:
        user_data = user_login_schema.load(request.json)
        token = userService.get_token(user_data['email'], user_data['password'])
        user = userService.get_user_by_email(user_data['email'])
        if token:
            extra_data = user_output_schema.dump(user)
            resp = {
                "status": "Success",
                "message": "Succesfull authentication",
                "token": token,
                "user_data": extra_data
            }
            return jsonify(resp), 200
        else:
            resp = {
                "status": "Error",
                "message": "Email or password is incorrect",

            }
            return jsonify(resp), 401
    except ValidationError as err:
        return jsonify(err.messages), 400
    
