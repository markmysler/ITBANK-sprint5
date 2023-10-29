from clientes import ClienteBlack, ClienteClassic, ClienteGold
from funciones_interfaz.opciones_cuenta_ahorro import opciones_cuentas_ahorro
from funciones_interfaz.opciones_cuentas_corrientes import opciones_cuentas_corrientes

def pedir_informacion_cliente(cuenta):
    nombre = input("Ingrese su nombre: ")
    last_nombre = input("Ingrese su last nombre: ")
    
    while True:
        dni = input("Ingrese su numero de DNI: ")
        
        try:
            dni = int(dni)
            dni_str = str(dni)  # Convert dni to a string
            
            if len(dni_str) == 8:  # Check the length of dni_str
                print("Creando cuenta")
                if cuenta == 1:
                    usuario = ClienteClassic(nombre, last_nombre, dni, 10001)
                elif cuenta == 2:
                    usuario = ClienteGold(nombre, last_nombre, dni, 20001)
                else:
                    usuario = ClienteBlack(nombre, last_nombre, dni, 30001)
                break  # Break the loop when the DNI is valid
            else:
                print("El DNI debe tener 8 digitos")
            
        except ValueError:
            print("DNI invalido. Ingresa un numero.")
    
    return usuario







def main_menu(usuario):
    while True:
        try:
            print("Selecciona el producto sobre el que queres operar:\n1.Cuentas de Ahorro")
            if not isinstance(usuario,ClienteClassic):
                producto = int(input("2.Cuentas Corrientes\n3.Tarjetas de Credito\n4.Cuenta de Inversion\n"))
            else:
                producto = int(input(""))
            break
        except ValueError:
            print("Porfavor ingrese un numero.")
    if producto == 1:
        opciones_cuentas_ahorro(usuario)
    elif producto == 2 and not isinstance(usuario,ClienteClassic):
        opciones_cuentas_corrientes(usuario)
    # elif producto == 3 and not isinstance(usuario,ClienteClassic):
    #     opciones_tarjetas_de_credito(usuario)
    # elif producto == 4 and not isinstance(usuario,ClienteClassic):
    #     opciones_cuenta_de_inversion(usuario)


def main():
    print("Selecciona el tipo de cuenta que deseas crear\n1. Classic\n2. Gold\n3. Black")

    while True:
        choice = input("Ingresa el numero (1-3): ")

        try:
            choice = int(choice)
            if choice >= 1 and choice <= 3:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

    if choice == 1:
        print("You have selected the Classic Account.")
    elif choice == 2:
        print("You have selected the Gold Account.")
    elif choice == 3:
        print("You have selected the Black Account.")
    usuario = pedir_informacion_cliente(choice)
    main_menu(usuario)
    return 

if __name__ == "__main__":
    main()

