from clientes import ClienteBlack, ClienteClassic, ClienteGold
from funciones_interfaz.opciones_cuenta_ahorro import opciones_cuentas_ahorro
from funciones_interfaz.opciones_cuenta_inversion import opciones_cuenta_inversion
from funciones_interfaz.opciones_cuentas_corrientes import opciones_cuentas_corrientes
from funciones_interfaz.opciones_tarjeta_credito import opciones_tarjetas_credito
from output_html_file import create_html_file
from resumen import Resumen

def pedir_informacion_cliente(cuenta):
    nombre = input("\nIngrese su nombre: ")
    apellido = input("\nIngrese su apellido: ")
    
    while True:
        dni = input("\nIngrese su numero de DNI: ")
        
        try:
            dni = int(dni)
            dni_str = str(dni)  # Convert dni to a string
            
            if len(dni_str) == 8:  # Check the length of dni_str
                print("\nCuenta creada")
                if cuenta == 1:
                    usuario = ClienteClassic(nombre, apellido, dni, 10001)
                elif cuenta == 2:
                    usuario = ClienteGold(nombre, apellido, dni, 20001)
                else:
                    usuario = ClienteBlack(nombre, apellido, dni, 30001)
                break  # Break the loop when the DNI is valid
            else:
                print("\nEl DNI debe tener 8 digitos")
            
        except ValueError:
            print("\nDNI invalido. Ingresa un numero.")
    
    return usuario







def main_menu(usuario):
    while True:
        while True:
            try:
                print("\nOpciones:\n \n0.Salir\n1.Cuentas de Ahorro")
                if not isinstance(usuario,ClienteClassic):
                    producto = int(input("2.Cuentas Corrientes\n3.Tarjetas de Credito\n4.Cuenta de Inversion\n\nTu seleccion (0-4): "))
                else:
                    producto = int(input("\nTu seleccion (0-1): "))
                break
            except ValueError:
                print("\nIngrese un numero.")
        if producto == 0:
            break
        if producto == 1:
            opciones_cuentas_ahorro(usuario)
        elif producto == 2 and not isinstance(usuario,ClienteClassic):
            opciones_cuentas_corrientes(usuario)
        elif producto == 3 and not isinstance(usuario,ClienteClassic):
            opciones_tarjetas_credito(usuario)
        elif producto == 4 and not isinstance(usuario,ClienteClassic):
            opciones_cuenta_inversion(usuario)
    print("\nVuelva pronto!\n \nPuede encontrar un resumen de las operaciones realizadas en resumen.html")
    create_html_file(usuario.resumen.get_resumen())


def main():
    print("\nSelecciona el tipo de cuenta que deseas crear\n \n1. Classic\n2. Gold\n3. Black")

    while True:
        try:
            choice = int(input("\nIngresa el numero (1-3): "))
            if choice >= 1 and choice <= 3:
                break
            else:
                print("\nIngrese un numero del 1 al 3.")
        except ValueError:
            print("\nIngrese un numero.")

    if choice == 1:
        print("\nSeleccionaste la cuenta Classic.")
        
    elif choice == 2:
        print("\nSeleccionaste la cuenta Gold.")
    elif choice == 3:
        print("\nSeleccionaste la cuenta Black.")
    usuario = pedir_informacion_cliente(choice)
    usuario.resumen = Resumen(usuario)
    main_menu(usuario)
    return 


