from Model.handle_db import HandleDB
from werkzeug.security import check_password_hash

def check_user(username, password):
    user = HandleDB()
    filter_user = user.getOnly(username)
    if filter_user:
        same_password = check_password_hash(filter_user[5], password)
        if same_password:
            return filter_user
    return None
