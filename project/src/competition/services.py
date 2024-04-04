from database import db
from flask import jsonify
from competition.models import Competition

class CompetitionServices:
    def get_competitions(self):
        competitions = Competition.query.all()
        competitions_list = [{'id': comp.id, 'name': comp.name, 'description': comp.description, 'start_date': comp.start_date, 'end_date': comp.end_date} for comp in competitions]
        return jsonify(competitions_list), 200

    def create_competition(self, data):
        new_competition = Competition(name=data['name'], description=data['description'], start_date=data['start_date'], end_date=data['end_date'])
        db.session.add(new_competition)
        db.session.commit()
        return jsonify({'message': 'Competition created successfully'}), 201

    def retrieve_competition(self, id):
        competition = Competition.query.get(id)
        if competition:
            competition_data = {'id': competition.id, 'name': competition.name, 'description': competition.description, 'start_date': competition.start_date, 'end_date': competition.end_date}
            return jsonify(competition_data), 200
        else:
            return jsonify({'message': 'Competition not found'}), 404

    def update_competition(self, id, data):
        competition = Competition.query.get(id)
        if competition:
            competition.name = data['name']
            competition.description = data['description']
            competition.start_date = data['start_date']
            competition.end_date = data['end_date']
            db.session.commit()
            return jsonify({'message': 'Competition updated successfully'}), 200
        else:
            return jsonify({'message': 'Competition not found'}), 404

    def delete_competition(self, id):
        competition = Competition.query.get(id)
        if competition:
            db.session.delete(competition)
            db.session.commit()
            return jsonify({'message': 'Competition deleted successfully'}), 204
        else:
            return jsonify({'message': 'Competition not found'}), 404