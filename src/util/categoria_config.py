# Se importan las clases necesarias del modelo.
from src.model.CategoriaLaboral import CategoriaLaboral
import json, os

# Ruta del archivo de configuración que almacena los sueldos base actualizados.
CONFIG_FILE = './data/sueldos_config.json'

def cargar_config() -> dict:
    """
    Carga la configuración de sueldos desde un archivo JSON.
    
    Si el archivo existe, se decodifica su contenido y se retorna como diccionario.
    En caso de error en la decodificación o si el archivo no existe, se retorna un diccionario
    con los sueldos base definidos en el Enum CategoriaLaboral.
    
    Returns:
        dict: Diccionario que asocia el nombre del Enum con el sueldo base actualizado.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding = "utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print("Error al cargar la configuración:", e)
                return {}
    else:
        # Si el archivo no existe, se retorna la configuración por defecto usando los valores del Enum.
        return {
            "DIRECTOR_CAMPAÑA": CategoriaLaboral.DIRECTOR_CAMPAÑA.sueldo_base,
            "PERSONAL_CONTABLE": CategoriaLaboral.PERSONAL_CONTABLE.sueldo_base,
            "PERSONAL_CONTACTO": CategoriaLaboral.PERSONAL_CONTACTO.sueldo_base,
            "PERSONAL_CREATIVO": CategoriaLaboral.PERSONAL_CREATIVO.sueldo_base
        }
        
def guardar_config(config: dict) -> None:
    """
    Guarda la configuración de sueldos en el archivo JSON.
    
    Se asegura que el directorio del archivo exista antes de escribir el archivo.
    
    Args:
        config (dict): Diccionario con la configuración de sueldos.
    """
    # Asegura que el directorio del archivo exista; si no, lo crea.
    os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok = True)
    with open(CONFIG_FILE, "w", encoding = "utf-8") as file:
        json.dump(config, file, indent = 4)
        
def get_sueldo_base(categoria: CategoriaLaboral, config: dict = None) -> float:
    """
    Retorna el sueldo base actualizado para una categoría laboral.
    
    Se consulta la configuración cargada desde el archivo JSON. Si no se proporciona la
    configuración, se carga la configuración por defecto. Se retorna el sueldo base actualizado
    según la configuración, o el valor por defecto definido en el Enum.
    
    Args:
        categoria (CategoriaLaboral): Categoría laboral (Enum).
        config (dict, opcional): Configuración cargada. Si no se proporciona, se carga la configuración.
    
    Returns:
        float: Sueldo base actualizado o, en su defecto, el valor por defecto del Enum.
    """
    if config is None:
        config = cargar_config()
    return config.get(categoria.name, categoria.sueldo_base)

def set_sueldo_base(categoria: CategoriaLaboral, nuevo_sueldo: float) -> None:
    """
    Actualiza el sueldo base para una categoría laboral y guarda la configuración.
    
    Se carga la configuración actual, se actualiza el sueldo para la categoría indicada y
    se guarda la nueva configuración en el archivo JSON.
    
    Args:
        categoria (CategoriaLaboral): Categoría laboral (Enum).
        nuevo_sueldo (float): Nuevo sueldo base a asignar.
    """
    config = cargar_config()
    config[categoria.name] = nuevo_sueldo
    guardar_config(config)