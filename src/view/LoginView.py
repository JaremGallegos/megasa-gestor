from src.controller.UsuarioController import UsuarioController
import os

class UsuarioView:
    def __init__(self):
        self.controller = UsuarioController()
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_login(self) -> str | None:
        """
        Muestra el menu de login y registro inicial.
        Devuelve el nombre de usuario autenticado o None si se sale.
        """
        while True:
            self.limpiar_ventana()
            print("=== Sistema Mega S.A. - Login ===")
            print("1. Iniciar sesión")
            print("2. Registrar nuevo usuario")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                username = input("Usuario: ")
                password = input("Contraseña: ")
                if self.controller.autentificar(username, password):
                    print("Inicio de sesión exitoso.")
                    input("Presione Enter para continuar...")
                    return username
                else:
                    print("Credenciales incorrectas. Intente nuevamente.")
                    input("Presione Enter para continuar...")
            elif opcion == '2':
                username = input("Ingrese nuevo usuario: ")
                password = input("Ingrese nueva contraseña: ")
                if self.controller.registrar_usuario(username, password):
                    print("Usuario registrado exitosamente.")
                else:
                    print("El usuario ya existe.")
                input("Presione Enter para continuar...")
            elif opcion == '3':
                print("Saliendo...")
                input("Presione Enter para continuar...")
                return None
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")