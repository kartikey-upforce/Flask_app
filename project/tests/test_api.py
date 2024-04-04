import os
import sys
import json

# root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# sys.path.append(root_dir)

import pytest
from app import create_app

flask_app = create_app()

@pytest.fixture
def client():
    with flask_app.test_client() as client:
        return client


# FOR USERS 
def test_user_api(client):
    response = client.get('/users')
    assert response.status_code == 200


def test_get_user_by_id(client):
    response = client.get('/users/3')

    assert response.status_code == 200

    user_data = json.loads(response.data)

    assert 'id' in user_data
    assert 'username' in user_data
    assert 'email' in user_data

    assert user_data['id'] == 1
    assert user_data['username'] == 'Noname'
    assert user_data['email'] == 'email@gmail.com\n'


def test_users_get(client):
    response = client.get('/users')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'username' in data[0]
    assert 'email' in data[0]

def test_user_retrieve(client):
    response = client.get('/users/1')
    assert response.status_code == 200

    user_data = json.loads(response.data)
    assert 'id' in user_data
    assert 'username' in user_data
    assert 'email' in user_data

def test_user_create(client):
    data = {
        'id':5,
        'username': 'NewUser',
        'email': 'newuser@example.com'
    }
    response = client.post('/users', json=data)
    assert response.status_code == 201

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'User created successfully'

def test_user_update(client):
    data = {
        'username': 'UpdatedUser',
        'email': 'updateduser@example.com'
    }
    response = client.put('/users/1', json=data)
    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'User updated successfully'

def test_user_delete(client):
    response = client.delete('/users/1')
    assert response.status_code == 204

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'User deleted successfully'


# FRO ENTRY

def test_entries_get(client):
    response = client.get('/entries')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'title' in data[0]
    assert 'content' in data[0]
    assert 'author_id' in data[0]

def test_entry_retrieve(client):
    response = client.get('/entries/1')
    assert response.status_code == 200

    entry_data = json.loads(response.data)
    assert 'id' in entry_data
    assert 'title' in entry_data
    assert 'content' in entry_data
    assert 'author_id' in entry_data

def test_entry_create(client):
    data = {
        'title': 'New Entry',
        'content': 'Lorem ipsum dolor sit amet.',
        'author_id': 1
    }
    response = client.post('/entries', json=data)
    assert response.status_code == 201

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'Entry created successfully'

def test_entry_update(client):
    data = {
        'title': 'Updated Entry',
        'content': 'Updated content.',
        'author_id': 1
    }
    response = client.put('/entries/1', json=data)
    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'Entry updated successfully'

def test_entry_delete(client):
    response = client.delete('/entries/1')
    assert response.status_code == 204

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'Entry deleted successfully'


# FOR COMPETITION
def test_competitions_get(client):
    response = client.get('/competitions')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'name' in data[0]
    assert 'description' in data[0]
    assert 'start_date' in data[0]
    assert 'end_date' in data[0]

def test_competition_retrieve(client):
    response = client.get('/competitions/1')
    assert response.status_code == 200

    competition_data = json.loads(response.data)
    assert 'id' in competition_data
    assert 'name' in competition_data
    assert 'description' in competition_data
    assert 'start_date' in competition_data
    assert 'end_date' in competition_data

def test_competition_create(client):
    data = {
        'name': 'New Competition',
        'description': 'This is a new competition',
        'start_date': '2025-01-01',
        'end_date': '2025-12-31'
    }
    response = client.post('/competitions', json=data)
    assert response.status_code == 201

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'Competition created successfully'

def test_competition_update(client):
    data = {
        'name': 'Updated Competition',
        'description': 'Updated competition description',
        'start_date': '2025-01-01',
        'end_date': '2025-12-31'
    }
    response = client.put('/competitions/1', json=data)
    assert response.status_code == 200

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'Competition updated successfully'

def test_competition_delete(client):
    response = client.delete('/competitions/1')
    assert response.status_code == 204

    response_data = json.loads(response.data)
    assert 'message' in response_data
    assert response_data['message'] == 'Competition deleted successfully'