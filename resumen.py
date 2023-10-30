from clientes import ClienteClassic, ClienteGold


class Resumen:
    def __init__(self,usuario):
        self.usuario = usuario
        self.transacciones = []
    def get_tipo(self):
        if isinstance(self.usuario, ClienteClassic):
            return "CLASSIC"
        elif isinstance(self.usuario, ClienteGold):
            return "GOLD"
        else:
            return "BLACK"
    def get_resumen(self):
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
            "transacciones" : transacciones_obj_arr
        }
    def add_transaccion(self, transaccion):
        self.transacciones.append(transaccion)
