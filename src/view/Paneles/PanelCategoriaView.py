from src.controller.CategoriaLaboralController import CategoriaLaboralController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelCategoriaView:
    def __init__(self) -> None:
        self.controller = CategoriaLaboralController()
        
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_categoria_laboral(self, username: str, rol: CategoriaLaboral) -> None:
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Configuración de Categorías - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Listar categorías laborales")
            print("2. Actualizar sueldo base de una categoría")
            print("3. Salir")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                config = self.controller.listar_categorias()
                print("\nConfiguración actual de sueldos:")
                for cat, sueldo in config.items():
                    print(f"{cat}: {sueldo}")
                input("\nPresione Enter para continuar...")

            elif opcion == "2":
                print("\nSeleccione la categoría a actualizar:")
                categorias = list(CategoriaLaboral)
                for index, categoria in enumerate(categorias, start=1):
                    print(f"{index}. {categoria.name}")
                try:
                    eleccion = int(input("Ingrese opción: "))
                    if 1 <= eleccion <= len(categorias):
                        categoria_seleccionada = categorias[eleccion - 1]
                        nuevo_sueldo = float(input(f"Ingrese el nuevo sueldo base para {categoria_seleccionada.name}: "))
                        if self.controller.actualizar_categoria(categoria_seleccionada, nuevo_sueldo):
                            print("\nSueldo actualizado exitosamente.")
                        else:
                            print("\nError al actualizar el sueldo.")
                    else:
                        print("\nOpción inválida.")
                except ValueError:
                    print("\nEntrada inválida. Por favor ingrese números válidos.")
                input("\nPresione Enter para continuar...")

            elif opcion == "3":
                print("\nSaliendo del panel...")
                break

            else:
                print("\nOpción no válida.")
                input("\nPresione Enter para continuar...")