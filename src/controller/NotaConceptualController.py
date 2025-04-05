from __future__ import annotations
from src.model.NotaConceptual import NotaConceptual
from typing import List
from datetime import date
import logging, json, os

# Configuración de logging para auditoría de ideas de anuncios.
logging.basicConfig(
    filename = './logging/auditoria_ideas.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s- %(message)s'
)

class NotaConceptualController:
    def __init__(self, file_path: str = './data/ideas.json') -> None:
        """
        Inicializa el controlador de notas conceptuales (ideas de anuncios),
        estableciendo la ruta del archivo JSON y cargando las ideas registradas.
        
        Args:
            file_path (str): Ruta del archivo JSON que contiene las ideas.
        """
        self.file_path = file_path
        # Carga las ideas registradas en el archivo JSON.
        self.ideas: List[NotaConceptual] = self.cagar_ideas()
        
    def cargar_ideas(self) -> List[NotaConceptual]:
        """
        Carga las notas conceptuales del archivo JSON y las almacena en una lista.
        
        Returns:
            List[NotaConceptual]: Lista de ideas cargadas, o lista vacía en caso de error.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try:
                    data = json.load(file)
                    ideas = []
                    # Recorre cada registro del JSON y crea una instancia de NotaConceptual.
                    for i in data:
                        idea = NotaConceptual(
                            id = i['id'],
                            descripcion = i['descripcion'],
                            fecha = i['fecha']
                        )
                        ideas.append(idea)
                    return ideas
                except json.JSONDecodeError as e:
                    logging.error("Error al decodificar JSON: %s", e)
        return []
    
    def guardar_ideas(self) -> None:
        """
        Guarda las ideas en el archivo JSON.
        Se sobreescribe el archivo con la lista actualizada de ideas.
        """
        data = [{
            'id': idea.id,
            'descripcion': idea.descripcion,
            'fecha': idea.fecha
        } for idea in self.ideas]
        
        try:
            with open(self.file_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            logging.error("Error al guardar ideas en JSON: %s", e)
    
    def registrar_ideas(self, descripcion: str, fecha: str) -> bool:
        """
        UC12: Registrar Ideas de Anuncios.
        
        Registra una nueva idea para un anuncio, verificando que no exista ya una idea
        con la misma descripción. Si la operación es exitosa, guarda el archivo JSON y
        registra la acción en el log.
        
        Args:
            descripcion (str): Texto descriptivo de la idea o nota conceptual.
            fecha (str): Fecha de registro en formato "YYYY-MM-DD".
        
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado.
        """
        # Verifica que no exista una idea con la misma descripción.
        if any(i.descripcion == descripcion for i in self.ideas):
            logging.error("Error: Ya existe una idea con la misma descripción.")
            return False
        
        # Genera un nuevo id incrementando el máximo de los existentes.
        nueva_id = max((i.id for i in self.ideas), default = 0) + 1
        
        # Crea una nueva instancia de NotaConceptual y registra la idea.
        nueva_idea = NotaConceptual()
        nueva_idea.registrar_nota(descripcion, fecha)
        nueva_idea.id = nueva_id
        
        # Agrega la nueva idea a la lista y guarda los cambios en el archivo JSON.
        self.ideas.append(nueva_idea)
        self.guardar_ideas()
        logging.info("Registro de auditoría: Se agrego una nueva idea con id %s.", nueva_idea.id)
        return True
    
    def consultar_ideas(self) -> List[dict]:
        """
        UC13: Consultar Ideas de Anuncios
        
        Permite visualizar las ideas y notas conceptuales registradas para los anuncios,
        facilitando la planificación y revisión de propuestas. Las ideas se muestran ordenadas
        por fecha.
        
        Returns:
            List[dict]: Lista de ideas con detalles del anuncio (id, descripción y fecha) 
                        ordenadas por fecha. Retorna una lista vacía si no hay ideas.
        """
        # Verifica si existen ideas registradas.
        if not self.ideas:
            logging.info("No hay ideas registradas.")
            return []
        
        # Ordena las ideas por fecha; si no tienen fecha, se ubican al inicio utilizando date.min.
        ideas_ordenadas = sorted(self.ideas, key=lambda idea: idea.fecha if idea.fecha is not None else date.min)
        
        # Construye la lista de diccionarios con la información relevante de cada idea.
        ideas_list = [{
            'id': idea.id,
            'descripcion': idea.descripcion,
            'fecha': idea.fecha if idea.fecha is not None else ""
        } for idea in ideas_ordenadas]
        
        return ideas_list