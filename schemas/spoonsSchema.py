from marshmallow import fields
from schemas import ma

class SpoonSchema(ma.Schema):
    id = fields.Integer(required=False)
    user_id = fields.Integer(required=True)
    spoons = fields.Integer(required=False)
    date = fields.String(required=False)

    class Meta:
        fields = ('id', 'user_id', 'date', 'spoons')
        
spoon_schema = SpoonSchema()
spoons_schema = SpoonSchema(many=True)