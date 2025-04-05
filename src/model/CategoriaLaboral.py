from __future__ import annotations
from enum import Enum
import json

class CategoriaLaboral(Enum):
    # Definición de los miembros del Enum con sus respectivos valores:
    # (id, nombre, sueldo_base)
    DIRECTOR_CAMPAÑA = (1, "Director Campaña", 1000.0)
    PERSONAL_CONTABLE = (2, "Personal Contable", 800.0)
    PERSONAL_CONTACTO = (3, "Personal Contacto", 700.0)
    PERSONAL_CREATIVO = (4, "Personal Creativo", 600.0)
    
    def __init__(self, 
                 id: int = 0, 
                 nombre: str = "", 
                 sueldo_base: float = 0.0) -> None:
        """
        Inicializa una instancia de CategoriaLaboral con los valores proporcionados.
        
        Args:
            id (int): Identificador único de la categoría.
            nombre (str): Nombre descriptivo de la categoría.
            sueldo_base (float): Sueldo base asociado a la categoría.
        """
        self._id = id
        self._nombre = nombre
        self._sueldo_base = sueldo_base
        
    @property
    def id(self) -> int:
        """
        Obtiene el identificador único de la categoría.
        
        Returns:
            int: El id de la categoría.
        """
        return self._id

    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre descriptivo de la categoría.
        
        Returns:
            str: El nombre de la categoría.
        """
        return self._nombre
    
    @property
    def sueldo_base(self) -> float:
        """
        Obtiene el sueldo base asociado a la categoría.
        
        Returns:
            float: El sueldo base.
        """
        return self._sueldo_base
    
    def to_json(self) -> str:
        """
        Convierte el objeto CategoriaLaboral en una cadena JSON.
        
        Returns:
            str: Cadena JSON que representa la categoría con sus atributos.
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
        Se busca en el Enum el miembro que coincida con el id proporcionado en el JSON.
        
        Args:
            data (str): Cadena JSON que contiene los datos de la categoría.
        
        Returns:
            CategoriaLaboral: Miembro del Enum que coincide con el id.
        
        Raises:
            ValueError: Si no se encuentra una categoría con el id especificado.
        """
        data_dict = json.loads(data)
        for categoria in cls:
            if categoria.id == data_dict["id"]:
                return categoria
        
        raise ValueError("Categoría no encontrada en el Enum")