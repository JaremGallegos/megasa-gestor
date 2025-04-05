from __future__ import annotations
from abc import abstractmethod, ABC
from src.model.Usuario import Usuario
from src.model.CategoriaLaboral import CategoriaLaboral
import json

class Empleado(ABC):
    # Atributo de clase para llevar la cuenta del último ID asignado a un empleado.
    ultimo_id: int = 0
    
    def __init__(self, 
                 id: int = 0, 
                 nombre: str = "", 
                 email: str = "", 
                 usuario: Usuario = None) -> None:
        """
        Inicializa una nueva instancia de Empleado.
        
        Args:
            id (int, opcional): Identificador del empleado. Por defecto es 0.
            nombre (str, opcional): Nombre del empleado.
            email (str, opcional): Email del empleado.
            usuario (Usuario, opcional): Objeto Usuario asociado al empleado.
        """
        self._id = id
        self._nombre = nombre
        self._email = email
        self._usuario = usuario if usuario is not None else None
    
    @property
    def id(self) -> int:
        """
        Obtiene el ID del empleado.
        
        Returns:
            int: Identificador del empleado.
        """
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Establece el ID del empleado.
        
        Args:
            id (int): Nuevo identificador.
        """
        self._id = id

    @property
    def nombre(self) -> str:
        """
        Obtiene el nombre del empleado.
        
        Returns:
            str: Nombre del empleado.
        """
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        """
        Establece el nombre del empleado.
        
        Args:
            nombre (str): Nuevo nombre del empleado.
        """
        self._nombre = nombre

    @property
    def email(self) -> str:
        """
        Obtiene el email del empleado.
        
        Returns:
            str: Email del empleado.
        """
        return self._email
    
    @email.setter
    def email(self, email: str) -> None:
        """
        Establece el email del empleado.
        
        Args:
            email (str): Nuevo email del empleado.
        """
        self._email = email

    @property
    def usuario(self) -> Usuario:
        """
        Obtiene el objeto Usuario asociado al empleado.
        
        Returns:
            Usuario: Objeto Usuario del empleado.
        """
        return self._usuario
    
    @usuario.setter
    def usuario(self, usuario: Usuario) -> None:
        """
        Establece el objeto Usuario asociado al empleado.
        
        Args:
            usuario (Usuario): Nuevo objeto Usuario.
        """
        self._usuario = usuario

    @abstractmethod
    def registrar_empleado(self, nombre: str, email: str, usuario: Usuario) -> None:
        """
        Método abstracto para registrar un empleado.
        
        Debe ser implementado en las subclases para definir cómo se registra un empleado.
        
        Args:
            nombre (str): Nombre del empleado.
            email (str): Email del empleado.
            usuario (Usuario): Objeto Usuario asociado al empleado.
        """
        pass
    
    @abstractmethod
    def actualizar_datos(self, nombre: str = None, email: str = None, usuario: Usuario = None) -> None:
        """
        Método abstracto para actualizar los datos de un empleado.
        
        Debe ser implementado en las subclases para definir cómo se actualizan los datos.
        
        Args:
            nombre (str, opcional): Nuevo nombre del empleado.
            email (str, opcional): Nuevo email del empleado.
            usuario (Usuario, opcional): Nuevo objeto Usuario asociado.
        """
        pass
    
    def to_json(self) -> str:
        """
        Serializa el objeto Empleado a una cadena JSON.
        
        Returns:
            str: Representación JSON del empleado.
        """
        return json.dumps({
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'usuario': self.usuario.to_json() if self.usuario is not None else None
        })