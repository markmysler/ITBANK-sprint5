from transaccion import Transaccion

class CuentaInversion:
    # Representa una cuenta de inversión de un usuario.

    # Attributes:
    #     usuario (Usuario): El usuario propietario de la cuenta de inversión.
    #     __saldo (float): El saldo actual de la cuenta de inversión.

    def __init__(self, usuario):
        # Inicializa una nueva instancia de la clase CuentaInversion.

        # Args:
        #     usuario (Usuario): El usuario propietario de la cuenta de inversión.

        self.__saldo = 0
        self.usuario = usuario

    def consultar_saldo(self):
        # Consulta el saldo actual de la cuenta de inversión.
        print(f"\nSaldo: {self.__saldo}")

    def depositar(self, monto):
        # Deposita un monto en la cuenta de inversión.

        # Args:
        #     monto (float): El monto a depositar.
        
        self.__saldo += monto
        print(f"\nSe depositaron ${monto} en la cuenta de inversión")
        self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CUENTA_DE_INVERSION", f"Se depositaron ${monto} en la cuenta de inversión", self.usuario))
