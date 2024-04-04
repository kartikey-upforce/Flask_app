from flask import Blueprint, jsonify, request
from user.services import UserServices
from utils import is_authenticated
from user.models import User
from flask_jwt_extended import get_jwt_identity

# from app import app

user_bp = Blueprint('user', __name__)


user_service = UserServices()

# GET
@user_bp.route('/users', methods=['GET'])
@is_authenticated
def users_get():
    return user_service.get_users()


# RETRIEVE
@user_bp.route('/users/<int:id>', methods=['GET'])
@is_authenticated
def users_retrieve(id):
    return user_service.retrieve_user(id)
    

# POST
@user_bp.route('/users', methods=['POST'])
def users_create():
    data = request.json
    return user_service.create_user(data)


# UPDATE
@user_bp.route('/users/<int:id>', methods=['PUT'])
@is_authenticated
def users_update(id):
    data = request.json
    return user_service.update_user(id, data)


# DELETE
@user_bp.route('/users/<int:id>', methods=['DELETE'])
@is_authenticated
def users_delete(id):
    return user_service.delete_user(id)


# Endpoint to generate JWT token
@user_bp.route('/login', methods=['POST'])
def get_token():
    data = request.json
    return user_service.user_login(data)


# @user_bp.route('/protected', methods=['GET'])
# @is_authenticated
# def protected_route():
#     current_user = get_jwt_identity()
#     return jsonify({'message': 'Welcome to the protected route!', 'user_id': current_user['id']}), 200

