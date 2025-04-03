from src.model.CategoriaLaboral import CategoriaLaboral
import os

class MainView:
    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_principal(self, username: str, rol: CategoriaLaboral) -> None:
        """
        Muestra el panel principal para el usuario autenticado.
        """
        while True:
            self.clear_screen()
            print(f"=== Panel Principal - Bienvenido {username} ({rol.value[1]}) ===")
            if rol.value[1] == "Director Campaña":
                print("1. Mantener Datos Cliente")
                print("2. Gastionar Campaña Publicitaria")
                print("3. Gestionar Anuncio")
                print("4. Gestionar Gastos")
            elif rol.value[1] == "Personal Contacto":
                print("1. Gestionar Anuncio")
                print("2. Gestionar Anuncio")
            elif rol.value[1] == "Personal Contacto":
                print("1. Gestionar Campañaaa")
            elif rol.value[1] == "Personal Creativo":
                print("1. Gestionar Anuncio")
            print("________________________________________________")
            print("9. Cambiar contraseña")
            print("0. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                # Aquí se implementaría la funcionalidad de cambio de contraseña.
                pass
            elif opcion == '2':
                print("Cerrando sesión...")
                input("Presione Enter para continuar...")
                break
            elif opcion == '3':
                pass
            elif opcion == '4':
                pass
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")