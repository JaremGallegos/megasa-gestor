from src.model.CategoriaLaboral import CategoriaLaboral
from src.controller.UsuarioController import UsuarioController
import os

class MainView:
    def __init__(self) -> None:
        self.controller = UsuarioController()
    
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_principal(self, username: str, rol: CategoriaLaboral) -> str | None:
        """
        Muestra el panel principal para el usuario autenticado.
        """
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Principal - Bienvenido {username} ({rol.value[1]}) ===")
            
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
            
            print("________________________________________________")
            print("9. Cambiar contraseña")
            print("0. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '0':
                print("Cerrando sesión...")
                input("Presione Enter para continuar...")
                return None
            elif opcion == '9':
                self.cambiar_password(username)
                print("Funcionalidad de cambio de contraseña pendiente de implementar.")
                input("Presione Enter para continuar...")
                continue
            else:
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
        Lógica de cambio de contraseña para el usuario autenticado.
        """
        print("\n--- Cambio de Contraseña ---")
        nueva = input("Ingrese nueva contraseña: ")
        confirmacion = input("Confirme nueva contraseña: ")
        
        if nueva != confirmacion:
            print("Las contraseñas no coinciden. Intente nuevamente.")
        elif len(nueva) < 4:
            print("La contraseña debe tener al menos 4 caracteres.")
        else:
            actualizado = self.controller.cambiar_password(username, nueva)
            if actualizado:
                print("Contraseña actualizada con éxito.")
            else:
                print("Error al actualizar la contraseña.")
        input("Presione Enter para continuar...")