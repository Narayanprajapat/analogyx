from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    from app.routes import blueprint
    for route_blueprint in blueprint:
        app.register_blueprint(route_blueprint, url_prefix='/api/v1')
    return app
