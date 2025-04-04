from __future__ import annotations
import json

class Pago:
    def __init__(self, 
                 id: int = 0, 
                 monto: float = 0.0, 
                 fecha_pago: str = ""):
        self._id = id
        self._monto = monto
        self._fecha_pago = fecha_pago
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def monto(self) -> float:
        return self._monto
    
    @monto.setter
    def monto(self, monto: float):
        self._monto = monto

    @property
    def fecha_pago(self) -> str:
        return self._fecha_pago
    
    @fecha_pago.setter
    def fecha_pago(self, fecha_pago: str):
        self._fecha_pago = fecha_pago
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'monto': self.monto,
            'fecha_pago': self.fecha_pago
        })

    @classmethod
    def from_json(cls, data: str) -> 'Pago':
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            monto = data_dict['monto'],
            fecha_pago = data_dict['fecha_pago']
        )