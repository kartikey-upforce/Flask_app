from flask import Flask, jsonify
from database import db
from flask_migrate import Migrate
from user.api import user_bp
from entry.api import entry_bp
from competition.api import competition_bp

from flask_jwt_extended import JWTManager
from config import Config


from celery import Celery
from redis import Redis
from elasticsearch import Elasticsearch


def create_app():
    
    migrate = Migrate()
    app = Flask(__name__)

    app.config.from_object(Config)

    jwt = JWTManager(app)

    db.init_app(app)
    migrate.init_app(app, db)


    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
    app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'

    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])


    es_client = Elasticsearch(['http://elasticsearch:9200/'])

    from worker import add
    
    @app.route('/trigger-task')
    def trigger_task():
        result = add.delay(10, 20)  # Calling the Celery task asynchronously
        return f'Task ID: {result.id}'
    


    @app.route('/')
    def index():
        result = add.delay(10, 20)
        return f"Task added to Celery. Task ID: {result.id}"

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(entry_bp)
    app.register_blueprint(competition_bp)



    
    # @app.route('/cache-example')
    # def cache_example():
    #     redis_client.set('Nepal', 'Kathmandu')
    #     cached_value = redis_client.get('Nepal')
    #     return f'Cached value: {cached_value}'


    @app.route('/create-index')
    def create_index():
        try:
            index_name = 'your_index'
            if not es_client.indices.exists(index=index_name):
                es_client.indices.create(index=index_name)
                return jsonify({'message': f'Index "{index_name}" created successfully'}), 200
            else:
                return jsonify({'message': f'Index "{index_name}" already exists'}), 200
        except Exception as e:
            print(e)

    @app.route('/create-and-search')
    def create_and_search():
        try:
            index_name = 'new_index'
            document = {
                "field": "example",
                "content": "This is an example document for Elasticsearch"
            }

            # Check if the index exists
            if not es_client.indices.exists(index=index_name):
                es_client.indices.create(index=index_name)
                res = es_client.index(index=index_name, body=document)
                # Search for the document
                search_results = es_client.search(index=index_name, body={"query": {"match_all": {}}})
                return jsonify({'message': f'Index "{index_name}" created and document added', 'document': res, 'search_results': search_results}), 200
            else:
                # Index already exists, return a message
                return jsonify({'message': f'Index "{index_name}" already exists, cannot create and add document'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    # Add a document to the index
    @app.route('/add-document')
    def add_document():
        index_name = 'your_index'
        document = {
            'field': 'example',
            'content': 'This is an example document for Elasticsearch'
        }
        res = es_client.index(index=index_name, body=document)
        return jsonify({'message': 'Document added successfully', 'result': res}), 200

    # Search for documents in the index
    @app.route('/search-example')
    def search_example():
        index_name = 'your_index'
        query = 'example'
        search_results = es_client.search(index=index_name, body={'query': {'match': {'field': query}}})
        return jsonify({'message': 'Search results', 'results': search_results}), 200



    return app


app = create_app()
