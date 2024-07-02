from marshmallow import fields
from schemas import ma

class TaskSchema(ma.Schema):
    id = fields.Integer(required=False)
    user_id = fields.String(required=True)
    task = fields.String(required=True)
    description = fields.String(required=True)
    date = fields.String(required=True)
    spoons_needed = fields.Integer(required=True)

    class Meta:
        fields = ('id', 'user_id', 'task', 'description', 'date', 'spoons_needed')
        
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)