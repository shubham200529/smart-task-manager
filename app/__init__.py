from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate

from flask_login import LoginManager

from flask_socketio import SocketIO

from config import Config


db = SQLAlchemy()

migrate = Migrate()

login_manager = LoginManager()

login_manager.login_view = 'auth.login'

socketio = SocketIO()


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    migrate.init_app(app, db)

    login_manager.init_app(app)

    socketio.init_app(app)

    from app.routes.auth import auth_bp

    from app.routes.task_routes import task_bp

    from app.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp)

    app.register_blueprint(task_bp)

    app.register_blueprint(dashboard_bp)

    return app