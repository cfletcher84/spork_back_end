from flask import request, jsonify
from schemas.spoonsSchema import spoon_schema
from services import spoonsService
from marshmallow import ValidationError
from database import db

def save():
    try:
        spoon_data = spoon_schema.load(request.json)
        spoon_save = spoonsService.save(spoon_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    return spoon_schema.jsonify(spoon_save), 201