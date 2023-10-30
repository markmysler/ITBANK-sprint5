from tarjetas_debito import TarjetaDeDebito


class CajaDeAhorro:
    def __init__(self, moneda, numero):
        self.moneda = moneda
        self.__saldo = 0
        self.numero = numero
        self.tarjeta_debito = None

    def consultar_saldo(self):
        print(f"\nSaldo: {self.__saldo}") 

    def depositar(self, monto):
        self.__saldo += monto
        print(f"\nDeposito exitoso. Saldo: {self.__saldo}") 

    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print(f"\nRetiraste {monto}. Saldo restante: {self.__saldo}") 
        else:
            print("\nNo tienes suficiente saldo")

    def transferir(self, monto, destinatario):
        self.retirar(monto * 1.01)
        destinatario.cajas_ahorro_pesos[self.numero-1].depositar(monto * 0.95)
        print(f"\nTransferencia a {destinatario.nombre} exitosa. Saldo restante: {self.__saldo}") 
