from funciones import calcular_monto_total
from transaccion import Transaccion
from tarjetas_debito import TarjetaDeDebito


class CajaDeAhorro:
    def __init__(self, moneda, numero,usuario):
        self.moneda = moneda
        self.saldo = 0
        self.numero = numero
        self.tarjeta_debito = None
        self.usuario = usuario

    def consultar_saldo(self):
        print(f"\nSaldo: {self.saldo}") 

    def depositar(self, monto):
        self.saldo += monto
        print(f"\nDeposito exitoso. Saldo: {self.saldo}")
        if self.usuario.resumen != None:
            self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CAJA_AHORRO", f"Deposito de {monto} {self.moneda} exitoso. Nuevo saldo: {self.saldo}", self.usuario))

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"\nRetiraste {monto}. Saldo restante: {self.saldo}")
            self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "RETIRO_EFECTIVO_POR_CAJA", f"Se retiraron {monto} {self.moneda} de la caja de ahorro", self.usuario))
        else:
            print("\nNo tienes suficiente saldo")
            self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "RETIRO_EFECTIVO_POR_CAJA", f"El retiro de {monto} {self.moneda} fallo. Causa: Saldo insuficiente", self.usuario))

    def transferir(self, monto, destinatario):
        if monto <= self.saldo:
            self.retirar(monto * 1.01)
            destinatario.cajas_ahorro_pesos[self.numero-1].depositar(monto * 0.95)
            print(f"\nTransferencia a {destinatario.nombre} exitosa. Saldo restante: {self.saldo}")
            self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", f"TRANSFERENCIA_ENVIADA_{self.moneda.upper()}", f"Se transfirieron {monto} {self.moneda} a {destinatario.nombre}", self.usuario))
        else:
            print("\nTransferencia fallida. Saldo insuficiente")
            self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", f"TRANSFERENCIA_ENVIADA_{self.moneda.upper()}", f"La transferencia fallo. Causa: Saldo insuficiente", self.usuario))
    def comprar_vender_dolares(self, monto, cta_destino):
        precio_dolar = 1000
        if self.moneda == "pesos":
            costo_operacion = calcular_monto_total(monto, precio_dolar)
            if self.saldo >= costo_operacion:
                self.saldo -= costo_operacion
                cta_destino.saldo += monto
                print(f"Compraste {monto} dolares")
                self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "COMPRA_DOLAR", f"La compra de {monto} dolares se completo exitosamente.", self.usuario))
            else:
                print("\nSaldo insuficiente")
                self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "COMPRA_DOLAR", "La compra fallo. Causa: Saldo en pesos insuficiente", self.usuario))
        else:
            if self.saldo >= monto:
                self.saldo -= monto
                cta_destino.saldo += monto*precio_dolar
                print(f"Vendiste {monto} dolares")
                self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "VENTA_DOLAR", f"La venta de {monto} dolares se completo exitosamente.", self.usuario))
            else:
                print("\nSaldo insuficiente")
                self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "VENTA_DOLAR", "La venta fallo. Causa: Saldo en dolares insuficiente", self.usuario))