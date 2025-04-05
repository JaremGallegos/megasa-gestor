from src.controller.EmpleadoController import EmpleadoController
from src.view.LoginView import UsuarioView
from src.view.MainView import MainView
from src.view.Paneles.PanelClienteView import PanelClienteView
from src.view.Paneles.PanelCampañaView import PanelCampañaView
from src.view.Paneles.PanelEmpleadoView import PanelEmpleadoView
from src.view.Paneles.PanelAnuncioView import PanelAnuncioView
from src.view.Paneles.PanelCategoriaView import PanelCategoriaView
from src.view.Paneles.PanelNominaView import PanelNominaView

def main():
    login_view = UsuarioView()
    login_data = login_view.view_menu_login()
    
    if login_data:
        username, rol = login_data
        main_view = MainView()
        opcion = main_view.view_menu_principal(username, rol)
        if opcion == "cliente":
            panel_cliente_view = PanelClienteView()
            panel_cliente_view.view_panel_cliente(username, rol)
        elif opcion == "campana":
            panel_campaña_view = PanelCampañaView()
            panel_campaña_view.view_panel_campaña(username, rol)
        elif opcion == "anuncio":
            panel_anuncio_view = PanelAnuncioView()
            panel_anuncio_view.view_panel_anuncio(username, rol)
        elif opcion == "empleados":
            panel_empleado_view = PanelEmpleadoView()
            panel_empleado_view.view_panel_empleado(username, rol)
        elif opcion == "categoria":
            panel_categoria_laboral_view = PanelCategoriaView()
            panel_categoria_laboral_view.view_panel_categoria_laboral(username, rol)
        elif opcion == "nomina":
            empleado_controller = EmpleadoController()
            panel_nomina_view = PanelNominaView(empleado_controller.empleados)
            panel_nomina_view.view_panel_nomina(username, rol)
        
    print("Saliendo de la aplicacion.")
    
if __name__ == '__main__':
    main()