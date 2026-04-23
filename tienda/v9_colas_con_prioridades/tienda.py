
from collections import deque
from usuario import Usuario

class Tienda:
    nombre: str = ''
    cola_pagos_deudas: deque[Usuario] = deque()
    cola_compras_a_contado: deque[Usuario] = deque()
    cola_pedidos_credito: deque[Usuario] = deque()

    def encolar_usuario(self, usuario:Usuario):
        if usuario.tipo_tramite == 0: #Viene a comprar de contado
            self.cola_compras_a_contado.append(usuario)
        elif usuario.tipo_tramite == 1: #Viene a pagar deudas
            self.cola_pagos_deudas.append(usuario)
        elif usuario.tipo_tramite == 2: #Viene a pedir crédito
            self.cola_pedidos_credito.append(usuario)

    '''
        Hay un problema con esta implementación, si llega un usuario a pedir crédito
        pero siguen llegando personas a comprar de contado y a pagar deudas
        el usuario que pidió crédito nunca va a ser atendido, porque siempre van a haber usuarios en las otras colas

        Esto se soluciona implementando diferentes algoritmos de prioridad:
            - Round Robin: Se atiende un usuario de cada cola de forma rotativa, 
                es decir, se atienden 3 usuario de la cola de pagos deudas, 
                luego 2 usuarios de la cola de compras a contado, 
                luego 1 usuario de la cola de pedidos crédito, y así sucesivamente.
    '''
    def atender_siguiente_usuario(self):
        if len(self.cola_pagos_deudas) > 0:
            usuario = self.cola_pagos_deudas.popleft()
            print(f"En la tienda {self.nombre}: Se atiende el usuario: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion} por pagar una deuda")
            return usuario
        elif len(self.cola_compras_a_contado) > 0:
            usuario = self.cola_compras_a_contado.popleft()
            print(f"En la tienda {self.nombre}: Se atiende el usuario: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion} por comprar de contado")
            return usuario
        elif len(self.cola_pedidos_credito) > 0:
            usuario = self.cola_pedidos_credito.popleft()
            print(f"En la tienda {self.nombre}: Se atiende el usuario: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion} por pedir crédito")
            return usuario
        else:
            print(f"En la tienda {self.nombre}: No hay usuarios para atender")
            return None
        
    def consultar_siguiente_usuario(self):
        if len(self.cola_pagos_deudas) > 0:
            usuario = self.cola_pagos_deudas[0]
            print(f"En la tienda {self.nombre}: El siguiente usuario a atender es: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion} por pagar una deuda")
        elif len(self.cola_compras_a_contado) > 0:
            usuario = self.cola_compras_a_contado[0]
            print(f"En la tienda {self.nombre}: El siguiente usuario a atender es: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion} por comprar de contado")
        elif len(self.cola_pedidos_credito) > 0:
            usuario = self.cola_pedidos_credito[0]
            print(f"En la tienda {self.nombre}: El siguiente usuario a atender es: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion} por pedir crédito")
        else:
            print(f"En la tienda {self.nombre}: No hay usuarios para consultar")

    def consultar_cola_de_usuarios(self):
        print(f"En la tienda {self.nombre}: Cola de usuarios por pagar deudas: {[usuario.nombre for usuario in self.cola_pagos_deudas]}")
        print(f"En la tienda {self.nombre}: Cola de usuarios por comprar de contado: {[usuario.nombre for usuario in self.cola_compras_a_contado]}")
        print(f"En la tienda {self.nombre}: Cola de usuarios por pedir crédito: {[usuario.nombre for usuario in self.cola_pedidos_credito]}")





