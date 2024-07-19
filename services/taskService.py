from sqlalchemy.orm import Session
from database import db
from models.task import Task
import datetime

dt = datetime.date.today()
print(type(dt))

def find_all():
    query = db.select(Task)
    tasks = db.session.execute(query).scalars().all()
    return tasks

def save(task_data):
    with Session(db.engine) as session:
        with session.begin():
            new_task = Task(user_id=task_data['user_id'],date=dt, task=task_data['task'], description=task_data['description'], spoons_needed=task_data['spoons_needed'], duration=task_data['duration'], time_of_day=task_data['time_of_day'])
            session.add(new_task)
            session.commit()
        session.refresh(new_task)
        return new_task

def get_user_tasks(user_id):
    with Session(db.engine) as session:
        tasks = session.query(Task).filter_by(user_id=user_id).all()
        print(f"Tasks found for user_id {user_id}: {tasks}") 
        return tasks 