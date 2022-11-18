from flask import Flask
from os import path
from flask_socketio import SocketIO

socketio = SocketIO(cors_allowed_origins="*", async_mode='threading')

def create_app():
    app = Flask(__name__)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    socketio.init_app(app)
    return app