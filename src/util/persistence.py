import json

def guardar_data(data, archivo):
    """
    Guardar data en el archivo JSON especificado.
    """
    with open(archivo, 'w') as file:
        json.dump(data, file, indent = 4, default = str) # Convierte fechas u otros objetos
        
def cargar_data(archivo):
    """
    Carga y retorna datos desde el archivo JSON. Si no existe, retorna None
    """
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
    
    