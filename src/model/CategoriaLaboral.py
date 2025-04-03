from __future__ import annotations
from enum import Enum
import json

class CategoriaLaboral(Enum):
    DIRECTOR_CAMPAÑA = (1, "Director Campaña", 1000.0)
    PERSONAL_CONTABLE = (2, "Personal Contable", 800.0)
    PERSONAL_CONTACTO = (3, "Personal Contacto", 700.0)
    PERSONAL_CREATIVO = (4, "Personal Creativo", 600.0)
    
    def __init__(self, id: int, nombre: str, sueldo_base: float) -> None:
        self._id = id
        self._nombre = nombre
        self._sueldo_base = sueldo_base
        
    def __str__(self) -> str:
        return self.nombre
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str):
        self._nombre = nombre

    @property
    def sueldo_base(self) -> float:
        return self._sueldo_base
    
    @sueldo_base.setter
    def sueldo_base(self, sueldo_base: float):
        self._sueldo_base = sueldo_base

    def to_json(self) -> str:
        """
        Convierte el objeto CategoriaLaboral en una cadena JSON.
        """
        return json.dumps({
            'id': self.id,
            'nombre': self.nombre,
            'sueldo_base': self.sueldo_base
        })

    @classmethod
    def from_json(cls, data: str) -> 'CategoriaLaboral':
        """
        Crea un objeto CategoriaLaboral a partir de una cadena JSON.
        """
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            sueldo_base = data_dict['sueldo_base']
        )