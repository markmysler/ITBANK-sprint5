from cajas_ahorro import CajaDeAhorro
from chequera import Chequera
from cuenta_corriente import CuentaCorriente
from tarjetas_debito import TarjetaDeDebito
from tarjetas_credito import Extension, TarjetaCredito


class Cliente:
    def __init__(self, nombre, apellido, dni, numero_cuenta, max_cajas_de_ahorro, comision_saliente, comision_entrante, limite_retiros_sin_cargo, limite_retiro_por_dia, max_cuentas_corrientes, acceso_cuenta_inversion, proveedores_credito_habilitados, limite_credito_un_pago, limite_credito_cuotas, max_extensiones_credito, max_tarjetas_debito, max_chequeras):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.cajas_ahorro_pesos = [CajaDeAhorro("pesos", 1)]
        self.cajas_ahorro_dolares = []
        self.max_cajas_de_ahorro = max_cajas_de_ahorro
        self.comision_saliente = comision_saliente
        self.comision_entrante = comision_entrante
        self.limite_retiros_sin_cargo = limite_retiros_sin_cargo
        self.limite_retiro_por_dia = limite_retiro_por_dia
        self.cuentas_corrientes_pesos = []
        self.cuentas_corrientes_dolares = []
        self.max_cuentas_corrientes = max_cuentas_corrientes
        self.acceso_cuenta_inversion = acceso_cuenta_inversion
        self.cuenta_de_inversion = None
        self.tarjetas_credito = []
        self.proveedores_credito_habilitados = proveedores_credito_habilitados
        self.limite_credito_un_pago = limite_credito_un_pago
        self.limite_credito_cuotas = limite_credito_cuotas
        self.max_extensiones_credito = max_extensiones_credito
        self.total_extensiones = 0
        self.tarjetas_debito = 0
        self.max_tarjetas_debito = max_tarjetas_debito
        self.chequeras = 0
        self.max_chequeras = max_chequeras

    def crear_caja_de_ahorro(self, moneda):
        if moneda == "pesos":
            if len(self.cajas_ahorro_pesos) + len(self.cajas_ahorro_dolares) < self.max_cajas_de_ahorro:
                self.cajas_ahorro_pesos.append(CajaDeAhorro(
                    "pesos", len(self.cajas_ahorro_pesos)+1))
                print("\nCaja de ahorro en pesos creada")
            else:
                print("\nNo se pueden crear mas cajas de ahorro en pesos")
        else:
            if len(self.cajas_ahorro_dolares) + len(self.cajas_ahorro_pesos) < self.max_cajas_de_ahorro:
                self.cajas_ahorro_dolares.append(CajaDeAhorro(
                    "dolares", len(self.cajas_ahorro_dolares)+1))
                print("\nCaja de ahorro en dolares creada")
            else:
                print("\nNo se pueden crear mas cajas de ahorro en dolares")

    def crear_cuenta_corriente(self, moneda):
        if moneda == "pesos":
            if len(self.cuentas_corrientes_pesos) + len(self.cuentas_corrientes_dolares) < self.max_cuentas_corrientes:
                self.cuentas_corrientes_pesos.append(CuentaCorriente(
                    "pesos", len(self.cuentas_corrientes_pesos)+1, self))
                print("\nCuenta corriente en pesos creada")
            else:
                print("\nNo se pueden crear mas cuentas corrientes en pesos")
        else:
            if len(self.cuentas_corrientes_dolares) + len(self.cuentas_corrientes_pesos) < self.max_cuentas_corrientes:
                self.cuentas_corrientes_dolares.append(CuentaCorriente(
                    "dolares", len(self.cuentas_corrientes_dolares)+1, self))
                print("\nCuenta corriente en dolares creada")

    def agregar_tarjeta_credito(self, emisor):
        if self.proveedores_credito_habilitados != None:
            if emisor in self.proveedores_credito_habilitados:
                if self.existe_tarjeta_emisor(emisor) == False:
                    self.tarjetas_credito.append(TarjetaCredito(len(
                        self.tarjetas_credito)+1, self.limite_credito_cuotas, self.limite_credito_un_pago, emisor))
                    print(f"\nTarjeta de credito {emisor} agregada")
                else:
                    print("\nYa tienes una tarjeta de credito de este emisor")
            else:
                print("\nEmisor de tarjeta de credito no disponible")
        else:
            print("\nNo tienes acceso a tarjetas de credito")

    def existe_tarjeta_emisor(self, emisor):
        for tarjeta in self.tarjetas_credito:
            if tarjeta.emisor == emisor:
                return True
        return False

    def asociar_tarjeta_debito_caja_ahorro(self, caja):
        if self.tarjetas_debito < self.max_tarjetas_debito:
            caja.tarjeta_debito = TarjetaDeDebito(caja)
            print("\nTarjeta asociada")
        else:
            print("\nAlcanzaste el limite de tarjetas de debito para esta cuenta")
    def asociar_chequera_cuenta_corriente(self, cuenta):
        if self.chequeras < self.max_chequeras:
            cuenta.chequera = Chequera(cuenta)
            print("\nChequera asociada")
        else:
            print("\nAlcanzaste el limite de chequeras para esta cuenta")
    def agregar_extension_tarjeta(self, tarjeta):
        if self.total_extensiones < self.max_extensiones_credito:
            tarjeta.extensiones.append(Extension(tarjeta))
            print("\nExtension asociada exitosamente")
        else:
            print("\nAlcanzaste el limite de extensiones para esta cuenta")

class ClienteClassic(Cliente):
    def __init__(self, nombre, apellido, dni, numero_cuenta):
        super().__init__(nombre, apellido, dni, numero_cuenta,
                         2, 0.1, 0.05, 5, 10000, 0, False, None, 0, 0, 0, 1,0)


class ClienteGold(Cliente):
    def __init__(self, nombre, apellido, dni, numero_cuenta):
        super().__init__(nombre, apellido, dni, numero_cuenta, 2, 0.05, 0.01,
                         None, 20000, 1, True, ["Visa", "Master Card"], 150000, 100000, 5, 1,1)


class ClienteBlack(Cliente):
    def __init__(self, nombre, apellido, dni, numero_cuenta):
        super().__init__(nombre, apellido, dni, numero_cuenta, 5, 0, 0, None, 100000,
                         3, True, ["Visa", "Master Card", "American Express"], 500000, 600000, 10, 5,2)
