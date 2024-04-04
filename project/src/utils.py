# decorators.py

from flask import jsonify, request
from functools import wraps
import jwt
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request
from user.models import User
from config import Config

conf = Config()

def is_authenticated(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        jwt_token = request.headers.get('Authorization')

        if not jwt_token:
            return jsonify({'message': 'Missing JWT token'}), 401

        try:
            jwt_token = jwt_token.split(" ")[1]
            data = jwt.decode(jwt_token, conf.JWT_SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['sub']['id']
            current_user = User.query.filter_by(id=current_user_id).first()
            if not current_user:
                raise jwt.InvalidTokenError

            verify_jwt_in_request()
            current_user = get_jwt_identity() 

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'JWT token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid JWT token'}), 401

        return f(*args, **kwargs)

    return decorated_function
