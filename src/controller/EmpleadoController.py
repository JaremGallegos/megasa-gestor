from __future__ import annotations
# Importa la clase Empleado y CategoriaLaboral del modelo.
from src.model.Empleado import Empleado
from src.model.CategoriaLaboral import CategoriaLaboral
from typing import List
import logging, json, os

# Configuración de logging para auditoría de empleados.
logging.basicConfig(
    filename = '/logging/auditoria_empleados.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class EmpleadoController:
    def __init__(self, file_path: str = './data/empleados.json') -> None:
        """
        Inicializa el controlador de empleados, estableciendo la ruta del archivo JSON
        y cargando la lista de empleados registrados.
        
        Args:
            file_path (str): Ruta del archivo JSON que contiene la información de los empleados.
        """
        self.file_path = file_path
        # Carga la lista de empleados desde el archivo JSON.
        self.empleados: List[Empleado] = self.cargar_empleados()
        
    def cargar_empleados(self) -> List[Empleado]:
        """
        Carga los empleados del archivo JSON y los almacena en una lista.
        Se utiliza el campo 'tipo' para instanciar la subclase adecuada de Empleado.
        
        Returns:
            List[Empleado]: Lista de empleados cargados. Retorna una lista vacía en caso de error.
        """
        empleados: List[Empleado] = []
        # Verifica si el archivo JSON existe en la ruta especificada.
        if os.path.exists(self.file_path):
            # Abre el archivo en modo lectura con codificación UTF-8.
            with open(self.file_path, 'r', ecoding = 'utf-8') as file:
                try:
                    # Carga el contenido del archivo como un diccionario.
                    data: dict = json.load(file)
                    # Itera sobre cada registro (empleado) en los datos.
                    for record in data:
                        # Se utiliza el campo 'tipo' para determinar la subclase del empleado.
                        record: dict = {}
                        tipo = record.get("tipo", "")
                        # Se convierte el registro (diccionario) a una cadena JSON para su posterior reconstrucción.
                        registro_json = json.dumps(record)
                        # Según el tipo, se importa la clase correspondiente y se instancia el objeto.
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
                            # Si no se encuentra un tipo definido, se registra una advertencia y se omite el registro.
                            logging.warning("Registro de empleado sin tipo definido: %s", record)
                            continue
                        # Agrega el empleado instanciado a la lista.
                        empleados.append(emp)
                    return empleados
                except json.JSONDecodeError as e:
                    # Registra un error si ocurre un problema al decodificar el JSON.
                    logging.error("Error al decodificar JSON: %s", e)
                    return []
        # Retorna una lista vacía si el archivo no existe.
        return []
    
    def guardar_empleados(self) -> None:
        """
        Guarda la lista de empleados en el archivo JSON.
        Se incluye el campo 'tipo' para poder reconstruir la subclase correspondiente al cargar.
        """
        data = []
        # Recorre cada empleado para preparar su representación JSON.
        for emp in self.empleados:
            # Convierte el objeto empleado a JSON y luego a un diccionario.
            registro = json.loads(emp.to_json())
            # Agrega el campo 'tipo' con el nombre de la clase para identificar la subclase.
            if hasattr(emp, '__class__'):
                registro["tipo"] = emp.__class__.__name__
            data.append(registro)
        
        try:
            # Asegura que el directorio para el archivo exista; si no, lo crea.
            os.makedirs(os.path.dirname(self.file_path), exist_ok = True)
            # Abre el archivo en modo escritura con codificación UTF-8 y guarda los datos.
            with open(self.file_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            # Registra un error en caso de que ocurra algún problema al guardar el archivo.
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
        
        Verifica que no exista ya un empleado con el mismo id o con información clave duplicada.
        Si la operación es exitosa, guarda la persistencia y registra la acción para auditoría.
        
        Args:
            emp (Empleado): Objeto empleado a registrar.
        
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado
        """
        # Verifica si ya existe un empleado con el mismo id.
        if any(e.id == emp.id for e in self.empleados):
            logging.error("Error: Ya existe un empleado con el id %s.", emp.id)
            return False
        
        # Agrega el nuevo empleado a la lista.
        self.empleados.append(emp)
        # Guarda los cambios en el archivo JSON.
        self.guardar_empleados()
        logging.info("Registro de auditoría: Se agregó un nuevo empleado con id %s.", emp.id)
        return True
    
    def actualizar_empleado(self, id: int, nombre: str = None, email: str = None, usuario: str = None) -> bool:
        """
        UC14: Actualiza los datos de un empleado existente.
        
        Busca el empleado por id y actualiza los campos proporcionados.
        Se registra la operación para auditoría.
        
        Args:
            id (int): Identificador del empleado a actualizar.
            nombre (str, optional): Nuevo nombre para el empleado.
            email (str, optional): Nuevo email para el empleado.
            usuario (str, optional): Nueva información de usuario.
        
        Returns:
            bool: True si la actualización fue exitosa, False en caso de no encontrar al empleado.
        """
        # Itera sobre la lista de empleados para encontrar el empleado con el id indicado.
        for emp in self.empleados:
            if emp.id == id:
                # Actualiza los campos solo si se proporcionan nuevos valores.
                if nombre is not None:
                    emp.nombre = nombre
                if email is not None:
                    emp.email = email
                # Se podría incluir la actualización de 'usuario' u otros campos según sea necesario.
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
        # Recorre la lista de empleados junto con sus índices para facilitar la eliminación.
        for index, emp in enumerate(self.empleados):
            if emp.id == id:
                # Elimina el empleado de la lista.
                del self.empleados[index]
                # Guarda la lista actualizada en el archivo JSON.
                self.guardar_empleados()
                logging.info("Registro de auditoría: Se eliminó el empleado con id %s.", id)
                return True
        
        logging.error("Error: Empleado con id %s no encontrado para eliminar.", id)
        return False