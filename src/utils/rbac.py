from functools import wraps
from fastapi import HTTPException

ROLE_MAPPING = {
    'admin': 1,
    'student': 0
}

def access_level(roles):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            claims = kwargs.get('claims')
            mapped_roles = [ROLE_MAPPING.get(role) for role in roles]

            if claims["cap"] in mapped_roles:
                return func(*args, **kwargs)
            else:
                raise HTTPException(status_code=403, detail='Access denied')
        return wrapper

    return decorator
