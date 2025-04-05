from src.controller.NominaController import NominaController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelNominaView:
    def __init__(self, empleados: list) -> None:
        """
        Constructor de la clase PanelNominaView.
        
        Inicializa el controlador de nómina con la lista de empleados proporcionada.
        
        Args:
            empleados (list): Lista de empleados sobre la que se calculará la nómina.
        """
        self.controller = NominaController(empleados)
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal para mantener la interfaz limpia.
        
        Utiliza 'cls' en Windows y 'clear' en sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_nomina(self, username: str, rol: CategoriaLaboral) -> None:
        """
        Muestra el panel de nómina para el usuario autenticado, permitiendo
        calcular la nómina de empleados o salir del panel.
        
        Args:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Rol o categoría laboral del usuario.
        """
        while True:
            # Limpia la pantalla al inicio de cada iteración del menú
            self.limpiar_ventana()
            # Muestra el encabezado del panel con el usuario y su rol
            print(f"=== Panel Nómina - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Calcular nómina")
            print("2. Salir")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                # Calcula la nómina utilizando el controlador y almacena el resultado en 'nominas'
                nominas = self.controller.calcular_nomina()
                if nominas:
                    print("\nNómina de empleados:")
                    # Itera sobre la lista de nóminas y muestra los detalles de cada empleado
                    for nomina in nominas:
                        print(f"ID: {nomina['id']}, Nombre: {nomina['nombre']}, "
                              f"Categoría: {nomina['categoria']}, Sueldo Base: {nomina['sueldo_base']}, "
                              f"Nómina Final: {nomina['nomina_final']}")
                else:
                    print("\nNo se pudo calcular la nómina o la lista está vacía.")
                input("\nPresione Enter para continuar...")
            elif opcion == "2":
                # Opción para salir del panel de nómina
                print("\nSaliendo del panel...")
                break
            else:
                print("\nOpción no válida.")
                input("\nPresione Enter para continuar...")
