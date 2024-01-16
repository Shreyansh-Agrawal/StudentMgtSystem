import sqlite3

from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, get_jwt, jwt_required
from flask_smorest import Blueprint, abort

from src.utils.rbac import ROLE_MAPPING
from src.blocklist import BLOCKLIST
from src.controllers import auth_controller
from src.models.schemas import AuthSchema
from src.utils.mailgun import send_simple_message

blp = Blueprint('users', __name__)


@blp.post('/register')
@blp.arguments(AuthSchema)
def register_user(user_data):
    try:
        auth_controller.register(user_data)
    except sqlite3.IntegrityError:
        abort(409, message='User already exists')

    send_simple_message(
        to='shreyansh.brbd@gmail.com',
        subject='New user signup in Student Mgt System',
        body=f'A new user with username: {user_data.get("username")} signed up!'
    )
    return {"message": "Successfully registered"}, 201


@blp.post('/login')
@blp.arguments(AuthSchema)
def login_user(user_data):
    data = auth_controller.login(user_data)
    if not data:
        abort(401, message="Invalid Login")

    role, username = data
    mapped_role = ROLE_MAPPING.get(role)
    access_token = create_access_token(identity=username, fresh=True, additional_claims={'cap': mapped_role})
    refresh_token = create_refresh_token(identity=username, additional_claims={'cap':mapped_role})
    return {"access_token": access_token, "refresh_token": refresh_token}


# to generate a non fresh access token
@blp.post('/refresh')
@jwt_required(refresh=True) # it needs a refresh token not an access token
def refresh():
    current_user = get_jwt_identity()
    claims = get_jwt()
    new_access_token = create_access_token(identity=current_user, fresh=False, additional_claims={'cap':claims.get('cap')}) # if not false then refresh token will give fresh tokens!
    return {"access_token": new_access_token}


@blp.post('/logout')
@jwt_required()
def logout_user():
    jti = get_jwt().get('jti')
    BLOCKLIST.add(jti)
    return {'message': 'Successfully logged out'}
