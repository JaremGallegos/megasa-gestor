from __future__ import annotations
import json

class Usuario:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password
    
    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, value: str):
        self._username = value

    @property
    def password(self) -> str:
        return self._password
    
    @password.setter
    def password(self, value: str):
        self._password = value

    def autenticar(self, input_user: str, input_pass: str) -> bool:
        return self._username == input_user and self._password == input_pass

    def registrar_usuario(self, username: str, password: str) -> None:
        self._username = username
        self._password = password

    def cambiar_password(self, nueva_password: str) -> None:
        self._password = nueva_password

    def obtener_username(self) -> str:
        return self._username

    def to_json(self) -> str:
        return json.dumps({
            'username': self._username,
            'password': self._password
        })

    @classmethod
    def from_json(cls, data: str) -> 'Usuario':
        data_dict = json.loads(data)
        return cls(
            username=data_dict['username'],
            password=data_dict['password']
        )