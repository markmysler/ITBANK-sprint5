from cuenta_inversion import CuentaInversion
from transaccion import Transaccion


def opciones_cuenta_inversion(usuario):
    if usuario.cuenta_de_inversion == None:
        while True:
            abrir = input("\n¿Abrir cuenta de inversion? (si/no): ")
            if abrir in ["si", "no"]:
                break
            else:
                print("\nResponda con si o no")
        if abrir == "si":
            usuario.cuenta_de_inversion = CuentaInversion(usuario)
            usuario.resumen.add_transaccion(Transaccion("ACEPTADA","ALTA_CUENTA_DE_INVERSION","La cuenta de inversion se abrio exitosamente",usuario))
            print("\nCuenta de inversion abierta")
        else:
            print("\nEntendido")
    else:
        while True:
            try:
                res = int(input("\nSeleccione la accion que desea realizar:\n \n1.Consultar saldo\n2.Depositar\n \nTu seleccion: "))
                if res in [1,2]:
                    break
                else:
                    print("\nResponda 1 o 2")
            except ValueError:
                print("\nResponda con 1 o 2")
        if res == 1:
            usuario.cuenta_de_inversion.consultar_saldo()
        elif res == 2:
            while True:
                try:
                    monto = float(input("\nIngrese el monto a depositar: "))
                    break
                except ValueError:
                    print("\nIngrese un valor numerico")
            usuario.cuenta_de_inversion.depositar(monto)