from cheque import Cheque


class Chequera:
    def __init__(self,cuenta_corriente):
        self.cuenta_corriente = cuenta_corriente
    def emitir_cheque(self, monto):
        self.cuenta_corriente.cheques.append(Cheque(monto, self.cliente)) 
        print(f"\nCheque por ${monto} emitido")