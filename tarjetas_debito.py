from transaccion import Transaccion


class TarjetaDeDebito:
    def __init__(self, cajaDeAhorro):
        # Crea una nueva instancia de TarjetaDeDebito.

        # Args:
        # - cajaDeAhorro: La instancia de la clase CajaDeAhorro asociada a la tarjeta de débito.
        
        self.cajaDeAhorro = cajaDeAhorro

    def get_saldo(self):
        # Obtiene el saldo actual de la cuenta de ahorro asociada a la tarjeta de débito.

        # Returns:
        # - El saldo actual de la cuenta de ahorro.
        
        self.cajaDeAhorro.consultar_saldo()

    def retirar(self, monto):
        # Realiza un retiro de efectivo de la cuenta de ahorro asociada a la tarjeta de débito.

        # Args:
        # - monto: El monto a retirar.

        # Returns:
        # - None

        # Prints:
        # - Mensaje indicando si el retiro fue exitoso o fallido.
        
        if monto <= self.get_saldo():
            if monto <= self.cajaDeAhorro.usuario.limite_retiros_sin_cargo:
                if monto + self.cajaDeAhorro.usuario.monto_retirado_cajeros <= self.cajaDeAhorro.usuario.limite_retiro_por_dia:
                    self.cajaDeAhorro.saldo -= monto
                    print(f"\nRetiraste {monto}. Saldo restante {self.get_saldo()}")
                    self.cajaDeAhorro.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", f"Retiro de ${monto} por cajero automatico exitoso. Saldo restante: ${self.get_saldo()}", self.cajaDeAhorro.usuario))
                else:
                    print(f"Extraccion fallida. Retiro maximo por dia: {self.cajaDeAhorro.usuario.limite_retiro_por_dia}")
                    self.cajaDeAhorro.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", f"Retiro de ${monto} por cajero automatico fallo. Retiro maximo por dia: {self.cajaDeAhorro.usuario.limite_retiro_por_dia}", self.cajaDeAhorro.usuario))
            else:   
                print(f"Extraccion fallida. Retiros maximos: {self.cajaDeAhorro.usuario.limite_retiros_sin_cargo}")
                self.cajaDeAhorro.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", f"Retiro de ${monto} por cajero automatico fallo. Retiros maximos: {self.cajaDeAhorro.usuario.limite_retiro_por_dia}", self.cajaDeAhorro.usuario))
        else:
            print("\nNo tienes suficiente saldo")
            self.cajaDeAhorro.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "RETIRO_EFECTIVO_CAJERO_AUTOMATICO", "Retiro fallido. Saldo insuficiente", self.cajaDeAhorro.usuario))

        
    def pagar(self, monto):
        # Realiza un pago utilizando la tarjeta de débito.

        # Args:
        # - monto: El monto a pagar.

        # Returns:
        # - None

        # Prints:
        # - Mensaje indicando si el pago fue exitoso o fallido.
        
        if monto <= self.get_saldo():
            self.cajaDeAhorro.saldo -= monto
            print(f"\nPagaste {monto}. Saldo restante {self.get_saldo()}")
            self.cajaDeAhorro.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "PAGO_TARJETA_DEBITO", f"El pago de ${monto} se completo exitosamente", self.cajaDeAhorro.usuario))

        else:
            print("\nNo tienes suficiente saldo")
            self.cajaDeAhorro.usuario.resumen.add_transaccion(Transaccion("RECHAZADA", "PAGO_TARJETA_DEBITO", f"Pago de ${monto} fallido. Saldo insuficiente.", self.cajaDeAhorro.usuario))

