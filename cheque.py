class Cheque:
    def __init__(self, monto, emisor, numero):
        # Constructor de la clase Cheque.

        # Parametros:
        # monto: monto del cheque.
        # emisor: emisor del cheque.
        # numero: número del cheque.
        
        self.monto = monto
        self.emisor = emisor
        self.depositado = False
        self.numero = numero
