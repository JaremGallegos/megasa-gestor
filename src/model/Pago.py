from __future__ import annotations
import json

class Pago:
    def __init__(self, 
                 id: int = 0, 
                 monto: float = 0.0, 
                 fecha_pago: str = "") -> None:
        """
        Inicializa una nueva instancia de Pago.

        Args:
            id (int, opcional): Identificador del pago. Por defecto es 0.
            monto (float, opcional): Monto del pago. Por defecto es 0.0.
            fecha_pago (str, opcional): Fecha en que se realizó el pago en formato "YYYY-MM-DD".
        """
        self._id = id
        self._monto = monto
        self._fecha_pago = fecha_pago
    
    @property
    def id(self) -> int:
        """
        Obtiene el identificador del pago.

        Returns:
            int: El identificador del pago.
        """
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Establece el identificador del pago.

        Args:
            id (int): Nuevo identificador.
        """
        self._id = id

    @property
    def monto(self) -> float:
        """
        Obtiene el monto del pago.

        Returns:
            float: El monto del pago.
        """
        return self._monto
    
    @monto.setter
    def monto(self, monto: float) -> None:
        """
        Establece el monto del pago.

        Args:
            monto (float): Nuevo monto.
        """
        self._monto = monto

    @property
    def fecha_pago(self) -> str:
        """
        Obtiene la fecha de pago.

        Returns:
            str: Fecha de pago en formato "YYYY-MM-DD".
        """
        return self._fecha_pago
    
    @fecha_pago.setter
    def fecha_pago(self, fecha_pago: str) -> None:
        """
        Establece la fecha de pago.

        Args:
            fecha_pago (str): Nueva fecha de pago en formato "YYYY-MM-DD".
        """
        self._fecha_pago = fecha_pago
    
    def to_json(self) -> str:
        """
        Serializa el objeto Pago a una cadena JSON.

        Returns:
            str: Cadena JSON que representa el pago.
        """
        return json.dumps({
            'id': self.id,
            'monto': self.monto,
            'fecha_pago': self.fecha_pago
        })

    @classmethod
    def from_json(cls, data: str) -> 'Pago':
        """
        Crea un objeto Pago a partir de una cadena JSON.

        Args:
            data (str): Cadena JSON con los datos del pago.

        Returns:
            Pago: Instancia de Pago creada a partir del JSON.
        """
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            monto = data_dict['monto'],
            fecha_pago = data_dict['fecha_pago']
        )