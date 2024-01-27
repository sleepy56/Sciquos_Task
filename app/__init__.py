# app/__init__.py
from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'your_database_name',
        'host': 'your_database_host',
        'port': 27017,
    }
    db.init_app(app)

    return app
