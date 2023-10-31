from cheque import Cheque
from transaccion import Transaccion

class CuentaCorriente:

    # Representa una cuenta corriente de un usuario.

    # Attributos:
    #     moneda (str): La moneda de la cuenta corriente.
    #     numero (str): El número de la cuenta corriente.
    #     usuario (Usuario): El usuario propietario de la cuenta corriente.
    #     __saldo (float): El saldo actual de la cuenta corriente.
    #     chequera (Chequera): La chequera asociada a la cuenta corriente.
    #     cheques (list): Una lista de cheques emitidos por la cuenta corriente.


    def __init__(self, moneda, numero, usuario):
        # Inicializa una nueva instancia de la clase CuentaCorriente.

        # Args:
        #     moneda (str): La moneda de la cuenta corriente.
        #     numero (str): El número de la cuenta corriente.
        #     usuario (Usuario): El usuario propietario de la cuenta corriente.
        
        self.__saldo = 0
        self.usuario = usuario
        self.moneda = moneda
        self.numero = numero
        self.chequera = None
        self.cheques = []

    def depositar(self, monto):
        # Deposita un monto en la cuenta corriente.

        # Args:
        #     monto (float): El monto a depositar.
        
        self.__saldo += monto
        print(f"\nHas depositado {monto} {self.moneda} en tu cuenta corriente")
        self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CUENTA_CORRIENTE", f"Se depositaron {monto} {self.moneda} en la cuenta corriente", self.usuario))

    def get_saldo(self):
        # Obtiene el saldo actual de la cuenta corriente.
        
        print(f"\nSaldo: {self.__saldo}")

    def depositar_cheque(self, cheque):
        # Deposita un cheque en la cuenta corriente.

        # Args:
        #     cheque (Cheque): El cheque a depositar.
        
        self.__saldo += cheque.monto
        cheque.emisor.cuentaCorriente.__saldo -= cheque.monto
        cheque.depositado = True
        print(f"\nEl cheque por {cheque.monto}, emitido por {cheque.emisor.nombre} fue depositado en tu cuenta corriente") 
        self.usuario.resumen.add_transaccion(Transaccion("ACEPTADA", "DEPOSITO_CHEQUE_CUENTA_CORRIENTE", f"El cheque por ${cheque.monto}, emitido por {cheque.emisor.nombre} se deposito exitosamente", self.usuario))
