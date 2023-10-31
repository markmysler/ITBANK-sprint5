def opciones_cuentas_corrientes(usuario):
    # Esta función maneja las opciones de las cuentas corrientes de un usuario.

    # Parámetros:
    # usuario (objeto): Un objeto de usuario que tiene una lista de cuentas corrientes en pesos y dólares.

    # Comportamiento:
    # Si el usuario no tiene ninguna cuenta corriente, se le dará la opción de crear una.
    # Si el usuario ya tiene una o más cuentas corrientes, se le dará la opción de seleccionar una cuenta para operar o crear una nueva cuenta.
    
    while True:
        try:
            if len(usuario.cuentas_corrientes_pesos) + len(usuario.cuentas_corrientes_dolares) == 0:
                seleccion = 2
            else:
                seleccion = int(input("\n1. Mis Cuentas corrientes\n2. Crear una cuenta corriente\nTu seleccion: "))
            if seleccion in [1,2]:
                if seleccion == 1:
                    print("\nSelecciona el numero de la cuenta corriente con la que queres operar")
                    cuentas = []
                    for cuenta in usuario.cuentas_corrientes_pesos:
                        print(cuenta.numero)
                        cuentas.append(cuenta)
                    for cuenta in usuario.cuentas_corrientes_dolares:
                        print(cuenta.numero)
                        cuentas.append(cuenta)
                    num_cuenta = int(input("\nTu seleccion: "))
                    while not(num_cuenta > 0 and num_cuenta <= len(usuario.cuentas_corrientes_pesos)+len(usuario.cuentas_corrientes_dolares)):
                        num_cuenta = input(f"\nIngrese un numero entre 1 y {len(usuario.cuentas_corrientes_pesos)+len(usuario.cuentas_corrientes_dolares)}" )
                    
                    if num_cuenta <= len(usuario.cuentas_corrientes_pesos):
                        opciones_cuenta_corriente(usuario,num_cuenta -1,"pesos")
                    else:
                        opciones_cuenta_corriente(usuario,num_cuenta -1,"dolares")
                elif seleccion == 2:
                    moneda = int(input("\nSeleccione la moneda de la nueva cuenta corriente:\n \n1.Pesos\n2.Dolares\n \nTu seleccion: "))
                    if moneda == 1:
                        usuario.crear_cuenta_corriente("pesos")
                    elif moneda == 2:
                        usuario.crear_cuenta_corriente("dolares")
                    
                break
            else:
                print("\nPorfavor ingrese un numero entre uno y dos.")
        except ValueError:
            print("\nPorfavor ingrese un numero.")
def opciones_cuenta_corriente(usuario, num_cuenta, moneda):
    # Esta función maneja las opciones de una cuenta corriente específica de un usuario.

    # Parámetros:
    # usuario (objeto): Un objeto de usuario que tiene una lista de cuentas corrientes en pesos y dólares.
    # num_cuenta (int): El índice de la cuenta corriente con la que el usuario desea operar.
    # moneda (str): La moneda de la cuenta corriente ("pesos" o "dolares").

    # Comportamiento:
    # El usuario puede seleccionar una operación para realizar en su cuenta corriente. Las opciones son:
    # 1. Consultar saldo
    # 2. Depositar
    # 3. Emitir un cheque o asociar una chequera, dependiendo de si ya tienen una chequera asociada o no.
    
    print("\nSeleccione la operacion que desea realizar: \n1.Consultar saldo\n2.Depositar")
    if moneda == "pesos":
        if usuario.cuentas_corrientes_pesos[num_cuenta].chequera != None:
            print("3.Emitir Cheque")
        else:
            print("3.Asociar chequera")
    else:
        if usuario.cuentas_corrientes_dolares[num_cuenta].chequera != None:
            print("3.Emitir Cheque")
        else:
            print("3.Asociar chequera")
    while True:
        try:
            op= int(input("\nTu seleccion: "))
            if op >= 1 and op <= 3:
                break
            else:
                print("\nPorfavor ingrese un numero entre uno y tres.")
        except ValueError:
            print("\nPorfavor ingrese un numero.")
    if op == 1:
        if moneda == "pesos":
            usuario.cuentas_corrientes_pesos[num_cuenta].get_saldo()
        else:
            usuario.cuentas_corrientes_dolares[num_cuenta].get_saldo()
    elif op == 2:
        while True:
            try:
                monto = int(input("\nIngrese el monto a depositar: "))
                break
            except ValueError:
                print("\nIngrese un numero.")
        if moneda == "pesos":
            usuario.cuentas_corrientes_pesos[num_cuenta].depositar(monto)
        else:
            usuario.cuentas_corrientes_dolares[num_cuenta].depositar(monto)
    elif op == 3:
        
        if moneda == "pesos":
            if usuario.cuentas_corrientes_pesos[num_cuenta].chequera != None:
                while True:
                    try:
                        monto = int(input("\nIngrese el monto a depositar: "))
                        break
                    except ValueError:
                        print("\nIngrese un numero.")
                usuario.cuentas_corrientes_pesos[num_cuenta].chequera.emitir_cheque(monto)
            else:
                usuario.asociar_chequera_cuenta_corriente(usuario.cuentas_corrientes_pesos[num_cuenta])
        else:
            if usuario.cuentas_corrientes_dolares[num_cuenta].chequera != None:
                while True:
                    try:
                        monto = int(input("\nIngrese el monto a depositar: "))
                        break
                    except ValueError:
                        print("\nIngrese un numero.")
                usuario.cuentas_corrientes_dolares[num_cuenta].chequera.emitir_cheque(monto)
            else:
                usuario.asociar_chequera_cuenta_corriente(usuario.cuentas_corrientes_dolares[num_cuenta])