from __future__ import annotations
from src.model.Empleado import Empleado
from src.model.Usuario import Usuario
import json

class DirectorCampana(Empleado):
    def __init__(self, 
                 id: int = 0,
                 nombre: str = "",
                 email: str = "",
                 usuario: Usuario = None) -> None:
        """
        Inicializa una nueva instancia de DirectorCampana, extendiendo la clase Empleado.
        
        Args:
            id (int, opcional): Identificador del empleado. Por defecto es 0.
            nombre (str, opcional): Nombre del empleado.
            email (str, opcional): Email del empleado.
            usuario (Usuario, opcional): Objeto Usuario asociado al empleado.
        """
        super().__init__(id, nombre, email, usuario)
    
    def registrar_empleado(self, nombre: str, email: str, usuario: Usuario) -> None:
        """
        Registra un empleado asignándole un id autogenerado.
        La asignación del id se realiza mediante un autoincremento en la variable de clase.
        
        Args:
            nombre (str): Nombre del empleado.
            email (str): Email del empleado.
            usuario (Usuario): Objeto Usuario asociado al empleado.
        """
        # Incrementa el último id asignado en la clase Empleado
        Empleado.ultimo_id += 1
        self.id = Empleado.ultimo_id
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        
        print(f"Director de Campaña registrado con id {self._id}.")

    def actualizar_datos(self, nombre: str = None, email: str = None, usuario: Usuario = None) -> None:
        """
        Actualiza los datos del Director de Campaña. Si se proporciona un nuevo valor,
        se actualiza; de lo contrario, se mantiene el valor actual.
        
        Args:
            nombre (str, opcional): Nuevo nombre. Si es None, no se actualiza.
            email (str, opcional): Nuevo email. Si es None, no se actualiza.
            usuario (Usuario, opcional): Nuevo objeto Usuario. Si es None, no se actualiza.
        """
        if nombre is not None:
            self.nombre = nombre
        if email is not None:
            self.email = email
        if usuario is not None:
            self.usuario = usuario
            
        print(f"Datos del Director de Campaña (id: {self.id}) actualizados.")

    def to_json(self) -> str:
        """
        Convierte el objeto DirectorCampana en una cadena JSON.
        Se utiliza el método to_json() de la clase Empleado.
        
        Returns:
            str: Cadena JSON que representa al Director de Campaña.
        """
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'DirectorCampana':
        """
        Crea un objeto DirectorCampana a partir de una cadena JSON.
        
        Args:
            data (str): Cadena JSON con los datos del Director de Campaña.
        
        Returns:
            DirectorCampana: Instancia creada a partir del JSON.
        """
        data_dict: dict = json.loads(data)
        # Deserializa el objeto Usuario si está presente en los datos
        usuario = Usuario.from_json(data_dict['usuario']) if data_dict.get('usuario') else None
        return cls(
            id = data_dict['id'],
            nombre = data_dict['nombre'],
            email = data_dict['email'],
            usuario = usuario,
        )