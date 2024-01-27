import sqlite3

from fastapi import APIRouter, HTTPException

from src.utils.rbac import ROLE_MAPPING
from src.blocklist import BLOCKLIST
from src.controllers import auth_controller
from src.models.schemas import AuthSchema
from src.utils.mailgun import send_simple_message

router = APIRouter(tags=['Authentication'])


@router.post('/register')
def register_user(user_data: AuthSchema):
    try:
        auth_controller.register(dict(user_data))
    except sqlite3.IntegrityError:
        raise HTTPException(409, 'User already exists')

    send_simple_message(
        to='shreyansh.brbd@gmail.com',
        subject='New user signup in Student Mgt System',
        body=f'A new user with username: {user_data.get("username")} signed up!'
    )
    return {"message": "Successfully registered"}, 201


@router.post('/login')
def login_user(user_data: AuthSchema):
    data = auth_controller.login(dict(user_data))
    if not data:
        raise HTTPException(401, "Invalid Login")

    role, username = data
    mapped_role = ROLE_MAPPING.get(role)
    # access_token = create_access_token(identity=username, fresh=True, additional_claims={'cap': mapped_role})
    # refresh_token = create_refresh_token(identity=username, additional_claims={'cap':mapped_role})
    access_token = None
    refresh_token = None
    return {"access_token": access_token, "refresh_token": refresh_token}


# to generate a non fresh access token
@router.post('/refresh')
def refresh():
    # current_user = get_jwt_identity()
    # claims = get_jwt()
    # new_access_token = create_access_token(identity=current_user, fresh=False, additional_claims={'cap':claims.get('cap')}) # if not false then refresh token will give fresh tokens!
    new_access_token = None
    return {"access_token": new_access_token}


@router.post('/logout')
def logout_user():
    # jti = get_jwt().get('jti')
    jti = None
    BLOCKLIST.add(jti)
    return {'message': 'Successfully logged out'}
