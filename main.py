from src.view.LoginView import UsuarioView
from src.view.MainView import MainView
from src.view.Paneles.PanelClienteView import PanelClienteView
from src.view.Paneles.PanelCampañaView import PanelCampañaView

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
    
    print("Saliendo de la aplicacion.")
    
if __name__ == '__main__':
    main()