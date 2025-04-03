from __future__ import annotations
from src.model.Usuario import Usuario
from src.model.CategoriaLaboral import CategoriaLaboral
import json

class Empleado:
    def __init__(self, 
                 id: int, 
                 nombre: str, 
                 email: str, 
                 rol: str, 
                 usuario: Usuario, 
                 categoria: CategoriaLaboral):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._rol = rol
        self._usuario = usuario
        self._categoria = categoria
    
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        self._id = value

    @property
    def nombre(self) -> str:
        return self._nombre
    
    @nombre.setter
    def nombre(self, value: str):
        self._nombre = value

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, value: str):
        self._email = value

    @property
    def rol(self) -> str:
        return self._rol
    
    @rol.setter
    def rol(self, value: str):
        self._rol = value

    @property
    def usuario(self) -> Usuario:
        return self._usuario
    
    @usuario.setter
    def usuario(self, value: Usuario):
        self._usuario = value

    @property
    def categoria(self) -> CategoriaLaboral:
        return self._categoria
    
    @categoria.setter
    def categoria(self, value: CategoriaLaboral):
        self._categoria = value
        
    def actualizar_datos(self) -> None:
        # Lógica para actualizar datos del empleado
        pass

    def asignar_a_rol(self, nuevo_rol: str) -> None:
        self._rol = nuevo_rol

    def obtener_perfil(self) -> str:
        return f"ID: {self._id}, Nombre: {self._nombre}, Email: {self._email}, Rol: {self._rol}"
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self._id,
            'nombre': self._nombre,
            'email': self._email,
            'rol': self._rol,
            'usuario': self._usuario.to_json(),
            'categoria': self._categoria.to_json()
        })

    @classmethod
    def from_json(cls, data: str) -> 'Empleado':
        data_dict = json.loads(data)
        usuario = Usuario.from_json(data_dict['usuario'])
        categoria = CategoriaLaboral.from_json(data_dict['categoria'])
        return cls(
            id=data_dict['id'],
            nombre=data_dict['nombre'],
            email=data_dict['email'],
            rol=data_dict['rol'],
            usuario=usuario,
            categoria=categoria
        )
