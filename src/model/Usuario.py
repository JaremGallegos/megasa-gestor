from __future__ import annotations
from src.model.CategoriaLaboral import CategoriaLaboral
import json

class Usuario:
    def __init__(self, 
                 username: str = "", 
                 password: str = "", 
                 rol: CategoriaLaboral = None) -> None:
        """
        Inicializa una nueva instancia de Usuario.

        Args:
            username (str, opcional): Nombre de usuario.
            password (str, opcional): Contraseña del usuario.
            rol (CategoriaLaboral, opcional): Rol asignado al usuario. Si no se proporciona, se asigna como lista vacía.
        """
        self._username = username
        self._password = password
        # Se asigna rol; si no se proporciona, se establece como una lista vacía.
        self._rol = rol if rol is not None else []
    
    @property
    def username(self) -> str:
        """
        Obtiene el nombre de usuario.

        Returns:
            str: El nombre de usuario.
        """
        return self._username
    
    @username.setter
    def username(self, username: str) -> None:
        """
        Establece el nombre de usuario.

        Args:
            username (str): Nuevo nombre de usuario.
        """
        self._username = username

    @property
    def password(self) -> str:
        """
        Obtiene la contraseña del usuario.

        Returns:
            str: La contraseña del usuario.
        """
        return self._password
    
    @password.setter
    def password(self, password: str) -> None:
        """
        Establece la contraseña del usuario.

        Args:
            password (str): Nueva contraseña.
        """
        self._password = password
        
    @property
    def rol(self) -> CategoriaLaboral:
        """
        Obtiene el rol asignado al usuario.

        Returns:
            CategoriaLaboral: El rol del usuario.
        """
        return self._rol
    
    @rol.setter
    def rol(self, rol: CategoriaLaboral) -> None:
        """
        Establece el rol del usuario.

        Args:
            rol (CategoriaLaboral): Nuevo rol a asignar.
        """
        self._rol = rol

    def autenticar(self, input_user: str, input_pass: str) -> bool:
        """
        Verifica las credenciales del usuario comparándolas con las almacenadas.

        Args:
            input_user (str): Nombre de usuario ingresado.
            input_pass (str): Contraseña ingresada.
        
        Returns:
            bool: True si las credenciales son correctas, False en caso contrario.
        """
        return self.username == input_user and self.password == input_pass

    def registrar_usuario(self, username: str, password: str) -> None:
        """
        Registra un nuevo usuario asignando un nombre de usuario y contraseña.

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.
        """
        self.username = username
        self.password = password

    def to_json(self) -> str:
        """
        Convierte el objeto Usuario en una cadena JSON.

        Returns:
            str: Representación JSON del usuario.
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

        Args:
            data (str): Cadena JSON que contiene los datos del usuario.
        
        Returns:
            Usuario: Instancia de Usuario creada a partir del JSON.
        """
        data_dict = json.loads(data)
        # Se recupera el rol a partir del nombre usando el Enum CategoriaLaboral.
        rol = CategoriaLaboral[data_dict['rol']]
        return cls(
            username = data_dict['username'],
            password = data_dict['password'],
            rol = rol
        )