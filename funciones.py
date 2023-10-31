
def calcular_monto_total(precio, monto):
    # Calcula el monto total a pagar, incluyendo impuestos, dado el precio unitario y la cantidad.

    # Args:
    #     precio (float): El precio unitario del producto.
    #     monto (int): La cantidad de productos a comprar.

    # Returns:
    #     float: El monto total a pagar, incluyendo impuestos.

    x = precio * monto
    impuesto_pais = 0.25
    impuesto_ganancias = 0.35
    return x * (impuesto_pais + impuesto_ganancias + 1)


def descontar_comision(monto, comision):
    # Calcula el monto después de descontar una comisión.

    # Args:
    #     monto (float): El monto original.
    #     comision (float): El porcentaje de comisión a descontar.

    # Returns:
    #     float: El monto después de descontar la comisión.

    return monto * (1 - comision)


def calcular_monto_plazo_fijo(monto):
    # Calcula el monto final de un plazo fijo, incluyendo intereses.

    # Args:
    #     monto (float): El monto inicial del plazo fijo.

    # Returns:
    #     float: El monto final del plazo fijo, incluyendo intereses.

    interes = 0.05
    return monto * (interes + 1)
