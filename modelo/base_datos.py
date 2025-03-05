from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    from modelo.libro import Libro
    from modelo.usuario import Usuario

    from controlador.controlador_usuarios import usuarios_bp
    app.register_blueprint(usuarios_bp)

    with app.app_context():
        db.create_all()

    return app
