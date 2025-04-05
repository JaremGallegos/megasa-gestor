from __future__ import annotations
from datetime import datetime, date
import json

def str_to_date(fecha_str: str) -> date:
    """
    Convierte una cadena de fecha en formato "YYYY-MM-DD" a un objeto date.

    Args:
        fecha_str (str): Cadena que representa la fecha.

    Returns:
        date: Objeto de fecha correspondiente.
    """
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()

def date_to_str(fecha_date: date) -> str:
    """
    Convierte un objeto date a una cadena en formato "YYYY-MM-DD".

    Args:
        fecha_date (date): Objeto de fecha.

    Returns:
        str: Cadena que representa la fecha.
    """
    return fecha_date.strftime("%Y-%m-%d")

class NotaConceptual:
    # Atributo de clase para llevar la cuenta del último ID asignado.
    ultimo_id = 0
    
    def __init__(self, 
                 id: int = 0, 
                 descripcion: str = "", 
                 fecha: str = "") -> None:
        """
        Inicializa una nueva instancia de NotaConceptual.

        Args:
            id (int, opcional): Identificador de la nota. Por defecto es 0.
            descripcion (str, opcional): Descripción o idea de la nota conceptual.
            fecha (str, opcional): Fecha de registro en formato "YYYY-MM-DD".
                                  Si no se proporciona o es vacía, se asigna None.
        """
        self._id = id
        self._descripcion = descripcion
        # Convierte la cadena de fecha a un objeto date si es válida.
        self._fecha = str_to_date(fecha) if isinstance(fecha, str) and fecha.strip() != "" else None
        
    @property
    def id(self) -> int:
        """
        Obtiene el ID de la nota conceptual.

        Returns:
            int: Identificador de la nota.
        """
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Establece el ID de la nota conceptual.

        Args:
            id (int): Nuevo identificador.
        """
        self._id = id

    @property
    def descripcion(self) -> str:
        """
        Obtiene la descripción de la nota conceptual.

        Returns:
            str: Descripción de la nota.
        """
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion: str):
        """
        Establece la descripción de la nota conceptual.

        Args:
            descripcion (str): Nueva descripción.
        """
        self._descripcion = descripcion

    @property
    def fecha(self) -> str:
        """
        Obtiene la fecha de la nota conceptual en formato string.

        Returns:
            str: Fecha en formato "YYYY-MM-DD" o None si no está definida.
        """
        return self._fecha if self._fecha else None
    
    @fecha.setter
    def fecha(self, fecha: str) -> None:
        """
        Establece la fecha de la nota conceptual a partir de un string.

        Args:
            fecha (str): Fecha en formato "YYYY-MM-DD".
        """
        self._fecha = str_to_date(fecha) if fecha and fecha.strip() else None
        
    def registrar_nota(self, descripcion: str, fecha: str) -> None:
        """
        Registra la idea de anuncio validando que la descripción no esté vacía,
        asigna un ID autogenerado y establece la fecha proporcionada.

        Args:
            descripcion (str): Texto de la idea o nota conceptual.
            fecha (str): Fecha de registro en formato "YYYY-MM-DD".

        Raises:
            ValueError: Si la descripción está vacía.
        """
        if not descripcion.strip():
            raise ValueError("La descripción del anuncio no puede estar vacía.")
        
        # Incrementa el contador de ID y lo asigna a la nota conceptual.
        NotaConceptual.ultimo_id += 1
        self.id = NotaConceptual.ultimo_id
        self.descripcion = descripcion
        self.fecha = fecha
        
        print(f"Nota conceptual registrada correctamente con id {self.id}.")

    def to_json(self) -> str:
        """
        Serializa el objeto NotaConceptual a una cadena JSON.

        Returns:
            str: Cadena JSON que representa la nota conceptual.
        """
        return json.dumps({
            'id': self.id,
            'descripcion': self.descripcion,
            'fecha': self.fecha
        })

    @classmethod
    def from_json(cls, data: str) -> 'NotaConceptual':
        """
        Crea un objeto NotaConceptual a partir de una cadena JSON.

        Args:
            data (str): Cadena JSON con los datos de la nota.

        Returns:
            NotaConceptual: Instancia de NotaConceptual creada a partir del JSON.
        """
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            descripcion = data_dict['descripcion'],
            fecha = data_dict['fecha']
        )