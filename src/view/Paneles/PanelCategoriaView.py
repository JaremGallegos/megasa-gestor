from src.controller.CategoriaLaboralController import CategoriaLaboralController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelCategoriaView:
    def __init__(self) -> None:
        """
        Constructor de la clase PanelCategoriaView.
        Inicializa el controlador de categoría laboral para gestionar la configuración
        de los sueldos base de las distintas categorías laborales.
        """
        self.controller = CategoriaLaboralController()
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal para ofrecer una interfaz limpia.
        Utiliza 'cls' en Windows y 'clear' en sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_categoria_laboral(self, username: str, rol: CategoriaLaboral) -> None:
        """
        Muestra el panel de configuración de categorías laborales para el usuario autenticado.
        
        Args:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Categoría laboral del usuario, mostrada en el encabezado.
        """
        while True:
            # Limpia la pantalla al inicio de cada iteración
            self.limpiar_ventana()
            # Muestra el encabezado del panel con la información del usuario y su rol
            print(f"=== Panel Configuración de Categorías - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Listar categorías laborales")
            print("2. Actualizar sueldo base de una categoría")
            print("3. Salir")
            opcion = input("Ingrese opción: ")

            # Opción 1: Listar las categorías laborales y sus sueldos base actuales
            if opcion == "1":
                config = self.controller.listar_categorias()
                print("\nConfiguración actual de sueldos:")
                for cat, sueldo in config.items():
                    print(f"{cat}: {sueldo}")
                input("\nPresione Enter para continuar...")
                
            # Opción 2: Actualizar el sueldo base de una categoría laboral
            elif opcion == "2":
                print("\nSeleccione la categoría a actualizar:")
                # Se convierte el Enum a una lista para iterar con índices
                categorias = list(CategoriaLaboral)
                for index, categoria in enumerate(categorias, start=1):
                    print(f"{index}. {categoria.name}")
                try:
                    eleccion = int(input("Ingrese opción: "))
                    # Obtiene la categoría seleccionada usando el índice ingresado
                    if 1 <= eleccion <= len(categorias):
                        categoria_seleccionada = categorias[eleccion - 1]
                        nuevo_sueldo = float(input(f"Ingrese el nuevo sueldo base para {categoria_seleccionada.name}: "))
                        # Llama al controlador para actualizar el sueldo de la categoría seleccionada
                        if self.controller.actualizar_categoria(categoria_seleccionada, nuevo_sueldo):
                            print("\nSueldo actualizado exitosamente.")
                        else:
                            print("\nError al actualizar el sueldo.")
                    else:
                        print("\nOpción inválida.")
                except ValueError:
                    # Maneja el error si la entrada no es un número válido
                    print("\nEntrada inválida. Por favor ingrese números válidos.")
                input("\nPresione Enter para continuar...")

            # Opción 3: Salir del panel de configuración
            elif opcion == "3":
                print("\nSaliendo del panel...")
                break
            
            # Manejo de opciones no válidas
            else:
                print("\nOpción no válida.")
                input("\nPresione Enter para continuar...")