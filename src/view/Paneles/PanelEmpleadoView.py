from src.controller.EmpleadoController import EmpleadoController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelEmpleadoView:
    def __init__(self) -> None:
        self.controller = EmpleadoController()
        
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_empleado(self, username: str, rol: CategoriaLaboral) -> tuple[str, CategoriaLaboral] | None:
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Empleado - Usuario: {username} | Rol: {rol.name} ===")
            