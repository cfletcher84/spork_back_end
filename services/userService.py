from sqlalchemy.orm import Session
from sqlalchemy import select
from database import db
from models.user import User
from schemas.userSchema import user_output_schema
from werkzeug.security import generate_password_hash, check_password_hash
from utils.util import encode_token
from flask import jsonify, request


def save(user_data):
    with Session(db.engine) as session:
        with session.begin():
            email_query = select(User).where(User.email == user_data['email'])
            email_check = session.execute(email_query).scalars().first()
            if email_check is not None:
                raise ValueError("Customer with that email already exists.")
            new_user = User(first_name=user_data['first_name'], last_name=user_data['last_name'], email=user_data['email'], password=generate_password_hash(user_data['password']))
            session.add(new_user)
            session.commit()
        session.refresh(new_user)
        return new_user


def get_user(user_id):
    return db.session.get(User, user_id)

def get_user_by_email(email):
    query = db.select(User).where(User.email == email)
    user = db.session.execute(query).scalars().first()
    return user

def get_token(email, password):
    query = db.select(User).where(User.email == email)
    user = db.session.execute(query).scalars().first()
    if user is not None and check_password_hash(user.password, password):
        auth_token = encode_token(user.id)
        return auth_token
    else:
        return None
    

def update_spoons(user_id):
    try:
        user = get_user(user_id)
        if not user:
            return jsonify({'error': 'User does not exist'}), 404
        data = request.get_json()
        new_spoons = data.get('spoons')
        user.spoons = new_spoons
        db.session.commit()
        return jsonify({'message': 'Spoons updated.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 404
    finally:
        db.session.close()