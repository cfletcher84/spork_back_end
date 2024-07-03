from marshmallow import fields
from schemas import ma

class FlareSchema(ma.Schema):
    id = fields.Integer(required=False)
    flare = fields.Boolean(required=True)
    date = fields.String(required=True)

    class Meta:
        fields = ('id', 'flare', 'date')

flare_schema = FlareSchema()
flares_schema = FlareSchema(many=True)

