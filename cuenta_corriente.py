from cheque import Cheque
from transaccion import Transaccion


class CuentaCorriente:
    def __init__(self, moneda, numero, usuario):
        self.__saldo = 0
        self.usuario = usuario
        self.moneda = moneda
        self.numero = numero
        self.chequera = None
        self.cheques= []
    def depositar(self, monto):
        self.__saldo += monto
        print(f"\nHas depositado {monto} {self.moneda} en tu cuenta corriente")
        self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CUENTA_CORRIENTE", f"Se depositaron {monto} {self.moneda} en la cuenta corriente", self.usuario))
    def get_saldo(self):
        print(f"\nSaldo: {self.__saldo}")
    def depositar_cheque(self, cheque):
        self.__saldo += cheque.monto
        cheque.emisor.cuentaCorriente.__saldo -= cheque.monto
        cheque.depositado = True
        print(f"\nEl cheque por {cheque.monto}, emitido por {cheque.emisor.nombre} fue depositado en tu cuenta corriente") 
        self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CHEQUE_CUENTA_CORRIENTE", f"El cheque por ${cheque.monto}, emitido por {cheque.emisor.nombre} se deposito exitosamente", self.usuario))
