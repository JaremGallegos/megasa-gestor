from __future__ import annotations
import json

class CategoriaLaboral:
    def __init__(self, id: int, nombre: str, sueldo_base: float):
        self._id = id
        self._nombre = nombre
        self._sueldo_base = sueldo_base
        
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
        
    def modificar_sueldo(self, nuevo_sueldo: float) -> None:
        self._sueldo_base = nuevo_sueldo

    def to_json(self) -> str:
        return json.dumps({
            'id': self._id,
            'nombre': self._nombre,
            'sueldo_base': self._sueldo_base
        })

    @classmethod
    def from_json(cls, data: str) -> 'CategoriaLaboral':
        data_dict = json.loads(data)
        return cls(
            id=data_dict['id'],
            nombre=data_dict['nombre'],
            sueldo_base=data_dict['sueldo_base']
        )