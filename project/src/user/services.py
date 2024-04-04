from user.models import User
from flask import jsonify
from database import db

class UserServices:
    def get_users(self):
        users = User.query.all()
        users_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(users_list),200
    
    def create_user(self, data):
        new_user = User(id = data['id'], username=data['username'], email=data['email'])
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

    