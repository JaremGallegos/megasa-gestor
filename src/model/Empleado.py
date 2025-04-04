from __future__ import annotations
from abc import abstractmethod, ABC
from src.model.Usuario import Usuario
from src.model.CategoriaLaboral import CategoriaLaboral
import json

class Empleado(ABC):
    ultimo_id: int = 0
    def __init__(self, 
                 id: int = 0, 
                 nombre: str = "", 
                 email: str = "", 
                 usuario: Usuario = None) -> None:
        self._id = id
        self._nombre = nombre
        self._email = email
        self._usuario = usuario if usuario is not None else None
    
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
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, email: str) -> None:
        self._email = email

    @property
    def usuario(self) -> Usuario:
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario: Usuario) -> None:
        self._usuario = usuario

    @abstractmethod
    def registrar_empleado(self, nombre: str, email: str, usuario: Usuario) -> None:
        pass
    
    @abstractmethod
    def actualizar_datos(self, nombre: str = None, email: str = None, usuario: Usuario = None) -> None:
        pass
    
    @abstractmethod
    def asignar_usuario(self) -> None:
        pass
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'usuario': self.usuario.to_json() if self.usuario is not None else None
        })