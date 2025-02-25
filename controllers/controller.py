from database.connection import crear_conexion
from models.models import Usuario, Libro, Prestamo

def prestar_libro(id_usuario, id_libro):
    conexion = crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT disponible FROM libros WHERE id_libro = %s", (id_libro,))
    resultado = cursor.fetchone()
    if resultado is None:
        conexion.close()
        return "Libro no encontrado."

    if not resultado[0]:
        conexion.close()
        return "El libro no está disponible."

    cursor.execute(
        "INSERT INTO prestamos (id_usuario, id_libro) VALUES (%s, %s)",
        (id_usuario, id_libro)
    )

    cursor.execute("UPDATE libros SET disponible = FALSE WHERE id_libro = %s", (id_libro,))
    conexion.commit()
    conexion.close()
    
    return "Libro prestado exitosamente."

def devolver_libro(id_prestamo):
    conexion = crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_libro, fecha_devolucion FROM prestamos WHERE id_prestamo = %s", (id_prestamo,))
    resultado = cursor.fetchone()

    if resultado is None:
        conexion.close()
        return "Préstamo no encontrado."

    id_libro, fecha_devolucion = resultado

    cursor.execute("SELECT disponible FROM libros WHERE id_libro = %s", (id_libro,))
    resultado_libro = cursor.fetchone()

    if resultado_libro is None:
        conexion.close()
        return "Libro no encontrado."

    if resultado_libro[0]: 
        conexion.close()
        return "El libro ya ha sido devuelto previamente."

    cursor.execute("UPDATE libros SET disponible = TRUE WHERE id_libro = %s", (id_libro,))
    cursor.execute("UPDATE prestamos SET fecha_devolucion = NOW() WHERE id_prestamo = %s", (id_prestamo,))

    conexion.commit()
    conexion.close()
    
    return "Libro devuelto exitosamente."


def obtener_libros_disponibles():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_libro, titulo, autor FROM vista_libros_disponibles")
    resultados = cursor.fetchall()
    
    libros = []
    for resultado in resultados:
        libro = Libro(resultado[0], resultado[1], resultado[2], True)  
        libros.append(libro)
    
    conexion.close()
    return libros

def obtener_prestamos_activos():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_prestamo, id_usuario, usuario, titulo, fecha_prestamo, id_libro FROM vista_prestamos_activos")
    resultados = cursor.fetchall()

    prestamos = []
    for resultado in resultados:
        prestamo = Prestamo(resultado[0], resultado[1], resultado[5], resultado[4], usuario=resultado[2], titulo=resultado[3] )
        prestamos.append(prestamo)
    
    conexion.close()
    return prestamos



def obtener_historial_prestamos():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_prestamo, id_usuario, usuario, titulo, fecha_prestamo, fecha_devolucion, id_libro FROM vista_historial_prestamos")
    resultados = cursor.fetchall()

    historial = []
    for resultado in resultados:
        prestamo = Prestamo(resultado[0],usuario=resultado[2],id_usuario=resultado[1],titulo=resultado[3],fecha_prestamo=resultado[4], fecha_devolucion=resultado[5], id_libro=resultado[6] )
        historial.append(prestamo)
    
    conexion.close()
    return historial





def obtener_usuarios():
    conexion = crear_conexion()
    cursor = conexion.cursor()

    cursor.execute("SELECT id_usuario, nombre, correo, telefono FROM usuarios")
    resultados = cursor.fetchall()

    usuarios = []
    for resultado in resultados:
        usuario = Usuario(resultado[0], resultado[1], resultado[2], resultado[3])
        usuarios.append(usuario)
    
    conexion.close()
    return usuarios
