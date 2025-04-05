from __future__ import annotations
from src.model.Empleado import Empleado
from src.model.Usuario import Usuario
from src.model.NotaConceptual import NotaConceptual
import json

class PersonalCreativo(Empleado):
    def __init__(self, 
                 id: int = 0,
                 nombre: str = "",
                 email: str = "",
                 usuario: Usuario = None) -> None:
        """
        Inicializa una nueva instancia de PersonalCreativo.

        Args:
            id (int, opcional): Identificador del empleado. Por defecto es 0.
            nombre (str, opcional): Nombre del empleado. Por defecto es una cadena vacía.
            email (str, opcional): Correo electrónico del empleado. Por defecto es una cadena vacía.
            usuario (Usuario, opcional): Objeto Usuario asociado. Por defecto es None.
        """
        super().__init__(id, nombre, email, usuario)    

    def registrar_empleado(self, nombre: str, email: str, usuario: Usuario) -> None:
        """
        Registra un nuevo empleado asignándole un ID único y estableciendo sus datos.

        Args:
            nombre (str): Nombre del empleado.
            email (str): Correo electrónico del empleado.
            usuario (Usuario): Usuario vinculado al empleado.
        """
        Empleado.ultimo_id += 1
        self.id = Empleado.ultimo_id
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        
        print(f"Personal Creativo registrado con id {self.id}")

    def actualizar_datos(self, nombre: str = None, email: str = None, usuario: Usuario = None) -> None:
        """
        Actualiza los datos del empleado.
        Si se proporciona un nuevo valor, se actualiza; de lo contrario, mantiene el valor actual.

        Args:
            nombre (str, opcional): Nuevo nombre del empleado.
            email (str, opcional): Nuevo correo electrónico.
            usuario (Usuario, opcional): Nuevo objeto Usuario.
        """
        if nombre is not None:
            self.nombre = nombre
        if email is not None:
            self.email = email
        if usuario is not None:
            self.usuario = usuario
            
        print(f"Datos del Personal Creativo (id: {self.id}) actualizados.")

    def to_json(self) -> str:
        """
        Serializa el objeto PersonalCreativo en una cadena JSON.

        Returns:
            str: Cadena JSON que representa al Personal Creativo.
        """
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'PersonalCreativo':
        """
        Crea una instancia de PersonalCreativo a partir de una cadena JSON.

        Args:
            data (str): Cadena JSON con los datos del empleado.

        Returns:
            PersonalCreativo: Objeto deserializado a partir del JSON.
        """
        data_dict: dict = json.loads(data)
        usuario = Usuario.from_json(data_dict['usuario']) if data_dict.get('usuario') else None
        return cls (
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            email = data_dict['email'],
            usuario = usuario,
        )