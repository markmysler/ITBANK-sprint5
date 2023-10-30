from cheque import Cheque


class CuentaCorriente:
    def __init__(self, moneda, numero, cliente):
        self.__saldo = 0
        self.cliente = cliente
        self.moneda = moneda
        self.numero = numero
        self.chequera = None
        self.cheques= []
    def depositar(self, monto):
        self.__saldo += monto
        print(f"\nHas depositado {monto} {self.moneda} en tu cuenta corriente")
    def get_saldo(self):
        print(f"\nSaldo: {self.__saldo}")
    def depositar_cheque(self, cheque):
        self.__saldo += cheque.monto
        cheque.emisor.cuentaCorriente.__saldo -= cheque.monto
        cheque.depositado = True
        print(f"\nEl cheque por {cheque.monto}, emitido por {cheque.emisor.nombre} fue depositado en tu cuenta corriente") 
