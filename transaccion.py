from datetime import datetime
class Transaccion:
    def __init__(self, estado, tipo, msj,usuario):
        # Crea una instancia de la clase Transaccion.

        # Args:
        #     estado (str): El estado de la transacción, puede ser "ACEPTADA" o "RECHAZADA".
        #     tipo (str): El tipo de transacción.
        #     msj (str): Un mensaje que describe la transacción.
        #     usuario (Usuario): El usuario que realizó la transacción.
        
        self.estado = estado
        self.tipo = tipo
        self.msj = msj
        self.usuario = usuario
    def get_obj(self):
        # Devuelve un diccionario con la información de la transacción.

        # Returns:
        #     dict: Un diccionario con los atributos de la transacción.
        
        return {
            "estado": self.estado,
            "tipo": self.tipo,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "numero": len(self.usuario.resumen.transacciones)+1,
            "msj": self.msj
        }