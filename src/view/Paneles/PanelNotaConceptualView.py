from src.controller.NotaConceptualController import NotaConceptualController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelNotaConceptualView:
    def __init__(self) -> None:
        """
        Constructor de la clase PanelNotaConceptualView.
        Inicializa el controlador de nota conceptual para gestionar las ideas de anuncios.
        """
        self.controller = NotaConceptualController()
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal para mantener la interfaz organizada.
        Utiliza 'cls' en Windows y 'clear' en sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_nota_conceptual(self, username: str, rol: CategoriaLaboral) -> None:
        """
        Muestra el panel de notas conceptuales para el usuario autenticado, 
        permitiendo registrar nuevas ideas de anuncios o consultar las ideas existentes.
        
        Args:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Rol asignado al usuario.
        """
        while True:
            # Limpia la pantalla en cada iteración para una vista limpia.
            self.limpiar_ventana()
            # Muestra el encabezado del panel con la información del usuario y su rol.
            print(f"=== Panel de Notas Conceptuales - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Registrar idea de anuncio")
            print("2. Consultar ideas de anuncios")
            print("3. Salir")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                # Solicita la descripción y fecha de la nueva idea de anuncio.
                descripcion = input("Ingrese la descripción de la idea: ")
                fecha = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
                # Intenta registrar la idea a través del controlador.
                if self.controller.registrar_ideas(descripcion, fecha):
                    print("Idea registrada exitosamente.")
                else:
                    print("Error: Ya existe una idea con la misma descripción o se presentó un problema al registrar.")
                input("Presione Enter para continuar...")

            elif opcion == "2":
                # Consulta las ideas registradas a través del controlador.
                ideas = self.controller.consultar_ideas()
                if ideas:
                    print("\nListado de ideas registradas:")
                    # Itera sobre la lista de ideas y muestra sus detalles.
                    for idea in ideas:
                        print(f"ID: {idea['id']} | Descripción: {idea['descripcion']} | Fecha: {idea['fecha']}")
                else:
                    print("No hay ideas registradas.")
                input("\nPresione Enter para continuar...")

            elif opcion == "3":
                # Opción para salir del panel de notas conceptuales.
                print("Saliendo del panel...")
                break

            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")