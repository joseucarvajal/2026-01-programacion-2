from usuario import Usuario
from tienda import Tienda

tienda = Tienda()

def main():
    while True:
        print("1. Registrar un turno de usuario")
        print("2. Atender un usuario")
        print("3. Consultar el usuario que sigue en el turno")
        print("4. Consultar todos los turnos pendientes")
        print("5. Salir")
        opcion = input("Digite una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese nombre: ")
            tipo_tramite = int(input("Seleccione un trámite: 0: Viene a comprar (compras) de contado, 1: Viene a pagar una deuda, 2: Viene a pedir crédito (fiado): ")) 
            monto_transaccion = float(input("Ingrese el monto de la transaccion: "))
            usuario = Usuario()
            usuario.nombre = nombre
            usuario.tipo_tramite = tipo_tramite
            usuario.monto_transaccion = monto_transaccion
            tienda.encolar_usuario(usuario)
        elif opcion == "2":
            tienda.atender_siguiente_usuario()
        elif opcion == "3":
            tienda.consultar_siguiente_usuario()
        elif opcion == "4":
            tienda.consultar_cola_de_usuarios()
        elif opcion == "5":
            break


if __name__ == "__main__":
    main()