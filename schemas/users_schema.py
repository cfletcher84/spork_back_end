from marshmallow import fields
from schemas import ma

class UsersSchema(ma.Schema):
    id = fields.Integer(required=False)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    spoons = fields.Integer(required=True)
    spoons_used = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password', 'spoons', 'spoons_used')

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)



