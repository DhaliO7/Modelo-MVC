from modelo.base_datos import db

class Libro(db.Model):
    _tablename_ = 'libros'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    estado_libro = db.Column(db.Boolean, default=True)  # True = Disponible, False = Prestado

    def __init__(self, titulo, autor, genero, estado_libro=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.estado_libro = estado_libro

    def prestar(self):
        """Marca el libro como prestado"""
        self.estado_libro = False

    def devolver(self):
        """Marca el libro como disponible"""
        self.estado_libro = True
