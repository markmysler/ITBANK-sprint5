from transaccion import Transaccion


class CuentaInversion:
    def __init__(self,usuario):
        self.__saldo = 0
        self.usuario = usuario
    def consultar_saldo(self):
        print(f"\nSaldo: {self.__saldo}")
    def depositar(self,monto):
        self.__saldo += monto
        print(f"\nSe depositaron ${monto} en la cuenta de inversion")
        self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CUENTA_DE_INVERSION", f"Se depositaron ${monto} en la cuenta de inversion", self.usuario))