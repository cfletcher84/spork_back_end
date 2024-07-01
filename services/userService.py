from sqlalchemy.orm import Session
from database import db
from models.user import User

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            new_user = User(first_name=user_data(['first_name']), last_name=user_data(['last_name']), email=user_data(['email']), username=user_data(['username']), password=user_data(['password']), spoons=user_data(['spoons']), spoons_used=user_data(['spoons_used']))
            session.add(new_user)
            session.commit()
        session.refresh(new_user)
        return new_user
    

    