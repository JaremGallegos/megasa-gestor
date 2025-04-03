from __future__ import annotations
import json

class Pago:
    def __init__(self, id: int, monto: float, fecha_pago: str):
        self._id = id
        self._monto = monto
        self._fecha_pago = fecha_pago
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def monto(self) -> float:
        return self._monto
    
    @monto.setter
    def monto(self, value: float):
        self._monto = value

    @property
    def fecha_pago(self) -> str:
        return self._fecha_pago
    
    @fecha_pago.setter
    def fecha_pago(self, value: str):
        self._fecha_pago = value
        
    def registrar_pago(self) -> None:
        # Lógica para registrar el pago
        pass

    def get_monto(self) -> float:
        return self._monto

    def get_fecha_pago(self) -> str:
        return self._fecha_pago
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self._id,
            'monto': self._monto,
            'fecha_pago': self._fecha_pago
        })

    @classmethod
    def from_json(cls, data: str) -> 'Pago':
        data_dict = json.loads(data)
        return cls(
            id=data_dict['id'],
            monto=data_dict['monto'],
            fecha_pago=data_dict['fecha_pago']
        )