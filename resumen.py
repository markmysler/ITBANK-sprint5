from clientes import ClienteClassic, ClienteGold


class Resumen:
    # Representa el resumen de transacciones de un usuario.

    # Attributes:
    #     usuario (Usuario): El usuario propietario del resumen.
    #     transacciones (list): Una lista de transacciones realizadas por el usuario.

    def __init__(self, usuario):
        # Inicializa una nueva instancia de la clase Resumen.

        # Args:
        #     usuario (Usuario): El usuario propietario del resumen.

        self.usuario = usuario
        self.transacciones = []

    def get_tipo(self):
        # Obtiene el tipo de usuario basado en el tipo de cliente.

        # Args:
        #     None

        # Returns:
        #     str: El tipo de usuario ("CLASSIC", "GOLD" o "BLACK").


        if isinstance(self.usuario, ClienteClassic):
            return "CLASSIC"
        elif isinstance(self.usuario, ClienteGold):
            return "GOLD"
        else:
            return "BLACK"

    def get_resumen(self):
        # Obtiene el resumen de transacciones del usuario.

        # Returns:
        #     dict: Un diccionario con la información del resumen.

        transacciones_obj_arr = []
        if len(self.transacciones) != 0:
            for transaccion in self.transacciones:
                transacciones_obj_arr.append(transaccion.get_obj())
        return {
            "numero": self.usuario.numero_cuenta,
            "nombre": self.usuario.nombre,
            "apellido": self.usuario.apellido,
            "dni": self.usuario.dni,
            "tipo": self.get_tipo(),
            "transacciones": transacciones_obj_arr
        }

    def add_transaccion(self, transaccion):
        # Agrega una transacción al resumen.

        # Args:
        #     transaccion (Transaccion): La transacción a agregar.
        self.transacciones.append(transaccion)
