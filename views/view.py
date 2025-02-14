from flask import Flask, request, jsonify
from controllers.controller import (
    obtener_libros_disponibles, 
    obtener_prestamos_activos, 
    obtener_historial_prestamos, 
    prestar_libro, 
    devolver_libro, 
    obtener_usuarios
)

app = Flask(__name__)

# Ruta para ver libros disponibles
@app.route('/libros', methods=['GET'])
def ver_libros_disponibles():
    try:
        libros = obtener_libros_disponibles()
        if libros:
            return jsonify([{"id_libro": libro.id_libro, "titulo": libro.titulo, "autor": libro.autor} for libro in libros])
        return jsonify({"mensaje": "No hay libros disponibles en este momento."}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener libros.", "error": str(e)}), 500

# Ruta para ver préstamos activos
@app.route('/prestamos/activos', methods=['GET'])
def ver_prestamos_activos():
    try:
        prestamos = obtener_prestamos_activos()
        if prestamos:
            return jsonify([
                {
                    "id_prestamo": prestamo.id_prestamo,
                    "id_usuario": prestamo.id_usuario,
                    "nombre_usuario": prestamo.usuario,  
                    "libro_id": prestamo.id_libro,
                    "titulo_libro": prestamo.titulo,     
                    "fecha_prestamo": prestamo.fecha_prestamo,
                    "fecha_devolucion": prestamo.fecha_devolucion or "No devuelto"  
                } for prestamo in prestamos
            ])
        return jsonify({"mensaje": "No hay préstamos activos."}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener préstamos activos.", "error": str(e)}), 500

# Ruta para ver historial de préstamos
@app.route('/prestamos/historial', methods=['GET'])
def ver_historial_prestamos():
    try:
        historial = obtener_historial_prestamos()
        if historial:
            return jsonify([
                {
                    "id_prestamo": prestamo.id_prestamo,
                    "id_usuario": prestamo.id_usuario, 
                    "usuario": prestamo.usuario,  
                    "libro_id": prestamo.id_libro, 
                    "titulo_libro": prestamo.titulo, 
                    "fecha_prestamo": prestamo.fecha_prestamo,
                    "fecha_devolucion": prestamo.fecha_devolucion or "No devuelto"
                } for prestamo in historial
            ])
        return jsonify({"mensaje": "No hay historial de préstamos."}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener el historial de préstamos.", "error": str(e)}), 500

# Ruta para ver usuarios registrados
@app.route('/usuarios', methods=['GET'])
def ver_usuarios():
    try:
        usuarios = obtener_usuarios()
        if usuarios:
            return jsonify([
                {
                    "id_usuario": usuario.id_usuario,
                    "nombre": usuario.nombre,
                    "correo": usuario.correo,
                    "telefono": usuario.telefono
                } for usuario in usuarios
            ])
        return jsonify({"mensaje": "No hay usuarios registrados."}), 404
    except Exception as e:
        return jsonify({"mensaje": "Error al obtener usuarios.", "error": str(e)}), 500

# Ruta para prestar un libro
@app.route('/prestamos/prestar', methods=['POST'])
def prestar_libro_vista():
    try:
        data = request.json
        id_usuario = data.get("id_usuario")
        id_libro = data.get("id_libro")
        
        if id_usuario and id_libro:
            mensaje = prestar_libro(id_usuario, id_libro)
            if mensaje == "Libro prestado exitosamente.":
                return jsonify({"mensaje": mensaje}), 200
            else:
                return jsonify({"mensaje": mensaje}), 400
        return jsonify({"mensaje": "Faltan datos para prestar el libro."}), 400
    except Exception as e:
        return jsonify({"mensaje": "Error al prestar el libro.", "error": str(e)}), 500

@app.route('/prestamos/devolver', methods=['POST'])
def devolver_libro_vista():
    try:
        data = request.json
        id_prestamo = data.get("id_prestamo")
        
        if id_prestamo:
            mensaje = devolver_libro(id_prestamo)
            if mensaje == "Libro devuelto exitosamente.":
                return jsonify({"mensaje": mensaje}), 200
            else:
                return jsonify({"mensaje": mensaje}), 400
        return jsonify({"mensaje": "Faltan datos para devolver el libro."}), 400
    except Exception as e:
        return jsonify({"mensaje": "Error al devolver el libro.", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
