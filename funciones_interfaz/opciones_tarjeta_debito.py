from clientes import ClienteClassic


def opciones_tarjeta_debito(usuario, moneda, num_caja = 0):
    while True:
        try:
            operacion=int(input("Seleccione la operacion que desea realizar:\n1.Pagar\2Consultar Saldo\n3.Extraccion"))
            if operacion in [1,2,3]:
                if operacion == 1:
                    monto = int(input("Ingrese el monto a pagar"))
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito.pagar(monto)
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito.pagar(monto)
                elif operacion == 2:
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito.get_saldo()
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito.get_saldo()
                elif operacion == 3:
                    monto = int(input("Ingrese el monto a extraer"))
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito.retirar(monto)
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito.retirar(monto)
                break
            else:
                print("Ingrese un numero entre 1 y 3")
        except ValueError:
            print("Porfavor ingrese un numero")