from __future__ import annotations
import json

class Anuncio:
    # Atributo de clase que almacena el último ID asignado a un anuncio.
    ultimo_id = 0
    def __init__(self, 
                 id: int = 0, 
                 descripcion: str = "", 
                 estado: str = "En preparación") -> None:
        """
        Inicializa una nueva instancia de la clase Anuncio.
        
        Args:
            id (int, opcional): Identificador del anuncio. Por defecto es 0.
            descripcion (str, opcional): Descripción del anuncio. Por defecto es cadena vacía.
            estado (str, opcional): Estado del anuncio. Por defecto es "En preparación".
        """
        self._id = id
        self._descripcion = descripcion
        self._estado = estado
        
    @property
    def id(self) -> int:
        """
        Propiedad que obtiene el ID del anuncio.
        
        Returns:
            int: El identificador del anuncio.
        """
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Establece el ID del anuncio.
        
        Args:
            id (int): Nuevo identificador para el anuncio.
        """
        self._id = id

    @property
    def descripcion(self) -> str:
        """
        Propiedad que obtiene la descripción del anuncio.
        
        Returns:
            str: La descripción del anuncio.
        """
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion: str) -> None:
        """
        Establece la descripción del anuncio.
        
        Args:
            descripcion (str): Nueva descripción para el anuncio.
        """
        self._descripcion = descripcion

    @property
    def estado(self) -> str:
        """
        Propiedad que obtiene el estado del anuncio.
        
        Returns:
            str: El estado actual del anuncio.
        """
        return self._estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        """
        Establece el estado del anuncio.
        
        Args:
            estado (str): Nuevo estado para el anuncio.
        """
        self._estado = estado
        
    def registrar_anuncio(self, descripcion: str) -> None:
        """
        Registra el anuncio validando que la descripción no esté vacía y estableciendo
        el estado inicial como 'En preparación'.
        
        Args:
            descripcion (str): Descripción del anuncio.
            
        Raises:
            ValueError: Si la descripción está vacía.
        """
        if not descripcion.strip():
            raise ValueError("La descripción del anuncio no puede estar vacía.")
        
        # Incrementa el último ID y lo asigna al anuncio.
        Anuncio.ultimo_id += 1
        self.id = Anuncio.ultimo_id
        self.descripcion = descripcion
        self.estado = "En preparación"
        
        print(f"Anuncio '{self.id}' registrado correctamente con estado '{self.estado}'.")

    def registrar_finalizacion(self, ) -> None:
        """
        Finaliza el anuncio verificando que se encuentre en un estado válido para ser finalizado.
        Si el anuncio ya está finalizado, se lanza una excepción.
        En caso contrario, se actualiza el estado del anuncio a 'Finalizado'.
        
        Raises:
            ValueError: Si el anuncio no está en estado 'En preparación'.
        """
        if self.estado != "En preparación":
            raise ValueError("Solo se puede finalizar un anuncio en preparación.")
        self.estado = "Finalizado"
        
        print(f"Anuncio '{self.id}' finalizada correctamente.")
        
    def to_json(self) -> str:
        """
        Serializa el objeto Anuncio a una cadena en formato JSON.
        
        Returns:
            str: Representación JSON del anuncio.
        """
        return json.dumps({
            'id': self.id,
            'descripcion': self.descripcion,
            'estado': self.estado
        })

    @classmethod
    def from_json(cls, data: str) -> 'Anuncio':
        """
        Crea una instancia de Anuncio a partir de una cadena en formato JSON.
        
        Args:
            data (str): Cadena JSON que contiene los datos del anuncio.
            
        Returns:
            Anuncio: Una nueva instancia de Anuncio creada a partir del JSON.
        """
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            descripcion = data_dict['descripcion'],
            estado = data_dict['estado']
        )