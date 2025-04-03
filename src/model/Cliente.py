from __future__ import annotations
from typing import List
from src.model.Campana import Campana

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
    
    def actualizar_datos(self, nombre: str = None, direccion: str = None, detalle_contacto: str = None) -> None:
        if nombre:
            self.nombre = nombre
        if direccion:
            self.detalle_contacto = direccion
        if detalle_contacto:
            self.detalle_contacto = detalle_contacto
        
        print("Datos del cliente actualizados")
    
    def consultar_campañas(self) -> List[Campana]:
        print("Consultando campañas asociadas al cliente...")
        return self.campañas
    
    def to_dict(self) -> str:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'direccion': self.direccion,
            'detalle_contacto': self.detalle_contacto,
            'campañas': [campana.to_dict() for campana in self.campañas]
        }
        
    @classmethod
    def from_dict(cls, data: dict) -> 'Cliente':
        cliente = cls(data['id'], data['nombre'], data['direccion'], data['detalle_contacto'])
        from src.model.Campana import Campana
        cliente.campañas = [Campana.form_dict(campana_data) for campana_data in data.get('campanas', [])]