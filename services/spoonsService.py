from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.spoons import Spoons
from models.user import User
import datetime



def save(spoon_data):
    try:
        with Session(db.engine) as session:
            with session.begin():
                user_spoons = Spoons(user_id=spoon_data['user_id'],date=datetime.date.today(), spoons=spoon_data['spoons'])
                session.add(user_spoons)
                session.commit()
            session.refresh(user_spoons)
            return user_spoons
    except Exception as e:
        return None

def get_user(user_id):
    return db.session.get(User, user_id)