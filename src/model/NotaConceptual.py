from __future__ import annotations
import json

class NotaConceptual:
    def __init__(self, id: int, descripcion: str, fecha: str):
        self._id = id
        self._descripcion = descripcion
        self._fecha = fecha
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion: str):
        self._descripcion = descripcion

    @property
    def fecha(self) -> str:
        return self._fecha
    
    @fecha.setter
    def fecha(self, value: str):
        self._fecha = value
        
    def registrar_nota(self) -> None:
        # Lógica para registrar nota
        pass

    def to_json(self) -> str:
        return json.dumps({
            'id': self._id,
            'descripcion': self._descripcion,
            'fecha': self._fecha
        })

    @classmethod
    def from_json(cls, data: str) -> 'NotaConceptual':
        data_dict = json.loads(data)
        return cls(
            id=data_dict['id'],
            descripcion=data_dict['descripcion'],
            fecha=data_dict['fecha']
        )