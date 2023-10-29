class TarjetaCredito:
    def __init__(self, numero, limite_cuotas, limite_un_pago, emisor):
        self.numero = numero
        self.limite_cuotas = limite_cuotas
        self.limite_un_pago = limite_un_pago
        self.pagos_en_cuotas = []
        self.saldo_cuotas = self.limite_cuotas
        self.saldo_un_pago = self.limite_un_pago
        self.emisor = emisor

    def pagar_en_cuotas(self, precio, cuotas):
        if precio <= self.saldo_cuotas:
            self.saldo_cuotas -= precio
            self.pagos_en_cuotas.append(PagoEnCuotas(precio, cuotas))
            print(f"El pago de ${precio} se pago en {cuotas} cuotas")
        else:
            print("No tienes suficiente saldo en cuotas")

    def pagar_un_pago(self, precio):
        print(precio)
        print(self.saldo_un_pago)
        if precio <= self.saldo_un_pago:
            self.saldo_un_pago -= precio
            print(f"Pagaste {precio} en un pago")
        else:
            print("Saldo en un pago insuficiente")

    def pago_mensual(self):
        self.saldo_un_pago = self.limite_un_pago
        self.saldo_cuotas += self.calcular_pago_mensual_cuotas()
        for pago in self.pagos_en_cuotas:
            pago.cuotas_pagas += 1
            if pago.cuotas_pagas == pago.cuotas:
                self.pagos_en_cuotas.remove(pago)
        print(
            f"Pagaste ${self.limite_un_pago-self.saldo_un_pago + self.calcular_pago_mensual_cuotas()}")

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
