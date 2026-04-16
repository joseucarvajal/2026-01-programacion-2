'''

1. Crear la cola vacía
cola_de_usuarios = deque() = []
=======================================================================================================================================
1. encolar - append usuarios
cola_de_usuarios.append(Juan)
cola_de_usuarios = [Juan]
                     0

cola_de_usuarios.append(Pepito)
cola_de_usuarios = [Juan, Pepito]
                      0     1   

cola_de_usuarios.append(Maria)
cola_de_usuarios = [Juan, Pepito, Maria]
                      0     1       2  

cola_de_usuarios.append(Yaneth)
cola_de_usuarios = [Juan, Pepito, Maria, Yaneth]
                      0     1       2      3   
cola_de_usuarios.append(Miguel)
cola_de_usuarios = [Juan, Pepito, Maria, Yaneth, Miguel]
                      0     1       2      3       4   

cola_de_usuarios.append(Natalia)
cola_de_usuarios = [Juan, Pepito, Maria, Yaneth, Miguel, Natalia]
                      0     1       2      3       4       5

=======================================================================================================================================
2. Desencolar (popleft) usuarios
- cola_de_usuarios.popleft() => atender y sacar el usuario que está a la cabeza de la cola (más a la izquierda) => Juan
cola_de_usuarios = [Pepito, Maria, Yaneth, Miguel, Natalia]
                      0       1      2       3       4 

- cola_de_usuarios.popleft() => atender y sacar el usuario que está a la cabeza de la cola (más a la izquierda) => Pepito
cola_de_usuarios = [Maria, Yaneth, Miguel, Natalia]
                      0       1      2       3  
=======================================================================================================================================
3. Peek
cola_de_usuarios[0] => Maria
cola_de_usuarios = [Maria, Yaneth, Miguel, Natalia]
                      0       1      2       3  
'''


from collections import deque
from usuario import Usuario

class Tienda:
    nombre: str = ''
    cola_de_usuarios = deque()

    def encolar_usuario(self, usuario:Usuario):
        self.cola_de_usuarios.append(usuario)

    def atender_siguiente_usuario(self):
        usuario = self.cola_de_usuarios.popleft()
        print(f"En la tienda {self.nombre}: Se atiende el usuario: {usuario.nombre} con un monto de transaccion {usuario.monto_transaccion}")
        return usuario
    
    def consultar_siguiente_usuario(self):
        usuario = self.cola_de_usuarios[0]
        print(f"El usuario que sigue es: {usuario.nombre}")
        return usuario
    
    def consultar_cola_de_usuarios(self):
        print("Consultando la cola de usuarios....")
        total_transacciones_pendientes = 0
        total_monto_transacciones_pendientes = 0
        for usuario in self.cola_de_usuarios:
            print(f"Nombre: {usuario.nombre}, Tramite: {usuario.tipo_tramite}, Monto: {usuario.monto_transaccion}")
            total_transacciones_pendientes = total_transacciones_pendientes + 1
            total_monto_transacciones_pendientes = total_monto_transacciones_pendientes + usuario.monto_transaccion
        print(f"El total de transacciones pendientes es: {total_transacciones_pendientes}")
        print(f"El total de dinero pendiente en transacciones es: {total_monto_transacciones_pendientes}")

        



