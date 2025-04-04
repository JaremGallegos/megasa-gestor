from __future__ import annotations
from src.model.Empleado import Empleado
from typing import List
import logging, json, os

logging.basicConfig(
    filename = '/logging/auditoria_empleados.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class EmpleadoController:
    def __init__(self, file_path: str = './data/empleados.json') -> None:
        self.file_path = file_path
        self.empleados: List[Empleado] = self.cargar_empleados()
        
    def cargar_empleados(self) -> List[Empleado]:
        """
        Carga los empleados del archivo JSON y los almacena en una lista.
        Se utiliza el campo 'tipo' para instanciar la subclase adecuada.
        """
        empleados: List[Empleado] = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', ecoding = 'utf-8') as file:
                try:
                    data: dict = json.load(file)
                    for record in data:
                        record: dict = {}
                        tipo = record.get("tipo", "")
                        registro_json = json.dumps(record)
                        if tipo == "DirectorCampaña":
                            from src.model.DirectorCampana import DirectorCampana
                            emp = DirectorCampana.from_json(registro_json)
                        elif tipo == "PersonalContable":
                            from src.model.PersonalContable import PersonalContable
                            emp = PersonalContable.from_json(registro_json)
                        elif tipo == "PersonalContacto":
                            from src.model.PersonalContacto import PersonalContacto
                            emp = PersonalContacto.from_json(registro_json)
                        elif tipo == "PersonalCreativo":
                            from src.model.PersonalCreativo import PersonalCreativo
                            emp = PersonalCreativo.from_json(registro_json)
                        else:
                            logging.warning("Registro de empleado sin tipo definido: %s", record)
                            continue
                        empleados.append(emp)
                    return empleados
                except json.JSONDecodeError as e:
                    logging.error("Error al decodificar JSON: %s", e)
                    return []
        return []
    
    def guardar_empleados(self) -> None:
        """
        Guarda la lista de empleados en el archivo JSON.
        Se incluye el campo 'tipo' para poder reconstruir la subclase al cargar.
        """
        data = []
        for emp in self.empleados:
            registro = json.loads(emp.to_json())
            if hasattr(emp, '__class__'):
                registro["tipo"] = emp.__class__.__name__
            data.append(registro)
        
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok = True)
            with open(self.file_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            logging.error("Error al guardar empleados en JSON: %s", e)
    
    def listar_empleados(self) -> List[Empleado]:
        """
        Retorna la lista de empleados registrados.
        
        Returns:
            List[Empleado]: Lista de empleados.
        """
        return self.empleados
    
    def registrar_empleado(self, emp: Empleado) -> bool:
        """
        UC14: Registra un nuevo empleado.
        Verifica que no exista ya un empleado con el mismo id o, alternativamente, con la misma información clave.
        Si se registra, se guarda la persistencia y se registra la operación para auditoría.
        
        Args:
            emp (Empleado): Objeto empleado a registrar.
        
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado
        """
        if any(e.id == emp.id for e in self.empleados):
            logging.error("Error: Ya existe un empleado con el id %s.", emp.id)
            return False
        
        self.empleados.append(emp)
        self.guardar_empleados()
        logging.info("Registro de auditoría: Se agregó un nuevo empleado con id %s.", emp.id)
        return True
    
    def actualizar_empleado(self, id: int, nombre: str = None, email: str = None, usuario: str = None) -> bool:
        """
        UC14: Actualiza los datos de un empleado existente.
        Se busca el empleado por id y se actualizan los campos proporcionados.
        Se registra la operación para auditoría.
        
        Args:
            id (int): Identificador del empleado a actualizar.
            nombre (str, optional): Nuevo nombre.
            email (str, optional): Nuevo email.
            usuario (str, optional): Nueva información de usuario (puede ser actualizada según tus necesidades).
        
        Returns:
            bool: True si la actualización fue exitosa, False en caso de no encontrar al empleado.
        """
        for emp in self.empleados:
            if emp.id == id:
                if nombre is not None:
                    emp.nombre = nombre
                if email is not None:
                    emp.email = email
                self.guardar_empleados()
                logging.info("Registro de auditoría: Se actualizó el empleado con id %s.", id)
                return True

        logging.error("Error: Empleado con id %s no encontrado para actualización.", id)
        return False
    
    def eliminar_empleado(self, id: int) -> bool:
        """
        UC14: Elimina un empleado dado su id.
        Se actualiza la persistencia y se registra la operación para auditoría.
        
        Args:
            id (int): Identificador del empleado a eliminar.
            
        Returns:
            bool: True si se eliminó el empleado, False si no se encontró.
        """
        for index, emp in enumerate(self.empleados):
            if emp.id == id:
                del self.empleados[index]
                self.guardar_empleados()
                logging.info("Registro de auditoría: Se eliminó el empleado con id %s.", id)
                return True
        
        logging.error("Error: Empleado con id %s no encontrado para eliminar.", id)
        return False