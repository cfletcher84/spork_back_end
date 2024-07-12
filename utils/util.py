from datetime import datetime, timedelta
import jwt
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretkey'


def encode_token(user_id):
    payload = {
        'exp': datetime.now() + timedelta(hours=1),
        'iat': datetime.now(),
        'sub': user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

