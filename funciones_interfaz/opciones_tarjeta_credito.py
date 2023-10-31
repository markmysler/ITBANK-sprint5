def opciones_tarjetas_credito(usuario):
    # Esta función permite a un usuario seleccionar una tarjeta de crédito existente o agregar una nueva.

    # Parámetros:
    # usuario: Un objeto de usuario que contiene información sobre las tarjetas de crédito del usuario y los proveedores de crédito habilitados.

    # La función primero verifica si el usuario tiene alguna tarjeta de crédito. Si no tiene ninguna, selecciona la opción 2 automáticamente, que es para agregar una nueva tarjeta de crédito.

    # Si el usuario tiene al menos una tarjeta de crédito, se le presentan dos opciones:
    # 1. Seleccionar una de sus tarjetas de crédito existentes.
    # 2. Agregar una nueva tarjeta de crédito.

    # Si el usuario selecciona la opción 1, se le pide que ingrese el número de la tarjeta con la que desea operar.

    # Si el usuario selecciona la opción 2, se le pide que seleccione un proveedor de crédito de su lista de proveedores habilitados y luego se agrega una nueva tarjeta de crédito del proveedor seleccionado a su lista de tarjetas.
    
    if len(usuario.tarjetas_credito) == 0:
        seleccion = 2
    else:
        print("\nOpciones:\n")
        while True:
            try:
                seleccion = int(input("1.Mis tarjetas de credito\n2.Nueva tarjeta de credito\nTu seleccion (1-2): "))
                if seleccion in [1,2]:
                    break
                else:
                    print("\nDebe ingresar un numero entre 1 y 2")
            except ValueError:
                print("\nDebe ingresar un numero entero")
    if seleccion == 1:
        print("\nIngresa el numero de la tarjeta con la que deseas operar")
        for tarjeta in usuario.tarjetas_credito:
            print(tarjeta.numero)
        while True:
            try:
                num_credito = int(input("\nTu seleccion: "))
                if num_credito > 0 and num_credito <= len(usuario.tarjetas_credito):
                    break
            except ValueError:
                print("\nIngresa el numero de la tarjeta")
        opciones_tarjeta_credito(usuario, num_credito)
    elif seleccion == 2:
        n = 0
        print("\nOpciones:\n")
        for proveedor in usuario.proveedores_credito_habilitados:
            n+=1
            print(f"{n}.{proveedor}")
        while True:
            try:
                proveedor_credito = int(input(f"\nSeleccione su proveedor de credito (1-{len(usuario.proveedores_credito_habilitados)})\n \nTu seleccion: "))
                if proveedor_credito > 0 and proveedor_credito <= len(usuario.proveedores_credito_habilitados):
                    break
                else:
                    print(f"\nDebe ingresar un numero entre 1 y {len(usuario.proveedores_credito_habilitados)}")
            except ValueError:
                print("\nDebe ingresar un numero entero")
        usuario.agregar_tarjeta_credito(usuario.proveedores_credito_habilitados[proveedor_credito-1])
        
