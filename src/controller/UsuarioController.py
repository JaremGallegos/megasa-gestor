from src.model.Usuario import Usuario
from src.model.CategoriaLaboral import CategoriaLaboral
import json, os

class UsuarioController:
    def __init__(self, file_path: str = "./data/usuarios.json") -> None:
        self.file_path = file_path
        self.usuarios = self.cargar_usuarios()
        
    def cargar_usuarios(self) -> dict[str, Usuario]:
        """
        Carga los usuarios del archivo JSON y los almacena en un diccionario
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    data = json.load(file)
                    usuarios = {}
                    for u in data:
                        usuario = Usuario(
                            username = u['username'], 
                            password = u['password'],
                            rol = CategoriaLaboral[u['rol']]
                        )
                        usuarios[usuario.username] = usuario
                    return usuarios
                except json.JSONDecodeError:
                    return {}
        return {}
    
    def guardar_usuarios(self) -> None:
        """
        Guardar los usuarios en el archivo JSON.
        """
        data = []
        for usuario in self.usuarios.values():
            data.append({
                'username': usuario.username,
                'password': usuario.password,
                'rol': usuario.rol.name
            })
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent = 4)
            
    def autentificar(self, username: str, password: str) -> bool:
        """
        Verificar las credenciales de un usuario.
        """
        usuario = self.usuarios.get(username)
        if usuario and usuario.autenticar(username, password):
            return True
        return False
    
    def registrar_usuario(self, username: str, password: str, rol: CategoriaLaboral) -> bool:
        """
        Registra un nuevo usuario si no existe.
        """
        if username in self.usuarios:
            return False
        nuevo_usuario = Usuario(username, password, rol)
        self.usuarios[username] = nuevo_usuario
        self.guardar_usuarios()
        return True
    
    def cambiar_password(self, username: str, nuevo_password: str) -> bool:
        """
        Actualiza la contraseña de un usuario existente.
        """
        if username in self.usuarios:
            self.usuarios[username].password(nuevo_password)
            self.guardar_usuarios()
            return True
        return False