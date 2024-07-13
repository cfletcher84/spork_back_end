from datetime import datetime, timedelta, timezone
import jwt
import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretkey'


def encode_token(user_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'iat': datetime.now(timezone.utc),
        'sub': user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        now = datetime.now(timezone.utc).timestamp()
        if payload.get('exp') < now:
            print('Token has expired')
            return None
        return payload.get('sub')
    except jwt.ExpiredSignatureError:
        print('Token has expired')
        return None
    except jwt.InvalidTokenError:
        print('Invalid Token')
        return None
    except Exception as e:
        print(f'An error has occured: {e}')
        return None
