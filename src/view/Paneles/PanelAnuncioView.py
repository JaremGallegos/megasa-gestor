from src.model.CategoriaLaboral import CategoriaLaboral
from src.controller.AnuncioController import AnuncioController
import os

class PanelAnuncioView():
    def __init__(self) -> None:
        self.controller = AnuncioController()
    
    def limpiar_ventana(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def view_panel_anuncio(self, username: str, rol: CategoriaLaboral) -> None:
        while True:
            self.limpiar_ventana()
            print(f"=== Panel Anuncio - Usuario: {username} | Rol: {rol.name} ===")
            print("Seleccione una opción:")
            print("1. Registrar anuncio")
            print("2. Finalizar anuncio")
            print("3. Listar anuncios")
            print("4. Salir")
            opcion = input("Ingrese opción: ")

            if opcion == "1":
                descripcion = input("Ingrese la descripción del anuncio: ")
                if self.controller.registrar_anuncio(descripcion):
                    print("Anuncio registrado exitosamente.")
                else:
                    print("Error: Ya existe un anuncio con esa descripción o hubo un problema al registrar.")
                input("Presione Enter para continuar...")

            elif opcion == "2":
                try:
                    id_anuncio = int(input("Ingrese el ID del anuncio a finalizar: "))
                    if self.controller.registrar_finalizacion_anuncio(id_anuncio):
                        print("Anuncio finalizado exitosamente.")
                    else:
                        print("Error: No se pudo finalizar el anuncio. Verifique que el ID sea correcto o que el anuncio esté en 'En preparación'.")
                except ValueError:
                    print("El ID ingresado no es válido.")
                input("Presione Enter para continuar...")

            elif opcion == "3":
                if self.controller.anuncios:
                    print("Listado de anuncios:")
                    for anuncio in self.controller.anuncios:
                        print(f"ID: {anuncio.id}, Descripción: {anuncio.descripcion}, Estado: {anuncio.estado}")
                else:
                    print("No hay anuncios registrados.")
                input("Presione Enter para continuar...")

            elif opcion == "4":
                print("Saliendo del panel...")
                break

            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")
