from __future__ import annotations
from typing import List
from src.model.Campana import Campana
import json

class Cliente:
    def __init__(self, 
                 id: int, 
                 nombre: str, 
                 direccion: str, 
                 detalle_contacto: str, 
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
        
    def registrar_cliente(self) -> None:
        pass
    
    def actualizar_datos(self) -> None:
        pass
    
    def eliminar_cliente(self) -> None:
        pass
    
    def consultar_campañas(self) -> List[Campana]:
        return self._campañas
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self._id,
            'nombre': self._nombre,
            'direccion': self._direccion,
            'detalle_contacto': self._detalle_contacto,
            'campañas': [campana.to_json() for campana in self._campañas]
        })
        
    @classmethod
    def from_json(cls, data: str) -> 'Cliente':
        data_dict = json.loads(data)
        campañas = [Campana.from_json(json.dumps(c)) for c in data_dict.get('campañas', [])] # Existe un error en .get, no se reconoce el metodo
        return cls(
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            direccion = data_dict['direccion'],
            detalle_contacto = data_dict['detalle_contacto'],
            campañas = campañas
        )