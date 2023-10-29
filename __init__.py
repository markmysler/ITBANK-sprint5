from clientes import ClienteBlack, ClienteClassic, ClienteGold


cliente1 = ClienteClassic("Mark", "Mysler", 43084313, 1)
cliente2 = ClienteGold("Gabriel", "Mysler", 00000000, 2)
cliente3 = ClienteBlack("Dana", "Mysler", 11111111, 3)


print(cliente1.cajas_ahorro_pesos[0].consultar_saldo())
cliente2.agregar_tarjeta_credito("Visa")
cliente2.tarjetas_credito[0].pagar_en_cuotas(10000, 6)
cliente2.tarjetas_credito[0].pagar_un_pago(150001)
cliente3.crear_cuenta_corriente("pesos")
