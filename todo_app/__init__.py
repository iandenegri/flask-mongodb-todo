# Third Party
from flask import Flask
from pymongo import MongoClient

# Local
from .main.routes import main
from .extensions import mongo

def create_app():
    app = Flask(__name__)

    app.config["DEBUG"] = True
    app.config["MONGO_URI"] = "mongodb://localhost:27017/todo"

    mongo.init_app(app)

    app.register_blueprint(main)

    return app