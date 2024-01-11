import sqlite3

from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from flask_smorest import Blueprint, abort

from blocklist import BLOCKLIST
from controllers import auth_controller
from views.schemas import AuthSchema

blp = Blueprint('users', __name__)


@blp.post('/register')
@blp.arguments(AuthSchema)
def register_user(user_data):
    try:
        auth_controller.register(user_data)
    except sqlite3.IntegrityError:
        abort(409, message='User already exists')

    return {"message": "Successfully registered"}, 201


@blp.post('/login')
@blp.arguments(AuthSchema)
def login_user(user_data):
    role = auth_controller.login(user_data)
    if not role:
        abort(401, message="Invalid Login")
    
    access_token = create_access_token(identity=role)
    return {"access_token": access_token}


@blp.post('/logout')
@jwt_required()
def logout_user():
    jti = get_jwt().get('jti')
    BLOCKLIST.add(jti)
    return {'message': 'Successfully logged out'}
