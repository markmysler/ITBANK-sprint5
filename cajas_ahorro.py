from tarjetas_debito import TarjetaDeDebito


class CajaDeAhorro:
    def __init__(self, moneda, numeroCaja):
        self.moneda = moneda
        self.__saldo = 0
        self.numeroCajaPesos = numeroCaja
        self.tarjeta_debito = None

    def consultar_saldo(self):
        print(self.__saldo) 

    def depositar(self, monto):
        self.__saldo += monto
        print(f"Deposito exitoso. Saldo: {self.__saldo}") 

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiraste {monto}. Saldo restante: {self.__saldo}") 
        else:
            print("No tienes suficiente saldo")

    def transferir(self, monto, destinatario):
        self.retirar(monto * 1.01)
        destinatario.cajaDeAhorroEnPesos.depositar(monto * 0.95)
        print(f"Transferencia a {destinatario.nombre} exitosa. Saldo restante: {self.__saldo}") 
