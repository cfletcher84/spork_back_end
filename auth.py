from flask_httpauth import HTTPTokenAuth
from utils.util import decode_token
from services import userService

token_auth = HTTPTokenAuth()

@token_auth.verify_token
def verify(token):
    user_id = decode_token(token)
    if user_id:
        return userService.get_user(user_id)
    else:
        return None
    
@token_auth.error_handler
def error_handler(status_code):
    return {"error": "Invalid token."}, status_code