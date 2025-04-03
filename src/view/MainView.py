import os

class MainView:
    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_menu_principal(self, username: str) -> None:
        """
        Muestra el panel principal para el usuario autenticado.
        """
        while True:
            self.clear_screen()
            print(f"=== Panel Principal - Bienvenido {username} ===")
            print("1. Cambiar contraseña")
            print("2. Imprimir resumen de gastos (ejemplo)")
            print("3. Cerrar sesión")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '1':
                # Aquí se implementaría la funcionalidad de cambio de contraseña.
                print("Funcionalidad de cambio de contraseña pendiente de implementar.")
                input("Presione Enter para continuar...")
            elif opcion == '2':
                # Aquí se implementaría la funcionalidad de resumen de gastos.
                print("Funcionalidad de resumen de gastos (pendiente de implementar).")
                input("Presione Enter para continuar...")
            elif opcion == '3':
                print("Cerrando sesión...")
                input("Presione Enter para continuar...")
                break
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")