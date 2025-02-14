class Usuario:
    def __init__(self, id_usuario, nombre, correo, telefono):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

class Libro:
    def __init__(self, id_libro, titulo, autor, disponible):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
        
class Prestamo:
    def __init__(self, id_prestamo, id_usuario, id_libro, fecha_prestamo, usuario, titulo, fecha_devolucion=None):
        self.id_prestamo = id_prestamo
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.usuario = usuario
        self.titulo =  titulo
