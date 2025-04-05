from src.controller.EmpleadoController import EmpleadoController
from src.model.CategoriaLaboral import CategoriaLaboral
from src.model.PersonalContable import PersonalContable
import os

class PanelEmpleadoView:
    def __init__(self) -> None:
        """
        Constructor de la clase PanelEmpleadoView.
        Inicializa la vista del panel de empleados creando una instancia
        del controlador de empleados.
        """
        self.controller = EmpleadoController()
        
    def limpiar_ventana(self) -> None:
        """
        Limpia la consola para mantener la vista organizada.
        Utiliza 'cls' para sistemas Windows y 'clear' para Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_empleado(self, username: str, rol: CategoriaLaboral) -> None:
        """
        Muestra el panel principal para la gestión de empleados, permitiendo
        listar, registrar, actualizar y eliminar empleados. También ofrece la opción
        de salir del panel.
        
        Args:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Rol asignado al usuario.
        """
        while True:
            self.limpiar_ventana()
            # Encabezado del panel que muestra la información del usuario y su rol.
            print(f"=== Panel Empleado - Usuario: {username} | Rol: {rol.name} ===")
            print("1. Listar empleados")
            print("2. Registrar empleado")
            print("3. Actualizar empleado")
            print("4. Eliminar empleado")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == '0':
                print("Saliendo del panel de empleados...")
                input("Presione Enter para continuar...")
                break
            elif opcion == '1':
                self.listar_empleados()
            elif opcion == '2':
                self.registrar_empleado()
            elif opcion == '3':
                self.actualizar_empleado()
            elif opcion == '4':
                self.eliminar_empleado()
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")
    
    def listar_empleados(self) -> None:
        """
        Muestra la lista de empleados registrados. Si no hay empleados,
        informa al usuario.
        """
        # Obtiene la lista de empleados a través del controlador.
        empleados = self.controller.listar_empleados()
        print("\n=== Lista de Empleados ===")
        if not empleados:
            print("No hay empleados registrados.")
        else:
            # Itera sobre la lista de empleados y muestra sus detalles.
            for emp in empleados:
                print(f"ID: {emp.id}, Nombre: {emp.nombre}, Email: {emp.email}")
        input("\nPresione Enter para continuar...")
          
    def registrar_empleado(self) -> None:
        """
        Solicita los datos para registrar un nuevo empleado, crea una instancia
        de PersonalContable y utiliza el controlador para persistirla.
        """
        print("\n=== Registrar Nuevo Empleado ===")
        try:
            id_str = input("Ingrese ID (número): ")
            id_emp = int(id_str)
        except ValueError:
            print("Error: El ID debe ser un número.")
            input("Presione Enter para continuar...")
            return
        
        nombre = input("Ingrese nombre: ")
        email = input("Ingrese email: ")
        
        # Crear la instancia de PersonalContable y asignar sus propiedades.
        nuevo_emp = PersonalContable()
        nuevo_emp.id = id_emp
        nuevo_emp.nombre = nombre
        nuevo_emp.email = email
        
        # Intenta registrar el empleado utilizando el controlador.
        if self.controller.registrar_empleado(nuevo_emp):
            print("Empleado registrado exitosamente.")
        else:
            print("Error: Ya existe un empleado con ese ID.")
        input("Presione Enter para continuar...")
        
    def actualizar_empleado(self) -> None:
        """
        Solicita el ID del empleado a actualizar y los nuevos datos (nombre y email).
        Utiliza el controlador para actualizar la información del empleado.
        """
        print("\n=== Actualizar Empleado ===")
        try:
            id_str = input("Ingrese el ID del empleado a actualizar: ")
            id_emp = int(id_str)
        except ValueError:
            print("Error: El ID debe ser un número.")
            input("Presione Enter para continuar...")
            return
        
        # Se solicita la entrada de nuevos datos; se permite dejar en blanco para no modificar.
        nombre = input("Ingrese nuevo nombre (deje en blanco para no cambiar): ")
        email = input("Ingrese nuevo email (deje en blanco para no cambiar): ")
        
        # Se pasan los nuevos valores si se ingresaron; de lo contrario, se utiliza None.
        if self.controller.actualizar_empleado(
                id_emp, 
                nombre if nombre.strip() != "" else None, 
                email if email.strip() != "" else None
            ):
            print("Empleado actualizado exitosamente.")
        else:
            print("Error: Empleado no encontrado.")
        input("Presione Enter para continuar...")
        
    def eliminar_empleado(self) -> None:
        """
        Solicita el ID del empleado a eliminar y utiliza el controlador para
        borrar el registro.
        """
        print("\n=== Eliminar Empleado ===")
        try:
            id_str = input("Ingrese el ID del empleado a eliminar: ")
            id_emp = int(id_str)
        except ValueError:
            print("Error: El ID debe ser un número.")
            input("Presione Enter para continuar...")
            return
        
        # Llama al controlador para eliminar el empleado.
        if self.controller.eliminar_empleado(id_emp):
            print("Empleado eliminado exitosamente.")
        else:
            print("Error: Empleado no encontrado.")
        input("Presione Enter para continuar...")