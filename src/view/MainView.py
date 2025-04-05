from src.model.CategoriaLaboral import CategoriaLaboral
from src.controller.UsuarioController import UsuarioController
import os

class MainView:
    def __init__(self) -> None:
        """
        Constructor de la clase MainView.
        Inicializa el controlador de usuario para manejar las operaciones relacionadas.
        """
        self.controller = UsuarioController()
    
    def limpiar_ventana(self) -> None:
        """
        Limpia la consola, dependiendo del sistema operativo.
        Utiliza 'cls' para Windows y 'clear' para sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_principal(self, username: str, rol: CategoriaLaboral) -> str | None:
        """
        Muestra el panel principal para el usuario autenticado según su rol.
        
        Parámetros:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Objeto que representa la categoría laboral del usuario.
        
        Retorna:
            str | None: Cadena que indica la acción seleccionada o None para cerrar sesión.
        """
        while True:
            # Limpia la consola al inicio de cada iteración del menú
            self.limpiar_ventana()
            # Muestra encabezado con el nombre del usuario y su rol
            print(f"=== Panel Principal - Bienvenido {username} ({rol.name}) ===")
            
            # Verifica el rol del usuario y muestra las opciones correspondientes
            if rol.value[1] == "Director Campaña":
                print("1. Mantener Datos Cliente")
                print("2. Gestionar Campaña Publicitaria")
                print("3. Gestionar Anuncio")
                print("4. Calcular Nomina")
            elif rol.value[1] == "Personal Contacto":
                print("1. Gestionar Anuncio")
                print("2. Gestionar Empleados")
            elif rol.value[1] == "Personal Creativo":
                print("1. Gestionar Ideas de Anuncio")
            elif rol.value[1] == "Personal Contable":
                print("1. Mantener Categoria Laboral")
                print("2. Mantener Empleados")
                
            # Opciones adicionales para cambio de contraseña y cierre de sesión
            print("________________________________________________")
            print("9. Cambiar contraseña")
            print("0. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            
            # Opción para cerrar sesión
            if opcion == '0':
                print("Cerrando sesión...")
                input("Presione Enter para continuar...")
                return None
            # Opción para cambiar la contraseña
            elif opcion == '9':
                self.cambiar_password(username)
                print("Funcionalidad de cambio de contraseña pendiente de implementar.")
                input("Presione Enter para continuar...")
                continue
            else:
                # Procesa las opciones según el rol del usuario
                if rol.value[1] == "Director Campaña":
                    if opcion == '1':
                        return "cliente"
                    elif opcion == '2':
                        return "campana"
                    elif opcion == '3':
                        return "anuncio"
                    elif opcion == '4':
                        return "nomina"
                    else:
                        print("Opción no válida.")
                        input("Presione Enter para continuar...")
                elif rol.value[1] == "Personal Contacto":
                    if opcion == '1':
                        return "anuncio"
                    elif opcion == '2':
                        return "empleados"
                    else:
                        print("Opción no válida.")
                        input("Presione Enter para continuar...")
                elif rol.value[1] == "Personal Creativo":
                    if opcion == '1':
                        return "ideas"
                    else:
                        print("Opción no válida.")
                        input("Presione Enter para continuar...")
                elif rol.value[1] == "Personal Contable":
                    if opcion == '1':
                        return "categoria"
                    elif opcion == '2':
                        return "empleados"
                    else:
                        print("Opción no válida.")
                        input("Presione Enter para continuar...")
                        
    def cambiar_password(self, username: str) -> None:
        """
        Permite al usuario cambiar su contraseña.
        
        Parámetros:
            username (str): Nombre del usuario que desea cambiar su contraseña.
            
        El método solicita la nueva contraseña y su confirmación, valida que sean iguales
        y cumplan con los requisitos mínimos (por ejemplo, longitud mínima) y llama al controlador
        para realizar la actualización.
        """
        print("\n--- Cambio de Contraseña ---")
        # Solicita la nueva contraseña y su confirmación
        nueva = input("Ingrese nueva contraseña: ")
        confirmacion = input("Confirme nueva contraseña: ")
        
        # Valida que ambas contraseñas coincidan
        if nueva != confirmacion:
            print("Las contraseñas no coinciden. Intente nuevamente.")
        # Valida que la contraseña tenga al menos 4 caracteres
        elif len(nueva) < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
        else:
            # Llama al controlador para actualizar la contraseña en la base de datos o backend
            actualizado = self.controller.cambiar_password(username, nueva)
            if actualizado:
                print("Contraseña actualizada con éxito.")
            else:
                print("Error al actualizar la contraseña.")
        input("Presione Enter para continuar...")