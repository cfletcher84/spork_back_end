from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.user import User
from werkzeug.security import generate_password_hash

def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            email_query = select(User).where(User.email == user_data['email'])
            email_check = session.execute(email_query).scalars().first()
            if email_check is not None:
                raise ValueError("Customer with that email already exists.")
            new_user = User(first_name=user_data['first_name'], last_name=user_data['last_name'], email=user_data['email'], spoons=user_data['spoons'], spoons_used=user_data['spoons_used'], password=generate_password_hash(user_data['password']))
            session.add(new_user)
            session.commit()
        session.refresh(new_user)
        return new_user
    

def get_user(user_id):
    return db.session.get(User, user_id)