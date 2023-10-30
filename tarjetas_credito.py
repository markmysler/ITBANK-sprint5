from transaccion import Transaccion

class TarjetaCredito:
    def __init__(self, numero, limite_cuotas, limite_un_pago, emisor, usuario):
        self.numero = numero
        self.limite_cuotas = limite_cuotas
        self.limite_un_pago = limite_un_pago
        self.pagos_en_cuotas = []
        self.saldo_cuotas = self.limite_cuotas
        self.saldo_un_pago = self.limite_un_pago
        self.emisor = emisor
        self.extensiones = []
        self.usuario = usuario

    def pagar_en_cuotas(self, precio, cuotas):
        if precio <= self.saldo_cuotas:
            self.saldo_cuotas -= precio
            self.pagos_en_cuotas.append(PagoEnCuotas(precio, cuotas))
            print(f"\nEl pago de ${precio} se pago en {cuotas} cuotas")
            self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_{self.emisor.upper()}", f"El pago de ${precio} en {cuotas} cuotas se completo exitosamente", self.usuario))
        else:
            print("\nNo tienes suficiente saldo en cuotas")
            self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", f"COMPRA_EN_CUOTAS_TARJETA_CREDITO_{self.emisor.upper()}", f"El pago de ${precio} en {cuotas} cuotas fallo. Causa: Saldo para cuotas insuficiente", self.usuario))

    def pagar_un_pago(self, precio):
        print(precio)
        print(self.saldo_un_pago)
        if precio <= self.saldo_un_pago:
            self.saldo_un_pago -= precio
            print(f"\nPagaste {precio} en un pago")
            self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", f"COMPRA_TARJETA_CREDITO_{self.emisor.upper()}", f"El pago de ${precio} se completo exitosamente", self.usuario))
        else:
            print("\nSaldo en un pago insuficiente")
            self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", f"COMPRA_TARJETA_CREDITO_{self.emisor.upper()}", f"El pago de ${precio} fallo. Causa: Saldo insuficiente", self.usuario))
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
            self.tarjeta_madre.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", f"COMPRA_EN_CUOTAS_EXTENSION_CREDITO_{self.tarjeta_madre.emisor.upper()}", f"El pago de ${precio} en {cuotas} cuotas se completo exitosamente", self.usuario))
        else:
            print("\nNo tienes suficiente saldo en cuotas")
            self.tarjeta_madre.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", f"COMPRA_EN_CUOTAS_EXTENSION_CREDITO_{self.tarjeta_madre.emisor.upper()}", f"El pago de ${precio} en {cuotas} cuotas fallo. Causa: Saldo para cuotas insuficiente", self.usuario))

    def pagar_un_pago(self, precio):
        print(precio)
        print(self.tarjeta_madre.saldo_un_pago)
        if precio <= self.tarjeta_madre.saldo_un_pago:
            self.tarjeta_madre.saldo_un_pago -= precio
            print(f"\nPagaste {precio} en un pago")
            self.tarjeta_madre.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", f"COMPRA_EXTENSION_CREDITO_{self.tarjeta_madre.emisor.upper()}", f"El pago de ${precio} se completo exitosamente", self.usuario))

        else:
            print("\nSaldo en un pago insuficiente")
            self.tarjeta_madre.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", f"COMPRA_EXTENSION_CREDITO_{self.tarjeta_madre.emisor.upper()}", f"El pago de ${precio} fallo. Causa: Saldo insuficiente", self.usuario))