def opciones_tarjeta_credito(usuario, num_credito):
    # Esta función permite a un usuario seleccionar una acción para realizar con una tarjeta de crédito específica.

    # Parámetros:
    # usuario: Un objeto de usuario que contiene información sobre las tarjetas de crédito del usuario.
    # num_credito: El número de la tarjeta de crédito con la que el usuario desea operar.

    # La función presenta al usuario las siguientes opciones:
    # 1. Pagar en un pago.
    # 2. Pagar en cuotas.
    # 3. Pagar factura mensual.
    # 4. Agregar extensión.
    # 5. Interactuar con las extensiones de la tarjeta (si existen).
    
    print("\nSelecciona la accion que deseas realizar:\n \n1.Pagar en un pago\n2.Pagar en cuotas\n3.Pagar factura mensual\n4.Agregar extension")
    if len(usuario.tarjetas_credito[num_credito-1].extensiones) != 0:
        print("5.Mis Extensiones\n")
    else:
        print("\n")
    while True:
        try:
            accion = int(input("\nTu seleccion: "))
            if len(usuario.tarjetas_credito) == 0:
                if accion in [1,2,3,4]:
                    break
                else:
                    print("\nDebe ingresar un numero entre 1 y 4")
            else:
                if accion in [1,2,3,4,5]:
                    break
                else:
                    print("\nDebe ingresar un numero entre 1 y 5")
        except ValueError:
            print("\nDebe ingresar un numero entero")
    if accion == 1:
        while True:
            try:
                monto = int(input("\nMonto a pagar: "))
                break
            except ValueError:
                print("\nDebe ingresar un numero entero")
        usuario.tarjetas_credito[num_credito-1].pagar_un_pago(monto)
    elif accion == 2:
        while True:
            try:
                monto = int(input("\nMonto a pagar: "))
                break
            except ValueError:
                print("\nDebe ingresar un numero entero")
        while True:
            try:
                cuotas = int(input("\nCantidad de cuotas: "))
                if cuotas >= 1 and cuotas <= 36:
                    break
                else:
                    print("\nDebe ingresar un numero entre 1 y 36")
            except ValueError:
                print("\nDebe ingresar un numero entero")
        usuario.tarjetas_credito[num_credito-1].pagar_en_cuotas(monto, cuotas)
    elif accion == 3:
        usuario.tarjetas_credito[num_credito-1].pago_mensual()
    elif accion == 4:
        usuario.agregar_extension_tarjeta(usuario.tarjetas_credito[num_credito-1])
    elif accion == 5:
        print("\nSelecciona la extension con la que deseas operar: ")
        for extension in usuario.tarjetas_credito[num_credito-1].extensiones:
            print(f"\n{extension.numero-40000}")
        while True:
            try:
                num_extension = int(input("\nTu seleccion: "))
                if num_extension > 0 and num_extension <= len(usuario.tarjetas_credito[num_credito-1].extensiones):
                    break
                else:
                    print(f"\nDebe ingresar un numero entre 1 y {len(usuario.tarjetas_credito[num_credito-1].extensiones)}")
            except ValueError:
                print("\nDebe ingresar un numero entero")
        opciones_extension(usuario, num_credito, num_extension)
            
def opciones_extension(usuario, num_credito, num_extension):
    # Esta función permite a un usuario seleccionar una operación para realizar con una extensión específica de una tarjeta de crédito.

    # Parámetros:
    # usuario: Un objeto de usuario que contiene información sobre las tarjetas de crédito del usuario.
    # num_credito: El número de la tarjeta de crédito con la que el usuario desea operar.
    # num_extension: El número de la extensión con la que el usuario desea operar.

    # La función presenta al usuario las siguientes opciones:
    # 1. Pagar en un pago.
    # 2. Pagar en cuotas.
    
    print("\nSelecciona la operacion que deseas realizar:\n \n1.Pagar en en pago\n2.Pagar en cuotas")
    while True:
        try:
            operacion = int(input("\nTu seleccion: "))
            if operacion in [1,2]:
                break
            else:
                print("\nDebe ingresar un numero entre 1 y 2")
        except ValueError:
            print("\nDebe ingresar un numero entero")
    if operacion == 1:
        while True:
            try:
                monto = int(input("\nMonto a pagar: "))
                break
            except ValueError:
                print("\nDebe ingresar un numero entero")
        usuario.tarjetas_credito[num_credito-1].extensiones[num_extension-1].pagar_un_pago(monto)
    elif operacion == 2:
        while True:
            try:
                monto = int(input("\nMonto a pagar: "))
                break
            except ValueError:
                print("\nDebe ingresar un numero entero")
        while True:
            try:
                cuotas = int(input("\nCantidad de cuotas: "))
                if cuotas >= 1 and cuotas <= 36:
                    break
                else:
                    print("\nDebe ingresar un numero entre 1 y 36")
            except ValueError:
                print("\nDebe ingresar un numero entero")
        usuario.tarjetas_credito[num_credito-1].extensiones[num_extension-1].pagar_en_cuotas(monto, cuotas)