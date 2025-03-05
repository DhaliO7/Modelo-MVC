from modelo.base_datos import db

class Usuario(db.Model):
    _tablename_ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f'<Usuario {self.nombre} - {self.email}>'
