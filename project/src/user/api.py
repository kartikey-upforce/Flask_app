from flask import Blueprint, jsonify, request
from user.services import UserServices

api_bp = Blueprint('user', __name__)

user_service = UserServices()

# GET
@api_bp.route('/users', methods=['GET'])
def users_get():
    return user_service.get_users()


# RETRIEVE
@api_bp.route('/users/<int:id>', methods=['GET'])
def users_retrieve(id):
    return user_service.retrieve_user(id)
    

# POST
@api_bp.route('/users', methods=['POST'])
def users_create():
    data = request.json
    return user_service.create_user(data)


# UPDATE
@api_bp.route('/users/<int:id>', methods=['PUT'])
def users_update(id):
    data = request.json
    return user_service.update_user(id, data)


# DELETE
@api_bp.route('/users/<int:id>', methods=['DELETE'])
def users_delete(id):
    return user_service.delete_user(id)
