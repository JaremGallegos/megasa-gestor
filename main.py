from src.controller.EmpleadoController import EmpleadoController
from src.view.Paneles.PanelAnuncioView import PanelAnuncioView
from src.view.Paneles.PanelCampañaView import PanelCampañaView
from src.view.Paneles.PanelCategoriaView import PanelCategoriaView
from src.view.Paneles.PanelClienteView import PanelClienteView
from src.view.Paneles.PanelEmpleadoView import PanelEmpleadoView
from src.view.Paneles.PanelNominaView import PanelNominaView
from src.view.Paneles.PanelNotaConceptualView import PanelNotaConceptualView
from src.view.LoginView import UsuarioView
from src.view.MainView import MainView


def main():
    """
    Función principal que inicia la aplicación.
    Muestra el menú de inicio de sesión, valida el acceso del usuario y 
    dirige al panel correspondiente según el rol y opción seleccionada.
    """
    # Vista de login
    login_view = UsuarioView()
    login_data = login_view.view_menu_login()
    
    if login_data:
        username, rol = login_data
        
        # Vista del menú principal
        main_view = MainView()
        opcion = main_view.view_menu_principal(username, rol)
        
        # Dirección a la vista/panel correspondiente según opción elegida
        if opcion == "anuncio":
            panel_anuncio_view = PanelAnuncioView()
            panel_anuncio_view.view_panel_anuncio(username, rol)
        elif opcion == "campana":
            panel_campaña_view = PanelCampañaView()
            panel_campaña_view.view_panel_campaña(username, rol)
        elif opcion == "categoria":
            panel_categoria_laboral_view = PanelCategoriaView()
            panel_categoria_laboral_view.view_panel_categoria_laboral(username, rol)
        elif opcion == "cliente":
            panel_cliente_view = PanelClienteView()
            panel_cliente_view.view_panel_cliente(username, rol)
        elif opcion == "empleado":
            panel_empleado_view = PanelEmpleadoView()
            panel_empleado_view.view_panel_empleado(username, rol)
        elif opcion == "nomina":
            empleado_controller = EmpleadoController()
            panel_nomina_view = PanelNominaView(empleado_controller.empleados)
            panel_nomina_view.view_panel_nomina(username, rol)
        elif opcion == "nota_conceptual":
            panel_nota_conceptual_view = PanelNotaConceptualView()
            panel_nota_conceptual_view.view_panel_nota_conceptual(username, rol)
        
    print("Saliendo de la aplicacion.")
    
if __name__ == '__main__':
    main()