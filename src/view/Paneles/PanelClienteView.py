from src.controller.ClienteController import ClienteController
from src.model.CategoriaLaboral import CategoriaLaboral
from src.model.Cliente import Cliente
import os

class PanelClienteView:
    def __init__(self) -> None:
        """
        Constructor de la clase PanelClienteView.
        Inicializa el controlador de cliente para gestionar las operaciones
        relacionadas con los clientes (listar, agregar, actualizar y eliminar).
        """
        self.controller = ClienteController()
    
    def limpiar_ventana(self) -> None:
        """
        Limpia la terminal para ofrecer una interfaz limpia.
        Utiliza 'cls' en Windows y 'clear' en sistemas Unix/Linux.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def view_panel_cliente(self, username: str, rol: CategoriaLaboral) -> tuple[str, CategoriaLaboral] | None:
        """
        Muestra el panel de clientes para el usuario autenticado.
        
        Args:
            username (str): Nombre del usuario autenticado.
            rol (CategoriaLaboral): Rol o categoría laboral del usuario.
        
        Returns:
            tuple[str, CategoriaLaboral] | None: Puede retornar una tupla o None, según la acción seleccionada.
        """
        while True:
            self.limpiar_ventana()
            # Encabezado del panel que muestra usuario y rol
            print(f"=== Panel Cliente - Usuario: {username} | Rol: {rol.name} ===")
            print("1. Listar clientes")
            print("2. Agregar nuevo cliente")
            print("3. Actualizar cliente")
            print("4. Eliminar cliente")
            print("5. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                # Llama al controlador para obtener la lista de clientes y muestra la tabla
                clientes = self.controller.listar_clientes()
                self.listar_clientes(clientes)
                input("Presione Enter para continuar...")
            elif opcion == "2":
                # Agrega un nuevo cliente
                self.agregar_cliente()
            elif opcion == "3":
                # Actualiza los datos de un cliente existente
                self.actualizar_cliente()
            elif opcion == "4":
                # Elimina un cliente
                self.eliminar_cliente()
            elif opcion == "5":
                print("Saliendo del panel de clientes...")
                break
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")
                
    def listar_clientes(self, clientes: list[Cliente]) -> None:
        """
        Muestra la lista de clientes en formato de tabla.
        
        Args:
            clientes (list[Cliente]): Lista de objetos Cliente a mostrar.
        """
        self.limpiar_ventana()
        print("|  id  |    nombre    |     direccion     | detalle contacto |   campañas (nombre)   |")
        print("-" * 90)
        # Se recorre la lista de clientes y se muestra cada uno formateado
        for cliente in clientes:
            campanas_nombres = ", ".join([campana.nombre for campana in cliente.campañas])
            print(f"| {cliente.id:<4} | {cliente.nombre:<12} | {cliente.direccion:<18} | {cliente.detalle_contacto:<16} | {campanas_nombres:<20} |")
        print("-" * 90)
    
    def agregar_cliente(self) -> None:
        """
        Solicita al usuario los datos para agregar un nuevo cliente y utiliza el 
        controlador para registrar el cliente.
        """
        self.limpiar_ventana()
        print("=== Agregar nuevo cliente ===")
        nombre = input("Ingrese nombre: ")
        direccion = input("Ingrese dirección: ")
        detalle_contacto = input("Ingrese detalle de contacto: ")
        # Se llama al controlador para registrar el nuevo cliente
        exito = self.controller.registrar_cliente(nombre, direccion, detalle_contacto)
        if exito:
            print("Cliente agregado exitosamente")
        else:
            print("Error al agregar cliente (posible duplicado)")
        input("Presione Enter para continuar...")
        
    def actualizar_cliente(self) -> None:
        """
        Solicita al usuario el id del cliente a actualizar y los nuevos datos, 
        y utiliza el controlador para actualizar el cliente.
        """
        self.limpiar_ventana()
        print("=== Actualizar cliente ===")
        id_cliente = input("Ingrese id del cliente a actualizar: ")
        try:
            id_cliente = int(id_cliente)
        except ValueError:
            print("Id Inválido.")
            input("Presione Enter para continuar...")
            return
        
        print("Deje en blanco los campos que no desea actualizar.")
        nombre = input("Ingrese nuevo nombre: ")
        direccion = input("Ingrese nueva dirección: ")
        detalle_contacto = input("Ingrese nuevo detalle de contacto: ")
        
        # Se convierten los campos vacíos a None para indicar que no se actualizarán
        nombre = nombre if nombre.strip() != "" else None
        direccion = direccion if direccion.strip() != "" else None
        detalle_contacto = detalle_contacto if detalle_contacto.strip() != "" else None
        
        # Llama al controlador para actualizar los datos del cliente
        exito = self.controller.actualizar_cliente(id_cliente, nombre, direccion, detalle_contacto)
        if exito:
            print("Cliente actualizado exitosamente.")
        else:
            print("Error al actualizar cliente (duplicidad o cliente no encontrado).")
        input("Presione Enter para continuar...")
        
    def eliminar_cliente(self) -> None:
        """
        Solicita el id del cliente a eliminar y utiliza el controlador para 
        eliminarlo.
        """
        self.limpiar_ventana()
        print("=== Eliminar cliente ===")
        id_cliente = input("Ingrese id del cliente a eliminar: ")
        try:
            id_cliente = int(id_cliente)
        except ValueError:
            print("Id inválido.")
            input("Presione Enter para continuar...")
            return
        
        # Llama al controlador para eliminar el cliente
        exito = self.controller.eliminar_cliente(id_cliente)
        if exito:
            print("Cliente eliminado exitosamente.")
        else:
            print("Error al eliminar cliente (cliente no encontrado).")
        input("Presione Enter para continuar...")
        