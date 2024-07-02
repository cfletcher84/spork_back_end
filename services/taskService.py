from sqlalchemy.orm import Session
from database import db
from models.task import Task

def find_all():
    query = db.select(Task)
    tasks = db.session.execute(query).scalars().all()
    return tasks
    