from flask import Blueprint, jsonify, request
from competition.services import CompetitionServices   
from utils import is_authenticated

competition_bp = Blueprint('competition', __name__)

competition_service = CompetitionServices()

# GET all competitions
@competition_bp.route('/competitions', methods=['GET'])
@is_authenticated
def competitions_get():
    return competition_service.get_competitions()


# RETRIEVE specific competition by ID
@competition_bp.route('/competitions/<int:id>', methods=['GET'])
@is_authenticated
def competition_retrieve(id):
    return competition_service.retrieve_competition(id)


# POST create new competition
@competition_bp.route('/competitions', methods=['POST'])
def competition_create():
    data = request.json
    return competition_service.create_competition(data)


# PUT update competition by ID
@competition_bp.route('/competitions/<int:id>', methods=['PUT'])
@is_authenticated
def competition_update(id):
    data = request.json
    return competition_service.update_competition(id, data)


# DELETE competition by ID
@competition_bp.route('/competitions/<int:id>', methods=['DELETE'])
@is_authenticated
def competition_delete(id):
    return competition_service.delete_competition(id)