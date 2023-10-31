from cheque import Cheque


class Chequera:
    def __init__(self,cuenta_corriente):
        # Constructor de la clase Chequera.

        # Parametro:
        # cuenta_corriente: objeto de la clase CuentaCorriente.
        
        self.cuenta_corriente = cuenta_corriente
    def emitir_cheque(self, monto):
        # Método que emite un cheque.

        # Parametro:
        # monto: monto del cheque a emitir.
        
        self.cuenta_corriente.cheques.append(Cheque(monto, self.cliente)) 
        print(f"\nCheque por ${monto} emitido")