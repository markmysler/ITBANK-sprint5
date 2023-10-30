from datetime import datetime
class Transaccion:
    def __init__(self, estado, tipo, msj,usuario):
        self.estado = estado
        self.tipo = tipo
        self.msj = msj
        self.usuario = usuario
    def get_obj(self):
        return {
            "estado": self.estado,
            "tipo": self.tipo,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "numero": len(self.usuario.resumen.transacciones)+1,
            "msj": self.msj
        }