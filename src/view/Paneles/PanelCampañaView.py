from src.controller.CampanaController import CampañaController
from src.model.PersonalContacto import PersonalContacto
from src.model.CategoriaLaboral import CategoriaLaboral
from src.model.Pago import Pago
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
            print("6. Registrar Empleado de Contacto para Campaña")
            print("0. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.registrar_campaña()
            elif opcion == "2":
                self.registrar_finalizacion_campaña()
            elif opcion == "3":
                self.registrar_pago_campaña()
            elif opcion == "4":
                self.consultar_pagos_campaña()
            elif opcion == "5":
                self.asignar_empleados_campaña()
            elif opcion == "6":
                self.registrar_contacto_campaña()
            elif opcion == "0":
                print("Saliendo del panel de campaña...")
                input("Presione Enter para continuar...")
                break
            else:
                print("Opción no válida.")
                input("Presione Enter para continuar...")
        
    def registrar_campaña(self) -> None:
        self.limpiar_ventana()
        print("=== Registrar Campaña Publicitaria ===")
        titulo = input("Ingrese título: ")
        fecha_inicio = input("Ingrese fecha de inicio (YYYY-MM-DD): ")
        fecha_fin_prevista = input("Ingrese fecha fin prevista (YYYY-MM-DD): ")
        try:
            costes_estimados = float(input("Ingrese costes estimados: "))
            presupuesto = float(input("Ingrese presupuesto: "))
        except ValueError:
            print("Error: Los costes y el presupuesto deben ser números.")
            input("Presione Enter para continuar...")
            return
        
        exito = self.controller.registrar_campaña(titulo, fecha_inicio, fecha_fin_prevista, costes_estimados, presupuesto)
        if exito:
            print("Campaña registrada exitosamente.")
        else:
            print("Error al registrar campaña. Verifique que el título no esté duplicado.")
        
        input("Presione Enter para continuar...")
    
    def registrar_finalizacion_campaña(self) -> None:
        self.limpiar_ventana()
        print("=== Registrar Finalización de Campaña ===")
        try:
            id_campana = int(input("Ingrese el ID de la campaña a finalizar: "))
        except ValueError:
            print("ID inválido.")
            input("Presione Enter para continuar...")
            return
        
        confirmacion = input("¿Confirma la finalización de la campaña? (s/n): ")
        if confirmacion.lower() != 's':
            print("Operación cancelada.")
            input("Presione Enter para continuar...")
            return
        
        exito = self.controller.registrar_finalizacion_campaña(id_campana)
        if exito:
            print("Campaña finalizada exitosamente.")
        else:
            print("Error al finalizar la campaña. Verifique que la campaña esté en ejecución y la información sea correcta.")
        
        input("Presione Enter para continuar...")
    
    def registrar_pago_campaña(self) -> None:
        self.limpiar_ventana()
        print("=== Registrar Pago de Campaña ===")
        try:
            id_campana = int(input("Ingrese el ID de la campaña: "))
            monto = float(input("Ingrese el monto del pago: "))
        except ValueError:
            print("Error: ID o monto inválido.")
            input("Presione Enter para continuar...")
            return
        fecha_pago = input("Ingrese la fecha del pago (YYYY-MM-DD): ")
        
        pago = Pago(id = 0, monto = monto, fecha_pago = fecha_pago)
        
        exito = self.controller.registrar_pago_campaña(id_campana, pago)
        if exito:
            print("Pago registrado exitosamente.")
        else:
            print("Error al registrar el pago. Verifique la información.")
        
        input("Presione Enter para continuar...")
        
    def consultar_pagos_campaña(self) -> None:
        self.limpiar_ventana()
        print("=== Consultar Pagos de Campaña ===")
        try:
            id_campana = int(input("Ingrese el ID de la campaña a consultar: "))
        except ValueError:
            print("ID inválido.")
            input("Presione Enter para continuar...")
            return
        
        pagos = self.controller.consultar_pagos_campaña(id_campana)
        if pagos:
            print(f"Pagos registrados para la campaña {id_campana}:")
            for pago in pagos:
                print(pago.to_json())
        else:
            print("No hay pagos registrados para esta campaña.")
        
        input("Presione Enter para continuar...")
    
    def asignar_empleados_campaña(self) -> None:
        self.limpiar_ventana()
        print("=== Asignar Empleados a Campaña ===")
        try:
            id_campana = int(input("Ingrese el ID de la campaña a asignar: "))
        except ValueError:
            print("ID de campaña inválido.")
            input("Presione Enter para continuar...")
            return
        
        try:
            id_empleado = int(input("Ingrese el ID del empleado: "))
        except ValueError:
            print("ID de empleado inválido.")
            input("Presione Enter para continuar...")
            return
        nombre_empleado = input("Ingrese el nombre del empleado: ")
        email_empleado = input("Ingrese el email del empleado: ")
        
        empleado = PersonalContacto(id_empleado, nombre_empleado, email_empleado)
        exito = self.controller.asignar_empleados_campaña(id_campana, empleado)
        
        if exito:
            print("Empleado asignado a la campaña exitosamente.")
        else:
            print("Error al asignar el empleado. Verifique la información o si ya está asignado.")
        
        input("Presione Enter para continuar...")
        
    def registrar_contacto_campaña(self) -> None:
        self.limpiar_ventana()
        print("=== Registrar Empleado de Contacto para Campaña ===")
        try:
            id_campana = int(input("Ingrese el ID de la campaña: "))
        except ValueError:
            print("ID de campaña inválido.")
            input("Presione Enter para continuar...")
            return
        
        campana = None
        for c in self.controller.campañas:
            if c.id == id_campana:
                campana = c
                break
        if campana is None:
            print("Campaña no encontrada.")
            input("Presione Enter para continuar...")
            return

        if not campana.empleados:
            print("No hay empleados asignados a la campaña. Asigne empleados antes de designar un contacto.")
            input("Presione Enter para continuar...")
            return
        print("Empleados asignados a la campaña:")
        
        for e in campana.empleados:
            print(f"ID: {e.id} | Nombre: {e.nombre} | Email: {e.email}")
        
        try:
            id_empleado = int(input("Ingrese el ID del empleado a designar como contacto: "))
        except ValueError:
            print("ID de empleado inválido.")
            input("Presione Enter para continuar...")
            return
        
        empleado = None
        for e in campana.empleados:
            if e.id == id_empleado:
                empleado = e
                break
        if empleado is None:
            print("El empleado no está asignado a la campaña. Primero asigne el empleado.")
            input("Presione Enter para continuar...")
            return
        
        exito = self.controller.registrar_contacto_campaña(id_campana, empleado)
        if exito:
            print("Empleado designado como contacto exitosamente.")
        else:
            print("Error al designar el contacto.")
        
        input("Presione Enter para continuar...")