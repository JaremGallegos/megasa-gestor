from src.model.CategoriaLaboral import CategoriaLaboral
import os

class MainView:
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_principal(self, username: str, rol: CategoriaLaboral) -> tuple[str, CategoriaLaboral] | None:
        """
        Muestra el panel principal para el usuario autenticado.
        """
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Principal - Bienvenido {username} ({rol.value[1]}) ===")
            if rol.value[1] == "Director Campaña":
                print("1. Mantener Datos Cliente")
                print("2. Gastionar Campaña Publicitaria")
                print("3. Gestionar Anuncio")
                print("4. Gestionar Gastos")
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
            
            if opcion == '1':
                if rol.value[1] == "Director Campaña":
                    return username, rol
                elif rol.value[1] == "Personal Contacto":
                    return username, rol
                elif rol.value[1] == "Personal Creativo":
                    return username, rol
                elif rol.value[1] == "Personal Contable":
                    return username, rol
            elif opcion == '2':
                if rol.value[1] == "Director Campaña":
                    return username, rol
                elif rol.value[1] == "Personal Contacto":
                    return username, rol
                elif rol.value[1] == "Personal Contable":
                    return username, rol
            elif opcion == '3':
                if rol.value[1] == "Director Campaña":
                    return username, rol
            elif opcion == '4':
                if rol.value[1] == "Director Campaña":
                    return username, rol
            elif opcion == '9':
                pass
            elif opcion == '0':
                print("Cerrando sesión...")
                input("Presione Enter para continuar...")
                break
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")