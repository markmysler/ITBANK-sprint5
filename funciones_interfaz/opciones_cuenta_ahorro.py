from funciones_interfaz.opciones_tarjeta_debito import opciones_tarjeta_debito
from lista_contactos import lista_contactos 


def opciones_cuentas_ahorro(usuario):
    while True:
        try:
            seleccion = int(input("\n1. Mis Cuentas de ahorro\n2. Crear una cuenta de ahorro\n \nTu seleccion: "))
            if seleccion in [1,2]:
                break
            
            else:
                print("\nIngrese un numero entre uno y dos.")
        except ValueError:
            print("\nIngrese un numero.")
    if seleccion == 1:
        print("\nSelecciona el numero de la cuenta de ahorro con la que queres operar")
        cuentas = []
        for cuenta in usuario.cajas_ahorro_pesos:
            print(f"\n{cuenta.numero}")
            cuentas.append(cuenta)
        for cuenta in usuario.cajas_ahorro_dolares:
            print(f"\n{cuenta.numero + len(usuario.cajas_ahorro_pesos)}")
            cuentas.append(cuenta)
        num_caja = int(input("\nTu seleccion: "))
        if num_caja <= len(usuario.cajas_ahorro_pesos):
            opciones_caja_ahorro(usuario,num_caja -1,"pesos")
        else:
            opciones_caja_ahorro(usuario,num_caja - len(usuario.cajas_ahorro_pesos) -1,"dolares")
                
    elif seleccion == 2:
        moneda = int(input("\nSeleccione la moneda de la nueva caja de ahorro:\n \n1.Pesos\n2.Dolares\n \nTu seleccion: "))
        if moneda == 1:
            usuario.crear_caja_de_ahorro("pesos")
        elif moneda == 2:
            usuario.crear_caja_de_ahorro("dolares")
def opciones_caja_ahorro(usuario,num_caja, moneda):
    print("\nSeleccione la opeacion que desea realizar:\n \n1.Consultar saldo\n2.Depositar\n3.Transferir")
    if moneda == "pesos":
        if usuario.cajas_ahorro_pesos[num_caja].tarjeta_debito != None:
            print("4.Ver tarjeta de debito")
        else:
            print("4.Asociar tarjeta de debito")
        print("5.Comprar dolares")
    else:
        if usuario.cajas_ahorro_dolares[num_caja].tarjeta_debito != None:
            print("4.Ver tarjeta de debito")
        else:
            print("4.Asociar tarjeta de debito")
        print("5.Vender dolares")
    while True:
        try:
            opcion = int(input("\nTu seleccion: "))
            if opcion in [1,2,3,4,5]:
                if opcion == 1:
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].consultar_saldo()
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].consultar_saldo()
                elif opcion == 2:
                    monto = int(input("\nIngrese el monto a depositar: "))
                    if moneda == "pesos":
                        usuario.cajas_ahorro_pesos[num_caja].depositar(monto)
                    else:
                        usuario.cajas_ahorro_dolares[num_caja].depositar(monto)
                elif opcion == 3:
                    monto = int(input("\nIngrese el monto a transferir: "))
                    n=0
                    for contacto in lista_contactos:
                        n+=1
                        print(f"{n}. {contacto.nombre} {contacto.apellido}")
                    beneficiario = int(input("\nIngrese el numero del beneficiario: "))
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
                elif opcion == 5:
                    if moneda == "pesos":
                        if len(usuario.cajas_ahorro_dolares) != 0:
                            while True:
                                try:
                                    monto = int(input("\nIngrese el monto de dolares a comprar: "))
                                    break
                                except ValueError:
                                    print("\nIngrese un numero")
                            print("\nOpciones:")
                            for caja in usuario.cajas_ahorro_dolares:
                                print(f"\n {caja.numero}")
                            while True:
                                try:
                                    nro = int(input("\nIngrese el numero de la cuenta que desea utilizar: "))
                                    if nro > 0 and nro <= len(usuario.cajas_ahorro_dolares):
                                        break
                                    else:
                                        print("\nIngrese el numero de la cuenta donde desea depositar los dolares")
                                except ValueError:
                                    print("\nIngrese un numero")
                            usuario.cajas_ahorro_pesos[num_caja].comprar_vender_dolares(monto,usuario.cajas_ahorro_dolares[nro-1])
                        else:
                            print("\nUna cuenta de ahorro en dolares es necesaria para comprar dolares")
                    else:
                        while True:
                            try:
                                monto = int(input("\nIngrese el monto de dolares a vender: "))
                                break
                            except ValueError:
                                print("\nIngrese un numero")
                            print("\nOpciones:")
                            for caja in usuario.cajas_ahorro_pesos:
                                print(f"\n {caja.numero}")
                        while True:
                            try:
                                nro = int(input("\nIngrese el numero de la cuenta que desea utilizar: "))
                                if nro > 0 and nro <= len(usuario.cajas_ahorro_pesos):
                                    break
                                else:
                                    print("\nIngrese el numero de la cuenta donde desea depositar los pesos")
                            except ValueError:
                                print("\nIngrese un numero")
                            usuario.cajas_ahorro_dolares[num_caja].comprar_vender_dolares(monto,usuario.cajas_ahorro_pesos[nro-1])
                break
            else:
                print("\nIngrese un numero entre 1 y 5")
        except ValueError:
            print("\nPorfavor ingrese un numero.")