from __future__ import annotations
import json

class Anuncio:
    def __init__(self, id: int, descripcion: str, estado: str):
        self._id = id
        self._descripcion = descripcion
        self._estado = estado
        
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
    def descripcion(self, descripcion: str) -> None:
        self._descripcion = descripcion

    @property
    def estado(self) -> str:
        return self._estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        self._estado = estado
        
    def registrar_anuncio(self) -> None:
        """
        Registra el anuncio validando que la descripción no esté vacía y estableciendo
        el estado inicial como 'En preparación'.
        """
        if not self.descripcion or not self.descripcion.strip():
            raise ValueError("La descripción del anuncio no puede estar vacía.")
        
        self.estado = "En preparación"

    def registrar_finalizacion(self) -> None:
        """
        Finaliza el anuncio verificando que se encuentre en un estado válido para ser finalizado.
        Si el anuncio ya está finalizado, se lanza una excepción.
        En caso contrario, se actualiza el estado del anuncio a 'Finalizado'.
        """
        if self.estado == "Finalizado":
            raise ValueError("El anuncio ya se encuentra finalizado.")

        estados_validos = ["En preparación", "En ejecución"]
        if self.estado not in estados_validos:
            raise ValueError("El anuncio no se puede finalizar desde el estado actual.")
        
        self.estado = "Finalizado"

    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'descripcion': self.descripcion,
            'estado': self.estado
        })

    @classmethod
    def from_json(cls, data: str) -> 'Anuncio':
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            descripcion = data_dict['descripcion'],
            estado = data_dict['estado']
        )