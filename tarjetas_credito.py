class TarjetaCredito:
    def __init__(self, numero, limite_cuotas, limite_un_pago, emisor):
        self.numero = numero
        self.limite_cuotas = limite_cuotas
        self.limite_un_pago = limite_un_pago
        self.pagos_en_cuotas = []
        self.saldo_cuotas = self.limite_cuotas
        self.saldo_un_pago = self.limite_un_pago
        self.emisor = emisor
        self.extensiones = []

    def pagar_en_cuotas(self, precio, cuotas):
        if precio <= self.saldo_cuotas:
            self.saldo_cuotas -= precio
            self.pagos_en_cuotas.append(PagoEnCuotas(precio, cuotas))
            print(f"\nEl pago de ${precio} se pago en {cuotas} cuotas")
        else:
            print("\nNo tienes suficiente saldo en cuotas")

    def pagar_un_pago(self, precio):
        print(precio)
        print(self.saldo_un_pago)
        if precio <= self.saldo_un_pago:
            self.saldo_un_pago -= precio
            print(f"\nPagaste {precio} en un pago")
        else:
            print("\nSaldo en un pago insuficiente")

    def pago_mensual(self):
        print(
            f"\nPagaste ${self.limite_un_pago-self.saldo_un_pago + self.calcular_pago_mensual_cuotas()}")
        self.saldo_un_pago = self.limite_un_pago
        self.saldo_cuotas += self.calcular_pago_mensual_cuotas()
        for pago in self.pagos_en_cuotas:
            pago.cuotas_pagas += 1
            if pago.cuotas_pagas == pago.cuotas:
                self.pagos_en_cuotas.remove(pago)

    def calcular_pago_mensual_cuotas(self):
        total = 0
        for pago in self.pagos_en_cuotas:
            total += pago.pago_por_mes
        return total

class PagoEnCuotas:
    def __init__(self, precio, cuotas):
        self.precio = precio
        self.cuotas = cuotas
        self.pago_por_mes = precio/cuotas
        self.cuotas_pagas = 0

class Extension:
    def __init__(self, tarjeta_madre):
        self.tarjeta_madre = tarjeta_madre
        self.numero = 40000 + len(self.tarjeta_madre.extensiones) + 1
    
    def pagar_en_cuotas(self,precio, cuotas):
        if precio <= self.tarjeta_madre.saldo_cuotas:
            self.tarjeta_madre.saldo_cuotas -= precio
            self.tarjeta_madre.pagos_en_cuotas.append(PagoEnCuotas(precio, cuotas))
            print(f"\nEl pago de ${precio} se pago en {cuotas} cuotas")
        else:
            print("\nNo tienes suficiente saldo en cuotas")
    def pagar_un_pago(self, precio):
        print(precio)
        print(self.tarjeta_madre.saldo_un_pago)
        if precio <= self.tarjeta_madre.saldo_un_pago:
            self.tarjeta_madre.saldo_un_pago -= precio
            print(f"\nPagaste {precio} en un pago")
        else:
            print("\nSaldo en un pago insuficiente")