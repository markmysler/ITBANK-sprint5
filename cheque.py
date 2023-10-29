class Cheque:
    def __init__(self, monto, emisor, numero):
        self.monto = monto
        self.emisor = emisor
        self.depositado = False
        self.numero = numero
