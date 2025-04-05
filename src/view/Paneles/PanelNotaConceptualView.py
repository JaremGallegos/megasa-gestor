from src.controller.NotaConceptualController import NotaConceptualController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelNotaConceptualView:
    def __init__(self) -> None:
        self.controller = NotaConceptualController()
        
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_nota_conceptual(self, username: str, rol: CategoriaLaboral) -> None:
        while True:
            self.limpiar_ventana()
            print(f"=== Panel de Notas Conceptuales - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Registrar idea de anuncio")
            print("2. Consultar ideas de anuncios")
            print("3. Salir")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                descripcion = input("Ingrese la descripción de la idea: ")
                fecha = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
                if self.controller.registrar_ideas(descripcion, fecha):
                    print("Idea registrada exitosamente.")
                else:
                    print("Error: Ya existe una idea con la misma descripción o se presentó un problema al registrar.")
                input("Presione Enter para continuar...")

            elif opcion == "2":
                ideas = self.controller.consultar_ideas()
                if ideas:
                    print("\nListado de ideas registradas:")
                    for idea in ideas:
                        print(f"ID: {idea['id']} | Descripción: {idea['descripcion']} | Fecha: {idea['fecha']}")
                else:
                    print("No hay ideas registradas.")
                input("\nPresione Enter para continuar...")

            elif opcion == "3":
                print("Saliendo del panel...")
                break

            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")