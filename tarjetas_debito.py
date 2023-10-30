class TarjetaDeDebito:
    def __init__(self, cajaDeAhorro):
        self.cajaDeAhorro = cajaDeAhorro

    def get_saldo(self):
        self.cajaDeAhorro.consultar_saldo()

    def retirar(self, monto):
        if monto <= self.get_saldo():
            self.cajaDeAhorro.retirar(monto)
            print(f"\nRetiraste {monto}. Saldo restante {self.get_saldo()}") 
        else:
            print("\nNo tienes suficiente saldo")
        
    def pagar(self, monto):
        if monto <= self.get_saldo():
            self.cajaDeAhorro.pagar(monto)
            print(f"\nPagaste {monto}. Saldo restante {self.get_saldo()}") 
        else:
            print("\nNo tienes suficiente saldo")

