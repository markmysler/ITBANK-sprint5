from cheque import Cheque


class CuentaCorriente:
    def __init__(self, moneda, numero, cliente):
        self.saldo = 0
        self.cliente = cliente
        self.moneda = moneda
        self.numero = numero
        self.chequera = None

    def emitir_cheque(self, monto):
        return Cheque(monto, self.cliente)

    def depositar_cheque(self, cheque):
        self.saldo += cheque.monto
        cheque.emisor.cuentaCorriente.saldo -= cheque.monto
        cheque.depositado = True
        return f"El cheque por {cheque.monto}, emitido por {cheque.emisor.nombre} fue depositado en tu cuenta corriente"
