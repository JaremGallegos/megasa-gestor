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
        super().__init__(id, nombre, email, usuario)    

    def registrar_empleado(self, nombre: str, email: str, usuario: Usuario) -> None:
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
        """
        if nombre is not None:
            self.nombre = nombre
        if email is not None:
            self.email = email
        if usuario is not None:
            self.usuario = usuario
            
        print(f"Datos del Personal Creativo (id: {self.id}) actualizados.")
        
    def asignar_usuario(self) -> None:
        """
        Asigna un objeto Usuario al Personal Creativo
        """
        pass

    def to_json(self) -> str:
        """
        Convierte el objeto Empleado en una cadena JSON
        """
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'PersonalCreativo':
        """
        Crea un objeto Empleado a partir de una cadena JSON.
        """
        data_dict: dict = json.loads(data)
        usuario = Usuario.from_json(data_dict['usuario']) if data_dict.get('usuario') else None
        return cls (
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            email = data_dict['email'],
            usuario = usuario,
        )