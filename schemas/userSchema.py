from marshmallow import fields
from schemas import ma

class UserSchema(ma.Schema):
    id = fields.Integer(required=False)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    # spoons = fields.Integer(required=False) --> Moved to its own table
    profile_pic = fields.String(required=False)

user_input_schema = UserSchema()
user_output_schema = UserSchema(exclude=['password'])
users_schema = UserSchema(many=True, exclude=["password"])
user_login_schema = UserSchema(only=["email", "password"])



