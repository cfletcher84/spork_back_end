from sqlalchemy.orm import Session
from database import db
from models.task import Task
import datetime
from sqlalchemy import and_

dt = datetime.date.today()

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
    
def get_between_tasks(user_id, start_date, end_date):
    try:
        with Session(db.engine) as session:
            tasks = session.query(Task).filter_by(and_(
                Task.user_id == user_id,
                Task.date >= start_date,
                Task.date <= end_date
            )).all()
        return tasks
    except Exception as e:
        return None
