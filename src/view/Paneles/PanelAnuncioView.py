from src.model.CategoriaLaboral import CategoriaLaboral
from src.controller.AnuncioController import AnuncioController
import os

class PanelAnuncioView():
    def __init__(self) -> None:
        """
        Constructor de la clase PanelAnuncioView.
        Inicializa el controlador de anuncios que se utilizará para gestionar las operaciones
        relacionadas con los anuncios (registro, finalización y listado).
        """
        self.controller = AnuncioController()
    
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal para ofrecer una interfaz limpia.
        Usa el comando 'cls' en Windows y 'clear' en sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def view_panel_anuncio(self, username: str, rol: CategoriaLaboral) -> None:
        """
        Muestra el panel de anuncios para el usuario autenticado, permitiendo registrar,
        finalizar y listar anuncios, según las opciones seleccionadas.

        Args:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Categoría laboral del usuario (se muestra para referencia).
        """
        while True:
            # Limpia la pantalla al inicio de cada iteración
            self.limpiar_ventana()
            
            # Muestra el encabezado del panel con información del usuario y su rol
            print(f"=== Panel Anuncio - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Registrar anuncio")
            print("2. Finalizar anuncio")
            print("3. Listar anuncios")
            print("4. Salir")
            opcion = input("Ingrese opción: ")
            
            # Opción 1: Registrar un nuevo anuncio
            if opcion == "1":
                descripcion = input("Ingrese la descripción del anuncio: ")
                
                # Intenta registrar el anuncio usando el controlador
                if self.controller.registrar_anuncio(descripcion):
                    print("Anuncio registrado exitosamente.")
                else:
                    print("Error: Ya existe un anuncio con esa descripción o hubo un problema al registrar.")
                input("Presione Enter para continuar...")
            
            # Opción 2: Finalizar un anuncio existente
            elif opcion == "2":
                try:
                    # Solicita el ID del anuncio a finalizar y lo convierte a entero
                    id_anuncio = int(input("Ingrese el ID del anuncio a finalizar: "))
                    
                    # Intenta finalizar el anuncio mediante el controlador
                    if self.controller.registrar_finalizacion_anuncio(id_anuncio):
                        print("Anuncio finalizado exitosamente.")
                    else:
                        print("Error: No se pudo finalizar el anuncio. Verifique que el ID sea correcto o que el anuncio esté en 'En preparación'.")
                except ValueError:
                    # Captura el error en caso de que el ID ingresado no sea un número válido
                    print("El ID ingresado no es válido.")
                input("Presione Enter para continuar...")
            
            # Opción 3: Listar todos los anuncios registrados
            elif opcion == "3":
                if self.controller.anuncios:
                    print("Listado de anuncios:")
                    # Itera sobre la lista de anuncios y muestra sus detalles
                    for anuncio in self.controller.anuncios:
                        print(f"ID: {anuncio.id}, Descripción: {anuncio.descripcion}, Estado: {anuncio.estado}")
                else:
                    print("No hay anuncios registrados.")
                input("Presione Enter para continuar...")
            
            # Opción 4: Salir del panel de anuncios
            elif opcion == "4":
                print("Saliendo del panel...")
                break
            
            # Opción no válida
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")
