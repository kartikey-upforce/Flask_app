from flask import Blueprint, jsonify, request
from entry.services import EntryServices   

entry_bp = Blueprint('entry', __name__)

entry_service = EntryServices()

# Entry Endpoints

# GET all entries
@entry_bp.route('/entries', methods=['GET'])
def entries_get():
    return entry_service.get_entries()


# RETRIEVE specific entry by ID
@entry_bp.route('/entries/<int:id>', methods=['GET'])
def entry_retrieve(id):
    return entry_service.retrieve_entry(id)


# POST create new entry
@entry_bp.route('/entries', methods=['POST'])
def entry_create():
    data = request.json
    return entry_service.create_entry(data)


# PUT update entry by ID
@entry_bp.route('/entries/<int:id>', methods=['PUT'])
def entry_update(id):
    data = request.json
    return entry_service.update_entry(id, data)


# DELETE entry by ID
@entry_bp.route('/entries/<int:id>', methods=['DELETE'])
def entry_delete(id):
    return entry_service.delete_entry(id)