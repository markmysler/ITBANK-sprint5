from clientes import ClienteClassic


def opciones_tarjeta_debito(usuario, moneda, num_caja = 0):
    # Esta función permite a un usuario seleccionar una operación para realizar con su tarjeta de débito.

    # Parámetros:
    # usuario: Un objeto de usuario que contiene información sobre las cajas de ahorro del usuario.
    # moneda: La moneda de la caja de ahorro con la que el usuario desea operar.
    # num_caja: El número de la caja de ahorro con la que el usuario desea operar. Por defecto es 0.

    # La función presenta al usuario las siguientes opciones:
    # 1. Pagar.
    # 2. Consultar saldo.
    # 3. Extraer dinero.
    
    while True:
        try:
            operacion=int(input("\nSeleccione la operacion que desea realizar:\n1.Pagar\n2.Consultar Saldo\n3.Extraccion\n \nTu seleccion: "))
            if operacion in [1,2,3]:
                if operacion == 1:
                    monto = int(input("\nIngrese el monto a pagar: "))
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
                    monto = int(input("\nIngrese el monto a extraer: "))
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito.retirar(monto)
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito.retirar(monto)
                break
            else:
                print("\nIngrese un numero entre 1 y 3")
        except ValueError:
            print("\nIngrese un numero")