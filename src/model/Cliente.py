from __future__ import annotations
from src.model.Campana import Campana
from typing import List
import json

class Cliente:
    # Atributo de clase para llevar la cuenta del último ID asignado a un cliente.
    ultimo_id: int = 0
    
    def __init__(self, 
                 id: int = 0, 
                 nombre: str = "", 
                 direccion: str = "", 
                 detalle_contacto: str = "", 
                 campañas: List[Campana] = None) -> None:
        """
        Inicializa una nueva instancia de Cliente con los datos proporcionados.
        
        Args:
            id (int, opcional): Identificador del cliente. Por defecto es 0.
            nombre (str, opcional): Nombre del cliente.
            direccion (str, opcional): Dirección del cliente.
            detalle_contacto (str, opcional): Detalle de contacto del cliente.
            campañas (List[Campana], opcional): Lista de campañas asociadas al cliente.
        """
        self._id = id;
        self._nombre = nombre
        self._direccion = direccion
        self._detalle_contacto = detalle_contacto
        # Inicializa la lista de campañas; si no se proporciona, se usa una lista vacía.
        self._campañas = campañas if campañas is not None else []
        
    @property
    def id(self) -> int:
        """
        Obtiene el ID del cliente.
        
        Returns:
            int: Identificador del cliente.
        """
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Establece el ID del cliente.
        
        Args:
            id (int): Nuevo identificador del cliente.
        """
        self._id = id
        
    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre del cliente.
        
        Returns:
            str: Nombre del cliente.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        """
        Establece el nombre del cliente.
        
        Args:
            nombre (str): Nuevo nombre del cliente.
        """
        self._nombre = nombre
        
    @property
    def direccion(self) -> str:
        """
        Obtiene la dirección del cliente.
        
        Returns:
            str: Dirección del cliente.
        """
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion: str) -> None:
        """
        Establece la dirección del cliente.
        
        Args:
            direccion (str): Nueva dirección del cliente.
        """
        self._direccion = direccion
        
    @property
    def detalle_contacto(self) -> str:
        """
        Obtiene el detalle de contacto del cliente.
        
        Returns:
            str: Detalle de contacto.
        """
        return self._detalle_contacto
    
    @detalle_contacto.setter
    def detalle_contacto(self, detalle_contacto: str) -> None:
        """
        Establece el detalle de contacto del cliente.
        
        Args:
            detalle_contacto (str): Nuevo detalle de contacto.
        """
        self._detalle_contacto = detalle_contacto
        
    @property
    def campañas(self) -> List[Campana]:
        """
        Obtiene la lista de campañas asociadas al cliente.
        
        Returns:
            List[Campana]: Lista de campañas.
        """
        return self._campañas
    
    @campañas.setter
    def campañas(self, campañas: List[Campana]) -> None:
        """
        Establece la lista de campañas asociadas al cliente.
        Verifica que todos los elementos de la lista sean instancias de Campana.
        
        Args:
            campañas (List[Campana]): Nueva lista de campañas.
            
        Raises:
            ValueError: Si algún elemento de la lista no es una instancia de Campana.
        """
        if not all(isinstance(c, Campana) for c in campañas):
            raise ValueError("Todos los elementos deben ser instancias de Campaña")
        self._campañas = campañas
        
    def registrar_cliente(self, nombre: str, direccion: str, detalle_contacto: str) -> None:
        """
        Registra el cliente asignándole un ID autogenerado mediante autoincremento.
        
        Args:
            nombre (str): Nombre del cliente.
            direccion (str): Dirección del cliente.
            detalle_contacto (str): Detalle de contacto del cliente.
        """
        Cliente.ultimo_id += 1
        self.id = Cliente.ultimo_id
        self.nombre = nombre 
        self.direccion = direccion
        self.detalle_contacto = detalle_contacto
        
        print(f"Cliente registrado: id = {self.id}, nombre = {self.nombre}")
    
    def actualizar_datos(self, nombre: str = None, direccion: str = None, detalle_contacto: str = None) -> None:
        """
        Actualiza los datos del cliente. Si se proporciona un nuevo valor, se actualiza;
        de lo contrario, mantiene el valor actual.
        
        Args:
            nombre (str, opcional): Nuevo nombre. Si es None, no se actualiza.
            direccion (str, opcional): Nueva dirección. Si es None, no se actualiza.
            detalle_contacto (str, opcional): Nuevo detalle de contacto. Si es None, no se actualiza.
        """
        if nombre is not None:
            self.nombre = nombre.strip()
        if direccion is not None:
            self.direccion = direccion.strip()
        if detalle_contacto is not None:
            self.detalle_contacto = detalle_contacto.strip()
        
        print("Datos del cliente actualizado")
    
    def to_json(self) -> str:
        """
        Convierte el objeto Cliente en una cadena JSON.
        
        Returns:
            str: Cadena JSON que representa al cliente con sus atributos.
        """
        return json.dumps({
            'id': self.id,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'detalle_contacto': self.detalle_contacto,
            'campañas': [campana.to_json() for campana in self.campañas]
        })
        
    @classmethod
    def from_json(cls, data: str) -> 'Cliente':
        """
        Crea un objeto Cliente a partir de una cadena JSON.
        
        Args:
            data (str): Cadena JSON con los datos del cliente.
        
        Returns:
            Cliente: Instancia de Cliente creada a partir del JSON.
        """
        data_dict: dict = json.loads(data)
        campañas = [Campana.from_json(c_json) for c_json in data_dict.get('campañas', [])]
        cliente = cls(
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            direccion = data_dict['direccion'],
            detalle_contacto = data_dict['detalle_contacto'],
            campañas = campañas
        )
        # Actualiza el último ID si es necesario.
        Cliente.ultimo_id = max(Cliente.ultimo_id, Cliente.id)
        return cliente