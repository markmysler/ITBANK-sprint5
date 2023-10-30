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
            self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "TRANSFERENCIA_CAJA_AHORRO", f"Se transfirieron {monto} {self.moneda} a {destinatario.nombre}", self.usuario))
        else:
            print("\nTransferencia fallida. Saldo insuficiente")
            self.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "TRANSFERENCIA_CAJA_AHORRO", f"La transferencia fallo. Causa: Saldo insuficiente", self.usuario))
