from __future__ import annotations
from src.model.CategoriaLaboral import CategoriaLaboral
import json

class Usuario:
    def __init__(self, username: str, password: str, rol: CategoriaLaboral) -> None:
        self._username = username
        self._password = password
        self._rol = rol
    
    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, username: str) -> None:
        self._username = username

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, password: str) -> None:
        self._password = password
        
    @property
    def rol(self) -> CategoriaLaboral:
        return self._rol
    
    @rol.setter
    def rol(self, rol: CategoriaLaboral) -> None:
        self._rol = rol

    def autenticar(self, input_user: str, input_pass: str) -> bool:
        """
        Verifica las credenciales del usuario
        """
        return self.username == input_user and self.password == input_pass

    def registrar_usuario(self, username: str, password: str) -> None:
        """
        Registra un nuevo usuario con su nombre de usuario y contraseña
        """
        self.username = username
        self.password = password

    def to_json(self) -> str:
        """
        Convierte el objeto Usuario en una cadena JSON
        """
        return json.dumps({
            'username': self.username,
            'password': self.password,
            'rol': self.rol.name
        })

    @classmethod
    def from_json(cls, data: str) -> 'Usuario':
        """
        Crea un objeto Usuario a partir de una cadena JSON.
        """
        data_dict = json.loads(data)
        rol = CategoriaLaboral[data_dict['rol']]
        return cls(
            username = data_dict['username'],
            password = data_dict['password'],
            rol = rol
        )