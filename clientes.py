from cajas_ahorro import CajaDeAhorro
from chequera import Chequera
from cuenta_corriente import CuentaCorriente
from transaccion import Transaccion
from tarjetas_debito import TarjetaDeDebito
from tarjetas_credito import Extension, TarjetaCredito


class Cliente:
    def __init__(self, nombre, apellido, dni, numero_cuenta, max_cajas_de_ahorro, comision_saliente, comision_entrante, limite_retiros_sin_cargo, limite_retiro_por_dia, max_cuentas_corrientes, acceso_cuenta_inversion, proveedores_credito_habilitados, limite_credito_un_pago, limite_credito_cuotas, max_extensiones_credito, max_tarjetas_debito, max_chequeras):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.cajas_ahorro_pesos = [CajaDeAhorro("pesos", 1,self)]
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
        self.resumen = None
        self.monto_retirado_cajeros = 0

    def crear_caja_de_ahorro(self, moneda):
        if moneda == "pesos":
            if len(self.cajas_ahorro_pesos) + len(self.cajas_ahorro_dolares) < self.max_cajas_de_ahorro:
                self.cajas_ahorro_pesos.append(CajaDeAhorro(
                    "pesos", len(self.cajas_ahorro_pesos)+1,self))
                print("\nCaja de ahorro en pesos creada")
                self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_CAJA_AHORRO_PESOS","Caja de ahorro en pesos creada", self))
            else:
                print("\nNo se pueden crear mas cajas de ahorro en pesos")
                self.resumen.add_transaccion(Transaccion("RECHAZADA", "ALTA_CAJA_AHORRO_PESOS", "Se alcanzo el limite de cajas de ahorro para esta cuenta", self))
        else:
            if len(self.cajas_ahorro_dolares) + len(self.cajas_ahorro_pesos) < self.max_cajas_de_ahorro:
                self.cajas_ahorro_dolares.append(CajaDeAhorro(
                    "dolares", len(self.cajas_ahorro_dolares)+1,self))
                print("\nCaja de ahorro en dolares creada")
                self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_CAJA_AHORRO_DOLARES","Caja de ahorro en dolares creada", self))
            else:
                print("\nNo se pueden crear mas cajas de ahorro en dolares")
                self.resumen.add_transaccion(Transaccion("RECHAZADA", "ALTA_CAJA_AHORRO_DOLARES", "Se alcanzo el limite de cajas de ahorro para esta cuenta", self))

    def crear_cuenta_corriente(self, moneda):
        if moneda == "pesos":
            if len(self.cuentas_corrientes_pesos) + len(self.cuentas_corrientes_dolares) < self.max_cuentas_corrientes:
                self.cuentas_corrientes_pesos.append(CuentaCorriente(
                    "pesos", len(self.cuentas_corrientes_pesos)+1, self))
                print("\nCuenta corriente en pesos creada")
                self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_CUENTA_CORRIENTE_PESOS","Cuenta corriente en pesos creada", self))
            else:
                print("\nNo se pueden crear mas cuentas corrientes en pesos")
                self.resumen.add_transaccion(Transaccion("RECHAZADA", "ALTA_CUENTA_CORRIENTE_PESOS", "Se alcanzo el limite de cuentas corrientes para esta cuenta", self))
        else:
            if len(self.cuentas_corrientes_dolares) + len(self.cuentas_corrientes_pesos) < self.max_cuentas_corrientes:
                self.cuentas_corrientes_dolares.append(CuentaCorriente(
                    "dolares", len(self.cuentas_corrientes_dolares)+1, self))
                print("\nCuenta corriente en dolares creada")
                self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_CUENTA_CORRIENTE_DOLARES","Cuenta corriente en dolares creada", self))
            else:
                print("\nNo se pueden crear mas cuentas corrientes en dolares")
                self.resumen.add_transaccion(Transaccion("RECHAZADA", "ALTA_CUENTA_CORRIENTE_DOLARES", "Se alcanzo el limite de cuentas corrientes para esta cuenta", self))

    def agregar_tarjeta_credito(self, emisor):
        if self.proveedores_credito_habilitados != None:
            if emisor in self.proveedores_credito_habilitados:
                if self.existe_tarjeta_emisor(emisor) == False:
                    self.tarjetas_credito.append(TarjetaCredito(len(
                        self.tarjetas_credito)+1, self.limite_credito_cuotas, self.limite_credito_un_pago, emisor, self))
                    print(f"\nTarjeta de credito {emisor} agregada")
                    self.resumen.add_transaccion(Transaccion("ACEPTADA", f"ALTA_TARJETA_CREDITO_{emisor.upper()}",f"Tarjeta de credito {emisor} agregada", self))
                else:
                    print("\nYa tienes una tarjeta de credito de este emisor")
                    self.resumen.add_transaccion(Transaccion("RECHAZADA", f"ALTA_TARJETA_CREDITO_{emisor.upper()}",f"Una tarjeta de credito {emisor} ya esta asociada con esta cuenta", self))
            else:
                print("\nEmisor de tarjeta de credito no disponible")
                self.resumen.add_transaccion(Transaccion("RECHAZADA", f"ALTA_TARJETA_CREDITO_{emisor.upper()}",f"Esta cuenta no tiene acceso a tarjetas de credito {emisor}", self))
        else:
            print("\nNo tienes acceso a tarjetas de credito")
            self.resumen.add_transaccion(Transaccion("RECHAZADA", f"ALTA_TARJETA_CREDITO_{emisor.upper()}","Esta cuenta no tiene acceso a tarjetas de credito", self))

    def existe_tarjeta_emisor(self, emisor):
        for tarjeta in self.tarjetas_credito:
            if tarjeta.emisor == emisor:
                return True
        return False

    def asociar_tarjeta_debito_caja_ahorro(self, caja):
        if self.tarjetas_debito < self.max_tarjetas_debito:
            caja.tarjeta_debito = TarjetaDeDebito(caja)
            print("\nTarjeta de debito asociada")
            self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_TARJETA_DEBITO", f"Tarjeta de debito asociada con la caja de ahorro {caja.numero}", self))
        else:
            print("\nAlcanzaste el limite de tarjetas de debito para esta cuenta")
            self.resumen.add_transaccion(Transaccion("RECHAZADA", "ALTA_TARJETA_DEBITO",f"Alcanzaste el limite de tarjetas de debito para esta cuenta: {self.max_tarjetas_debito}", self))
    def asociar_chequera_cuenta_corriente(self, cuenta):
        if self.chequeras < self.max_chequeras:
            cuenta.chequera = Chequera(cuenta)
            print("\nChequera asociada")
            self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_CHEQUERA", f"Chequera asociada con la cuenta corriente numero {cuenta.numero}", self))
        else:
            print("\nAlcanzaste el limite de chequeras para esta cuenta")
            self.resumen.add_transaccion(Transaccion("RECHAZADA", "ALTA_CHEQUERA", f"Alcanzaste el limite de chequeras para esta cuenta. Limite: {self.max_chequeras}", self))
    def agregar_extension_tarjeta(self, tarjeta):
        if self.total_extensiones < self.max_extensiones_credito:
            tarjeta.extensiones.append(Extension(tarjeta))
            self.total_extensiones += 1
            print("\nExtension asociada exitosamente")
            self.resumen.add_transaccion(Transaccion("ACEPTADA", "ALTA_EXTENSION", f"Extension asociada con la tarjeta de credito {tarjeta.emisor} numero {tarjeta.numero}", self))
        else:
            print("\nAlcanzaste el limite de extensiones para esta cuenta")
            (Transaccion("RECHAZADA", "ALTA_EXTENSION", f"Alcanzaste el limite de extensiones para esta cuenta. Limite: {self.max_extensiones_credito}", self))

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
