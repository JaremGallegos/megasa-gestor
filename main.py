from src.view.LoginView import UsuarioView
from src.view.MainView import MainView

def main():
    login_view = UsuarioView()
    username = login_view.view_menu_login()
    
    if username:
        main_view = MainView()
        main_view.view_menu_principal(username)
    
    print("Saliendo de la aplicacion.")
    
if __name__ == '__main__':
    main()