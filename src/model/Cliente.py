from __future__ import annotations
from src.model.Campana import Campana
from typing import List
import json

class Cliente:
    ultimo_id: int = 0
    def __init__(self, 
                 id: int = 0, 
                 nombre: str = "", 
                 direccion: str = 2, 
                 detalle_contacto: str = "", 
                 campañas: List[Campana] = None) -> None:
        self._id = id;
        self._nombre = nombre
        self._direccion = direccion
        self._detalle_contacto = detalle_contacto
        self._campañas = campañas if campañas is not None else []
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id
        
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre
        
    @property
    def direccion(self) -> str:
        return self._direccion
    
    @direccion.setter
    def direccion(self, direccion: str) -> None:
        self._direccion = direccion
        
    @property
    def detalle_contacto(self) -> str:
        return self._detalle_contacto
    
    @detalle_contacto.setter
    def detalle_contacto(self, detalle_contacto: str) -> None:
        self._detalle_contacto = detalle_contacto
        
    @property
    def campañas(self) -> List[Campana]:
        return self._campañas
    
    @campañas.setter
    def campañas(self, campañas: List[Campana]) -> None:
        self._campañas = campañas
        
    def registrar_cliente(self, nombre: str, direccion: str, detalle_contacto: str) -> None:
        """
        Registra un cliente asignándole un id atogenerado
        La asignación del id se realiza mediante un autoincremente en la variable de clase.
        """
        Cliente.ultimo_id += 1
        self.id = Cliente.ultimo_id
        self.nombre = nombre 
        self.direccion = direccion
        self.detalle_contacto = detalle_contacto
        
        print(f"Cliente registrado: id = {self.id}, nombre = {self.nombre}")
    
    def actualizar_datos(self, nombre: str = None, direccion: str = None, detalle_contacto: str = None) -> None:
        """
        Actualiza los datos del cliente.
        Si se proporciona un nuevo valor, se actualiza; de lo contrario, mantiene el valor actual.
        """
        if nombre is not None:
            self.nombre = nombre
        if direccion is not None:
            self.direccion = direccion
        if detalle_contacto is not None:
            self.detalle_contacto = detalle_contacto
        
        print("Datos del cliente actualizado")
    
    def to_json(self) -> str:
        """
        Convierte el objeto Cliente en una cadena JSON
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
        """
        data_dict: dict = json.loads(data)
        campañas = [Campana.from_json(c_json) for c_json in data_dict.get('campañas', [])]
        return cls(
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            direccion = data_dict['direccion'],
            detalle_contacto = data_dict['detalle_contacto'],
            campañas = campañas
        )