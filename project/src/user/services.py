from user.models import User
from flask import jsonify
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserServices:
    def get_users(self):
        users = User.query.all()
        users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(users_list),200
    
    def create_user(self, data):
        password_hash = generate_password_hash(data['password'])
        new_user = User(id = data['id'], username=data['username'], email=data['email'], password = password_hash)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201

    def retrieve_user(self, id):
        user = User.query.get(id)
        if user:
            user_data = {'id': user.id, 'username': user.username, 'email': user.email}
            return jsonify(user_data),200
        else:
            return jsonify({'message': 'User not found'}), 404

    def update_user(self, id, data):
        user = User.query.get(id)
        if user:
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404
        
    def delete_user(self, id):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'}), 204   
        else:
            return jsonify({'message': 'User not found'}), 404

    def user_login(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Missing username or password'}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid username or password'}), 401

        access_token = create_access_token(identity={'id': user.id})
        return jsonify({'access_token': access_token}), 200
    