from flask import Blueprint, request, jsonify
from modelo.base_datos import db
from modelo.usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.query.all()
    resultado = [{"id": u.id, "nombre": u.nombre, "email": u.email} for u in usuarios]
    return jsonify(resultado), 200

@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = Usuario.query.get(id)
    if usuario:
        return jsonify({"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email}), 200
    return jsonify({"error": "Usuario no encontrado"}), 404

@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.get_json()
    
    if not datos or 'nombre' not in datos or 'email' not in datos:
        return jsonify({"error": "Faltan datos"}), 400
    
    nuevo_usuario = Usuario(nombre=datos['nombre'], email=datos['email'])
    db.session.add(nuevo_usuario)
    db.session.flush()  # Asegura que la BD procese la operación antes de confirmarla
    db.session.commit()

    return jsonify({"mensaje": "Usuario creado correctamente"}), 201

@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    datos = request.get_json()
    usuario.nombre = datos.get('nombre', usuario.nombre)
    usuario.email = datos.get('email', usuario.email)
    db.session.commit()
    return jsonify({"mensaje": "Usuario actualizado correctamente"}), 200

@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    usuario = Usuario.query.get(id)
    if not usuario:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario eliminado correctamente"}), 200
