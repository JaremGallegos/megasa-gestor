from src.controller.UsuarioController import UsuarioController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class UsuarioView:
    def __init__(self):
        """
        Constructor de la clase UsuarioView.
        Inicializa el controlador de usuario para manejar las operaciones relacionadas
        con el login y registro.
        """
        self.controller = UsuarioController()
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal para ofrecer una interfaz limpia.
        Usa 'cls' en Windows y 'clear' en sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_login(self) -> tuple[str, CategoriaLaboral] | None:
        """
        Muestra el menú de login y registro inicial.
        
        Opciones del menú:
            1. Iniciar sesión
            2. Registrar nuevo usuario
            3. Salir
        
        Retorna:
            - Una tupla (username, rol) si la autenticación es exitosa, donde:
                - username (str): Nombre del usuario autenticado.
                - rol (CategoriaLaboral): Categoría laboral asociada al usuario.
            - None, en caso de que el usuario decida salir.
        """
        while True:
            # Limpia la ventana al inicio de cada iteración del menú
            self.limpiar_ventana()
            
            # Muestra el encabezado y las opciones disponibles
            print("=== Sistema Mega S.A. - Login ===")
            print("1. Iniciar sesión")
            print("2. Registrar nuevo usuario")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            
            # Opción para iniciar sesión
            if opcion == '1':
                username = input("Usuario: ")
                password = input("Contraseña: ")
                # Valida las credenciales mediante el controlador
                if self.controller.autentificar(username, password):
                    usuario = self.controller.usuarios.get(username)
                    rol = usuario.rol if usuario is not None else None
                    print("Inicio de sesión exitoso.")
                    input("Presione Enter para continuar...")
                    return username, rol
                else:
                    print("Credenciales incorrectas. Intente nuevamente.")
                    input("Presione Enter para continuar...")
                    
            # Opción para registrar un nuevo usuario
            elif opcion == '2':
                username = input("Ingrese nuevo usuario: ")
                password = input("Ingrese nueva contraseña: ")
                nombre = input("Ingrese nombre completo: ")
                email = input("Ingrese email: ")
                
                # Muestra las opciones de categoría laboral disponibles
                print("Seleccione una categoria laboral:")
                for rol in CategoriaLaboral:
                    print(f"{rol.value[0]}. {rol.value[1]}")
                    
                rol_input = input("Ingrese el número correspondiente a la categoría: ")
                rol_seleccionado = None
                
                # Verifica que la opción ingresada corresponda a alguna categoría laboral
                for rol in CategoriaLaboral:
                    if str(rol.value[0]) == rol_input:
                        rol_seleccionado = rol
                        break
                
                # Valida la selección de la categoría laboral
                if rol_seleccionado is None:
                    print("Categoría laboral no válida.")
                    input("Presione Enter para continuar...")
                else:
                    # Intenta registrar al nuevo usuario mediante el controlador
                    if self.controller.registrar_usuario(nombre, email, username, password, rol_seleccionado):
                        print("Usuario registrado exitosamente.")
                    else:
                        print("El usuario ya existe.")
                    input("Presione Enter para continuar...")
            
            # Opción para salir del sistema
            elif opcion == '3':
                print("Saliendo...")
                input("Presione Enter para continuar...")
                return None
            
            # Manejo de opción no válida
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")