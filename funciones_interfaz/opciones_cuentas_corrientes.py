def opciones_cuentas_corrientes(usuario):
    while True:
        try:
            if len(usuario.cuentas_corrientes_pesos) + len(usuario.cuentas_corrientes_dolares) == 0:
                seleccion = 2
            else:
                seleccion = int(input("1. Mis Cuentas corrientes\n2. Crear una cuenta corriente\nTu seleccion: "))
            if seleccion in [1,2]:
                if seleccion == 1:
                    print("Selecciona el numero de la cuenta corriente con la que queres operar")
                    cuentas = []
                    for cuenta in usuario.cuentas_corrientes_pesos:
                        print(cuenta.numero)
                        cuentas.append(cuenta)
                    for cuenta in usuario.cuentas_corrientes_dolares:
                        print(cuenta.numero)
                        cuentas.append(cuenta)
                    num_cuenta = int(input("Tu seleccion: "))
                    while not(num_cuenta > 0 and num_cuenta <= len(usuario.cuentas_corrientes_pesos)+len(usuario.cuentas_corrientes_dolares)):
                        num_cuenta = input(f"Ingrese un numero entre 1 y {len(usuario.cuentas_corrientes_pesos)+len(usuario.cuentas_corrientes_dolares)}" )
                    
                    if num_cuenta <= len(usuario.cuentas_corrientes_pesos):
                        opciones_cuenta_corriente(usuario,num_cuenta -1,"pesos")
                    else:
                        opciones_cuenta_corriente(usuario,num_cuenta -1,"dolares")
                elif seleccion == 2:
                    moneda = int(input("Seleccione la moneda de la nueva caja de ahorro:\n1.Pesos\n2.Dolares"))
                    if moneda == 1:
                        usuario.crear_cuenta_corriente("pesos")
                    elif moneda == 2:
                        usuario.crear_cuenta_corriente("dolares")
                    
                break
            else:
                print("Porfavor ingrese un numero entre uno y dos.")
        except ValueError:
            print("Porfavor ingrese un numero.")
def opciones_cuenta_corriente(usuario, num_cuenta, moneda):
    print("")