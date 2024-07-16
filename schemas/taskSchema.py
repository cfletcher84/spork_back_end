from marshmallow import fields
from schemas import ma

class TaskSchema(ma.Schema):
    id = fields.Integer(required=False)
    user_id = fields.Integer(required=True)
    task = fields.String(required=True)
    description = fields.String(required=True)
    # date = fields.Date(required=False)
    spoons_needed = fields.Integer(required=True)
    # icon = fields.String(required=False)
    duration = fields.String(required=True)
    time_of_day = fields.String(required=True)

    class Meta:
        fields = ('id', 'user_id', 'task', 'description', 'spoons_needed', 'duration', 'time_of_day')
        
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
user_task_schema = TaskSchema(only=['task'])