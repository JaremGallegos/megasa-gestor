from __future__ import annotations
# Se importan las clases necesarias del modelo.
from src.model.Anuncio import Anuncio
from typing import List
import json, os, logging

# Configuración de logging para auditoría de anuncio.
# Se define el archivo de log, nivel de detalle y formato.
logging.basicConfig(
    filename = './logging/auditoria_anuncio.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class AnuncioController:
    def __init__(self, file_path: str = '/data/anuncio.json') -> None:
        """
        Inicializa el controlador de anuncios.
        
        Args:
            file_path (str): Ruta del archivo JSON donde se almacenan los anuncios.
        """
        self.file_path = file_path
        self.anuncios: List[Anuncio] = self.cargar_anuncios()
        
    def cargar_anuncios(self) -> List[Anuncio]:
        """
        Carga los anuncios desde el archivo JSON y los almacena en una lista.
        
        Returns:
            List[Anuncio]: Lista de objetos Anuncio cargados desde el archivo. Si ocurre un error,
            se retorna una lista vacía.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try:
                    data = json.load(file)
                    anuncios = []
                    # Se recorre cada registro y se crea un objeto Anuncio
                    for a in data:
                        anuncio = Anuncio(
                            id = a["id"],
                            descripcion = a["descripcion"],
                            estado = a["estado"]
                        )
                        anuncios.append(anuncio)
                    return anuncios
                except json.JSONDecodeError as e:
                    logging.error("Error al decodificar JSON: %s", e)
                    return []
        return []
    
    def guardar_anuncios(self) -> None:
        """
        Guarda la lista de anuncios en el archivo JSON.
        Se sobrescribe el archivo con la lista actualizada.
        """
        # Se obtiene la representación de cada anuncio a partir de su método to_json()
        data = [json.loads(anuncio.to_json()) for anuncio in self.anuncios]
        try:
            with open(self.file_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            logging.error("Error al guardar anuncios en JSON: %s", e)
        
    def registrar_anuncio(self, descripcion: str) -> bool:
        """
        UC8: Registrar Anuncio de Campaña
        
        Valida que la descripción no esté vacía y que no exista ya un anuncio con la misma descripción.
        Si es válido, se registra el anuncio con un estado inicial de 'En preparación', se asigna un ID único,
        se agrega a la lista de anuncios y se guarda la operación para auditoría.
        
        Args:
            descripcion (str): Descripción del anuncio.
            
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado o error.
        """
        # Validación de duplicados: si existe un anuncio con la misma descripción, se rechaza
        if any(a.descripcion == descripcion for a in self.anuncios):
            logging.error("Error: Ya existe un anuncio con la misma descripción.")
            return False
        
        # Se genera un nuevo ID único basado en el máximo de los IDs existentes
        nueva_id = max((a.id for a in self.anuncios), default = 0) + 1
        
        # Se crea el anuncio y se utiliza el método registrar_anuncio del modelo para inicializarlo
        nuevo_anuncio = Anuncio()
        nuevo_anuncio.registrar_anuncio(descripcion)
        nuevo_anuncio.id = nueva_id
        
        self.anuncios.append(nuevo_anuncio)
        self.guardar_anuncios()
        logging.info("Registro de auditoría: Se agrego un nuevo anuncio con id %s.", nuevo_anuncio.id)
        return True
        
    def registrar_finalizacion_anuncio(self, id: int) -> bool:
        """
        UC9: Registrar Finalización de Anuncio
        
        Busca el anuncio por su ID y, si está en estado 'En preparación', lo finaliza (cambia su estado a 'Finalizado')
        y registra la fecha de finalización. Se guarda la operación para auditoría.
        
        Args:
            id (int): ID del anuncio a finalizar
        
        Returns:
            bool: True si la finalización fue exitosa, False en caso de error o si no se
            encuentra el anuncio.
        """
        for anuncio in self.anuncios:
            if anuncio.id == id:
                try:
                    # Se intenta finalizar el anuncio; si ya está finalizado, se lanzará una excepción
                    anuncio.registrar_finalizacion()
                    self.guardar_anuncios()
                    logging.info("Registro de auditoría: Se finalizó el anuncio con id %s.", id)
                    return True
                except Exception as e:
                    logging.error("Error al finalizar el anuncio con id %s: %s", id, e)
                    return False
                
        logging.error("Anuncio con id %s no encontrado para finalización.", id)
        return False