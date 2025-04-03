from src.controller.UsuarioController import UsuarioController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class UsuarioView:
    def __init__(self):
        self.controller = UsuarioController()
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_login(self) -> tuple[str, CategoriaLaboral] | None:
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
                    usuario = self.controller.usuarios.get(username)
                    rol = usuario.rol if usuario is not None else None
                    print("Inicio de sesión exitoso.")
                    input("Presione Enter para continuar...")
                    return username, rol
                else:
                    print("Credenciales incorrectas. Intente nuevamente.")
                    input("Presione Enter para continuar...")
            elif opcion == '2':
                username = input("Ingrese nuevo usuario: ")
                password = input("Ingrese nueva contraseña: ")
                nombre = input("Ingrese nombre completo: ")
                email = input("Ingrese email: ")
                
                print("Seleccione una categoria laboral:")
                for rol in CategoriaLaboral:
                    print(f"{rol.value[0]}. {rol.value[1]}")
                    
                rol_input = input("Ingrese el número correspondiente a la categoría: ")
                rol_seleccionado = None
                for rol in CategoriaLaboral:
                    if str(rol.value[0]) == rol_input:
                        rol_seleccionado = rol
                        break
                
                if rol_seleccionado is None:
                    print("Categoría laboral no válida.")
                    input("Presione Enter para continuar...")
                else:
                    if self.controller.registrar_usuario(nombre, email, username, password, rol_seleccionado):
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