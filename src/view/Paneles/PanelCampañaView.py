from src.controller.CampanaController import CampañaController
from src.model.CategoriaLaboral import CategoriaLaboral
import os

class PanelCampañaView:
    def __init__(self):
        self.controller = CampañaController()
        
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def view_panel_campaña(self, username: str, rol: CategoriaLaboral) -> tuple[str, CategoriaLaboral] | None:
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Campaña - Usuario: {username} | Rol: {rol.name} ===")
            print("1. Registrar Campaña Publicitaria")
            print("2. Registrar Finalización de Campaña")
            print("3. Registrar Pago de Campaña")
            print("4. Consultar Pagos de Campaña")
            print("5. Asignar Empleados a Campaña")
            print("6. Registrar Anuncio de Campaña")
            print("7. Registrar Finalización de Anuncio")
            print("8. Registrar Gastos de Campaña")
            print("9. Consultar Gastos de Campaña")