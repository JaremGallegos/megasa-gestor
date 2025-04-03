from src.view.LoginView import UsuarioView
from src.view.MainView import MainView

def main():
    login_view = UsuarioView()
    login_data = login_view.view_menu_login()
    
    if login_data:
        username, rol = login_data
        main_view = MainView()
        main_view.view_menu_principal(username, rol)
    
    print("Saliendo de la aplicacion.")
    
if __name__ == '__main__':
    main()