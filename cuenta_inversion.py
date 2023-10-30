class CuentaInversion:
    def __init__(self):
        self.__saldo = 0
    def consultar_saldo(self):
        print(f"\nSaldo: {self.__saldo}")
    def depositar(self,monto):
        self.__saldo += monto
        print(f"\nSe depositaron ${monto} en la cuenta de inversion")