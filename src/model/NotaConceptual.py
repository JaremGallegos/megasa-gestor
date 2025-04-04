from __future__ import annotations
from datetime import datetime, date
import json

def str_to_date(fecha_str: str) -> date:
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()

def date_to_str(fecha_date: date) -> str:
    return fecha_date.strftime("%Y-%m-%d")

class NotaConceptual:
    ultimo_id = 0
    def __init__(self, 
                 id: int = 0, 
                 descripcion: str = "", 
                 fecha: str = "") -> None:
        self._id = id
        self._descripcion = descripcion
        self._fecha = str_to_date(fecha) if isinstance(fecha, str) and fecha.strip() != "" else None
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def descripcion(self) -> str:
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion: str):
        self._descripcion = descripcion

    @property
    def fecha(self) -> str:
        return self._fecha if self._fecha else None
    
    @fecha.setter
    def fecha(self, fecha: str) -> None:
        self._fecha = str_to_date(fecha) if fecha and fecha.strip() else None
        
    def registrar_nota(self, descripcion: str, fecha: str) -> None:
        """
        Registra la idea de anuncio validando que la descripción no esté vacía
        y asigna un ID autogenerado y la fecha proporcionada.
        
        Args:
            descripcion (str): Texto de la idea o nota conceptual.
            fecha (str): Fecha de registro en formato"YYYY-MM-DD".
            
        Raises:
            ValueError: Si la descripción está vacía.
        """
        if not descripcion.strip():
            raise ValueError("La descripción del anuncio no puede estar vacía.")
        
        NotaConceptual.ultimo_id += 1
        self.id = NotaConceptual.ultimo_id
        self.descripcion = descripcion
        self.fecha = fecha
        
        print(f"Nota conceptual registrada correctamente con id {self.id}.")

    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'descripcion': self.descripcion,
            'fecha': self.fecha
        })

    @classmethod
    def from_json(cls, data: str) -> 'NotaConceptual':
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            descripcion = data_dict['descripcion'],
            fecha = data_dict['fecha']
        )