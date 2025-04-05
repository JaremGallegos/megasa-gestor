from __future__ import annotations
# Se importan las clases necesarias del modelo.
from src.model.Usuario import Usuario
from src.model.CategoriaLaboral import CategoriaLaboral
from src.model.DirectorCampana import DirectorCampana
from src.model.PersonalContable import PersonalContable
from src.model.PersonalContacto import PersonalContacto
from src.model.PersonalCreativo import PersonalCreativo
import json, os

class UsuarioController:
    def __init__(self, file_path: str = "./data/usuarios.json") -> None:
        """
        Inicializa el controlador de usuarios, estableciendo la ruta del archivo JSON
        y cargando los usuarios registrados en un diccionario.
        
        Args:
            file_path (str): Ruta del archivo JSON que contiene la información de usuarios.
        """
        self.file_path = file_path
        # Carga los usuarios desde el archivo JSON al iniciar el controlador.
        self.usuarios = self.cargar_usuarios()
        
    def cargar_usuarios(self) -> dict[str, Usuario]:
        """
        Carga los usuarios del archivo JSON y los almacena en un diccionario.
        
        Returns:
            dict[str, Usuario]: Diccionario donde la clave es el username y el valor es un objeto Usuario.
            Retorna un diccionario vacío en caso de error o si el archivo no existe.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try:
                    # Decodifica el contenido del archivo JSON.
                    data = json.load(file)
                    usuarios = {}
                    # Itera sobre cada registro para crear instancias de Usuario.
                    for u in data:
                        usuario = Usuario(
                            username = u['username'], 
                            password = u['password'],
                            rol = CategoriaLaboral[u['rol']]
                        )
                        # Almacena el usuario en el diccionario usando el username como clave.
                        usuarios[usuario.username] = usuario
                    return usuarios
                except json.JSONDecodeError:
                    # Si ocurre un error al decodificar el JSON, se retorna un diccionario vacío.
                    return {}
        # Retorna un diccionario vacío si el archivo no existe.
        return {}
    
    def guardar_usuarios(self) -> None:
        """
        Guarda los usuarios en el archivo JSON.
        
        Serializa el diccionario de usuarios a una lista de diccionarios y sobreescribe el archivo
        JSON con la información actualizada.
        """
        data = []
        # Recorre todos los usuarios y prepara su representación en diccionario.
        for usuario in self.usuarios.values():
            data.append({
                'username': usuario.username,
                'password': usuario.password,
                'rol': usuario.rol.name # Se almacena el nombre del Enum para facilitar la reconstrucción.
            })
        with open(self.file_path, 'w', encoding = 'utf-8') as file:
            json.dump(data, file, indent = 4)
            
    def autentificar(self, username: str, password: str) -> bool:
        """
        Verifica las credenciales de un usuario.
        
        Busca al usuario en el diccionario y, si existe, llama al método 'autenticar' del objeto Usuario.
        
        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.
            
        Returns:
            bool: True si las credenciales son correctas, False en caso contrario.
        """
        usuario = self.usuarios.get(username)
        if usuario and usuario.autenticar(username, password):
            return True
        return False
    
    def registrar_usuario(self, nombre: str, email: str, username: str, password: str, rol: CategoriaLaboral) -> bool:
        """
        Registra un nuevo usuario si no existe previamente.
        
        Verifica que no se encuentre un usuario con el mismo username. Si es nuevo, crea una instancia
        de Usuario y del empleado correspondiente según el rol. Luego registra el empleado y persiste la información.
        
        Args:
            nombre (str): Nombre del empleado.
            email (str): Email del empleado.
            username (str): Nombre de usuario para el acceso.
            password (str): Contraseña del usuario.
            rol (CategoriaLaboral): Rol asignado al usuario, basado en el Enum CategoriaLaboral.
            
        Returns:
            bool: True si el usuario se registra exitosamente, False si ya existe.
        """
        if username in self.usuarios:
            # Si el usuario ya existe, retorna False.
            return False
        
        # Crea la instancia del usuario.
        nuevo_usuario = Usuario(username, password, rol)
        # Agrega el usuario al diccionario.
        self.usuarios[username] = nuevo_usuario
        
        # Según el rol, se crea el empleado correspondiente.
        if rol == CategoriaLaboral.DIRECTOR_CAMPAÑA:
            empleado = DirectorCampana(nombre = nombre, email = email, usuario = nuevo_usuario)
        elif rol == CategoriaLaboral.PERSONAL_CONTABLE:
            empleado = PersonalContable(nombre = nombre, email = email, usuario = nuevo_usuario)
        elif rol == CategoriaLaboral.PERSONAL_CONTACTO:
            empleado = PersonalContacto(nombre = nombre, email = email, usuario = nuevo_usuario)
        elif rol == CategoriaLaboral.PERSONAL_CREATIVO:
            empleado = PersonalCreativo(nombre = nombre, email = email, usuario = nuevo_usuario)
        else:
            # Si el rol no coincide con ninguno esperado, se retorna False.
            return False
        
        # Registra al empleado (este método debe estar implementado en la clase correspondiente).
        empleado.registrar_empleado(nombre, email, nuevo_usuario)
        # Persiste la información de usuarios en el archivo JSON.
        self.guardar_usuarios()
        return True
    
    def cambiar_password(self, username: str, nuevo_password: str) -> bool:
        """
        Actualiza la contraseña de un usuario existente.
        
        Busca al usuario en el diccionario y, si existe, actualiza la contraseña y guarda los cambios.
        
        Args:
            username (str): Nombre de usuario.
            nuevo_password (str): Nueva contraseña a asignar.
            
        Returns:
            bool: True si la actualización es exitosa, False si el usuario no existe.
        """
        if username in self.usuarios:
            # Se actualiza la contraseña; se asume que la propiedad 'password' permite asignación directa.
            self.usuarios[username].password = nuevo_password
            # Guarda los cambios en el archivo JSON.
            self.guardar_usuarios()
            return True
        return False