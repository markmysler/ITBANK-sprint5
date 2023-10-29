def calcular_monto_total(precio, monto):
    x = precio*monto
    impuesto_pais = 0.25
    impuesto_ganancias = 0.35
    return x*(impuesto_pais + impuesto_ganancias + 1)


def descontar_comision(monto, comision):
    return monto*(1-comision)


def calcular_monto_plazo_fijo(monto):
    interes = 0.05
    return monto*(interes + 1)
