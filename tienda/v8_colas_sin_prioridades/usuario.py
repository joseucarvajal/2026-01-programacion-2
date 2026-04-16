class Usuario:
    nombre: str
    tipo_tramite: int #0: Viene a comprar (compras) de contado, 1: Viene a pagar una deuda, 2: Viene a pedir crédito (fiado)
    monto_transaccion: int = 0