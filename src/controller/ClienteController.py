from __future__ import annotations
# Se importan las clases Cliente y Campana desde el modelo correspondiente.
from src.model.Cliente import Cliente
from src.model.Campana import Campana
from typing import List
import json, os, logging

# Configuración de logging para auditoría de clientes.
logging.basicConfig(
    filename = './logging/auditoria_clientes.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class ClienteController:
    def __init__(self, file_path: str = './data/clientes.json') -> None:
        """
        Inicializa el controlador de clientes, estableciendo la ruta del archivo JSON
        y cargando la lista de clientes registrados.
        
        Args:
            file_path (str): Ruta del archivo JSON que contiene los clientes.
        """
        self.file_path = file_path
        # Carga la lista de clientes desde el archivo JSON.
        self.clientes: List[Cliente] = self.cargar_clientes()
        
    def cargar_clientes(self) -> List[Cliente]:
        """
        Carga los clientes del archivo JSON y los convierte en una lista de objetos Cliente.
        
        Returns:
            List[Cliente]: Lista de clientes cargados; en caso de error o si el archivo
                           no existe, retorna una lista vacía.
        """
        # Verifica si el archivo existe en la ruta especificada.
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try:
                    # Carga los datos JSON del archivo.
                    data: dict = json.load(file)
                    clientes = []
                    # Itera sobre cada registro para construir los objetos Cliente.
                    for c in data:
                        # Verifica si el cliente tiene campañas asociadas, de lo contrario asigna una lista vacía.
                        campañas_data = c['campañas'] if 'campañas' in c else []
                        # Crea objetos Campana a partir de los datos JSON.
                        campañas_obj = [Campana.from_json(campana_data) for campana_data in campañas_data]
                        
                        # Crea una instancia de Cliente con los datos cargados.
                        cliente = Cliente(
                            id = c['id'],
                            nombre = c['nombre'],
                            direccion = c['direccion'],
                            detalle_contacto = c['detalle_contacto'],
                            campañas = campañas_obj
                        )
                        clientes.append(cliente)
                    return clientes
                except json.JSONDecodeError as e:
                    # Registra error si ocurre un problema al decodificar el JSON.
                    logging.error("Error al decodificar JSON: %s", e)
                    return []
        # Retorna una lista vacía si el archivo no existe.
        return []
    
    def guardar_clientes(self) -> None:
        """
        Guarda la lista actual de clientes en el archivo JSON.
        Se sobreescribe el archivo con la lista actualizada.
        """
        # Prepara la información de cada cliente en formato diccionario para ser serializada.
        data = [{
            'id': cliente.id,
            'nombre': cliente.nombre,
            'direccion': cliente.direccion,
            'detalle_contacto': cliente.detalle_contacto,
            'campañas': [campana.to_json() for campana in cliente.campañas]
        } for cliente in self.clientes]
        
        try:
            # Abre el archivo en modo escritura y guarda los datos en formato JSON.
            with open(self.file_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            # Registra error en caso de fallo al guardar el archivo.
            logging.error("Error al guardar clientes en JSON: %s", e)
            
    def listar_clientes(self) -> List[Cliente]:
        """
        UC1: Retorna la lista de clientes registrados.
        
        Returns:
            List[Cliente]: Lista de clientes.
        """
        return self.clientes
    
    def registrar_cliente(self, nombre: str, direccion: str, detalle_contacto: str) -> bool:
        """
        UC1: Registra un nuevo cliente.
        
        Antes de registrar, se verifica que no exista ya un cliente con la misma combinación de nombre y dirección.
        Si la operación es exitosa, se guarda el archivo JSON y se registra la acción para auditoría.
        
        Args:
            nombre (str): Nombre del cliente.
            direccion (str): Dirección del cliente.
            detalle_contacto (str): Detalle de contacto.
        
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado.
        """
        # Recorre la lista de clientes para detectar duplicados.
        for cliente in self.clientes:
            if cliente.nombre == nombre and cliente.direccion == direccion:
                logging.error("Error: Ya existe un cliente con el mismo nombre y direccion.")
                return False
        
        # Crea un nuevo objeto Cliente y registra los datos.
        nuevo_cliente = Cliente()
        nuevo_cliente.registrar_cliente(nombre, direccion, detalle_contacto)
        # Agrega el nuevo cliente a la lista.
        self.clientes.append(nuevo_cliente)
        # Persiste la lista actualizada en el archivo JSON.
        self.guardar_clientes()
        logging.info("Registro de auditoria: Se agrego un nuevo cliente con id %s.", nuevo_cliente.id)
        return True
    
    def actualizar_cliente(self, id: int, nombre: str = None, direccion: str = None, detalle_contacto: str = None) -> bool:
        """
        UC1: Actualiza los datos de un cliente existente.
        
        Se busca el cliente por su id y se actualizan los campos indicados. Antes de actualizar, se verifica que la nueva 
        combinación de nombre y dirección no coincida con la de otro cliente.
        
        Args:
            id (int): Identificador del cliente a actualizar.
            nombre (str, optional): Nuevo nombre.
            direccion (str, optional): Nueva dirección.
            detalle_contacto (str, optional): Nuevo detalle de contacto.
        
        Returns:
            bool: True si la actualización fue exitosa, False si no se encontró al cliente o existe duplicidad.
        """
        # Busca el cliente por su identificador.
        for cliente in self.clientes:
            if cliente.id == id:
                # Define los valores nuevos, conservando los existentes si no se especifica uno nuevo.
                nuevo_nombre = nombre if nombre is not None else cliente.nombre
                nueva_direccion = direccion if direccion is not None else cliente.direccion
                
                # Verifica que ningún otro cliente tenga la misma combinación de nombre y dirección.                                
                if any(otro.id != id and otro.nombre == nuevo_nombre and otro.direccion == nueva_direccion for otro in self.clientes):
                    logging.error("Error: Existe otro cliente con el mismo nombre y direccion")
                    return False
                
                # Actualiza los datos del cliente.
                cliente.actualizar_datos(nombre, direccion, detalle_contacto)
                # Guarda los cambios en el archivo JSON.
                self.guardar_clientes()
                logging.info("Registro de auditoria: Se actualizó la información del cliente con id %s.", id)
                return True
        
        logging.error("Error: Cliente con id %s no encontrado.", id)
        return False
    
    def eliminar_cliente(self, id: int) -> bool:
        """
        UC1: Elimina un cliente dado su id.
        
        Se busca el cliente y, si existe, se elimina de la lista y se actualiza el archivo JSON.
        
        Args:
            id (int): Identificador del cliente a eliminar.
        
        Returns:
            bool: True si se eliminó el cliente, False si no se encontró.
        """
        # Recorre la lista de clientes con su índice para facilitar la eliminación.
        for index, cliente in enumerate(self.clientes):
            if cliente.id == id:
                # Elimina el cliente de la lista.
                del self.clientes[index]
                # Persiste la lista actualizada en el archivo JSON.
                self.guardar_clientes()
                logging.info("Registro de auditoría: Se eliminó el cliente con id %s.", id)
                return True
        
        logging.error("Error: Cliente con id %s no encontrado para eliminar.", id)
        return False