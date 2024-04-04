from database import db
from flask import jsonify
from entry.models import Entry

class EntryServices:
    def get_entries(self):
        entries = Entry.query.all()
        entries_list = [{'id': entry.id, 'title': entry.title, 'content': entry.content} for entry in entries]
        return jsonify(entries_list), 200

    def create_entry(self, data):
        new_entry = Entry(title=data['title'], content=data['content'], author_id=data['author_id'])
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Entry created successfully'}), 201

    def retrieve_entry(self, id):
        entry = Entry.query.get(id)
        if entry:
            entry_data = {'id': entry.id, 'title': entry.title, 'content': entry.content}
            return jsonify(entry_data), 200
        else:
            return jsonify({'message': 'Entry not found'}), 404

    def update_entry(self, id, data):
        entry = Entry.query.get(id)
        if entry:
            entry.title = data['title']
            entry.content = data['content']
            db.session.commit()
            return jsonify({'message': 'Entry updated successfully'}), 200
        else:
            return jsonify({'message': 'Entry not found'}), 404

    def delete_entry(self, id):
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
            return jsonify({'message': 'Entry deleted successfully'}), 204
        else:
            return jsonify({'message': 'Entry not found'}), 404