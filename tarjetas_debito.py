class TarjetaDeDebito:
    def __init__(self, cajaDeAhorro):
        self.cajaDeAhorro = cajaDeAhorro

    def get_saldo(self):
        print(self.cajaDeAhorro.consultar_saldo())

    def retirar(self, monto):
        if monto <= self.get_saldo():
            self.cajaDeAhorro.retirar(monto)
            print(f"Retiraste {monto}. Saldo restante {self.get_saldo()}") 
        else:
            print("No tienes suficiente saldo")
        
    def pagar(self, monto):
        if monto <= self.get_saldo():
            self.cajaDeAhorro.pagar(monto)
            print(f"Pagaste {monto}. Saldo restante {self.get_saldo()}") 
        else:
            print("No tienes suficiente saldo")


class TarjetaDeDebitoClassic(TarjetaDeDebito):
    def __init__(self, cajaDeAhorro):
        super().__init__(1, cajaDeAhorro)
        self.cantidadDeRetiros = 0
        self.tarifa_retiros = 1.03

    def retirar(self, monto):
        if monto <= 10000:
            if self.cantidadDeRetiros <= 5:
                self.cantidadDeRetiros += 1
                return super().retirar(monto)
            else:
                print(
                    "Se te cobro una tarifa del 3% por retirar mas de 5 veces en un dia")
                return super().retirar(monto*self.tarifa_retiros)
        else:
            print("Solo puedes retirar 10000 pesos por cajero por dia")
