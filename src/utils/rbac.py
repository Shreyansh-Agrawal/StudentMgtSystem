from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_jwt, verify_jwt_in_request

ROLE_MAPPING = {
    'admin': 1,
    'student': 0
}

def access_level(roles):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            mapped_roles = [ROLE_MAPPING.get(role) for role in roles]

            if claims["cap"] in mapped_roles:
                return func(*args, **kwargs)
            else:
                return jsonify(msg="Unauthorized"), 403
        return wrapper

    return decorator
