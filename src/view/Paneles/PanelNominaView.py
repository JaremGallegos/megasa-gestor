from src.controller.NominaController import NominaController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelNominaView:
    def __init__(self, empleados: list) -> None:
        self.controller = NominaController(empleados)
        
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_nomina(self, username: str, rol: CategoriaLaboral) -> None:
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Nómina - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Calcular nómina")
            print("2. Salir")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                nominas = self.controller.calcular_nomina()
                if nominas:
                    print("\nNómina de empleados:")
                    for nomina in nominas:
                        print(f"ID: {nomina['id']}, Nombre: {nomina['nombre']}, "
                              f"Categoría: {nomina['categoria']}, Sueldo Base: {nomina['sueldo_base']}, "
                              f"Nómina Final: {nomina['nomina_final']}")
                else:
                    print("\nNo se pudo calcular la nómina o la lista está vacía.")
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                print("\nSaliendo del panel...")
                break
            else:
                print("\nOpción no válida.")
                input("\nPresione Enter para continuar...")
