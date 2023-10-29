from funciones_interfaz.opciones_tarjeta_debito import opciones_tarjeta_debito
from lista_contactos import lista_contactos 


def opciones_cuentas_ahorro(usuario):
    while True:
        try:
            seleccion = int(input("1. Mis Cuentas de ahorro\n2. Crear una cuenta de ahorro\nTu seleccion: "))
            if seleccion in [1,2]:
                if seleccion == 1:
                    print("Selecciona el numero de la cuenta de ahorro con la que queres operar")
                    cuentas = []
                    for cuenta in usuario.cajas_ahorro_pesos:
                        print(cuenta.numeroCajaPesos)
                        cuentas.append(cuenta)
                    for cuenta in usuario.cajas_ahorro_dolares:
                        print(cuenta.numeroCajaDolares)
                        cuentas.append(cuenta)
                    num_caja = int(input("Tu seleccion: "))
                    while not(num_caja > 0 and num_caja <= len(usuario.cajas_ahorro_pesos)+len(usuario.cajas_ahorro_dolares)):
                        num_caja = input(f"Ingrese un numero entre 1 y {len(usuario.cajas_ahorro_pesos)+len(usuario.cajas_ahorro_dolares)}" )
                    
                    if num_caja <= len(usuario.cajas_ahorro_pesos):
                        opciones_caja_ahorro(usuario,num_caja -1,"pesos")
                    else:
                        opciones_caja_ahorro(usuario,num_caja -1,"dolares")
                elif seleccion == 2:
                    moneda = int(input("Seleccione la moneda de la nueva caja de ahorro:\n1.Pesos\n2.Dolares"))
                    if moneda == 1:
                        usuario.crear_caja_de_ahorro("pesos")
                    elif moneda == 2:
                        usuario.crear_caja_de_ahorro("dolares")
                    
                break
            else:
                print("Porfavor ingrese un numero entre uno y dos.")
        except ValueError:
            print("Porfavor ingrese un numero.")
            
def opciones_caja_ahorro(usuario,num_caja, moneda):
    print("Seleccione la opeacion que desea realizar:\n1.Consultar saldo\n2.Depositar\n3.Transferir")
    if moneda == "pesos":
        if usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito != None:
            print("4.Ver tarjeta de debito")
        else:
            print("4.Asociar tarjeta de debito")
    else:
        if usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito != None:
            print("4.Ver tarjeta de debito")
        else:
            print("4.Asociar tarjeta de debito")
    while True:
        try:
            opcion = int(input("Tu seleccion: "))
            if opcion in [1,2,3,4]:
                if opcion == 1:
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].consultar_saldo()
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].consultar_saldo()
                elif opcion == 2:
                    monto = int(input("Ingrese el monto a depositar: "))
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].depositar(monto)
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].depositar(monto)
                elif opcion == 3:
                    monto = int(input("Ingrese el monto a transferir: "))
                    n=0
                    for contacto in lista_contactos:
                        n+=1
                        print(f"{n}. {contacto.nombre} {contacto.apellido}")
                    beneficiario = int(input("Ingrese el numero del beneficiario: "))
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].transferir(monto,lista_contactos[beneficiario-1])
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].transferir(monto,lista_contactos[beneficiario-1])
                elif opcion == 4:
                    if moneda == "pesos":
                        if usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito != None:
                            opciones_tarjeta_debito(usuario,moneda, num_caja)
                        else:
                            usuario.asociar_tarjeta_debito_caja_ahorro(usuario.cajas_ahorro_pesos[num_caja])
                    else:
                        if usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito != None:
                            opciones_tarjeta_debito(usuario,moneda, num_caja)
                        else:
                            usuario.asociar_tarjeta_debito_caja_ahorro(usuario.cajas_ahorro_dolares[num_caja])
            else:
                print("Ingresa un numero entre 1 y 4")
        except ValueError:
            print("Porfavor ingrese un numero.")