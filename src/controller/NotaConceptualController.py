from __future__ import annotations
from src.model.NotaConceptual import NotaConceptual
from typing import List
import logging, json, os

logging.basicConfig(
    filename = './logging/auditoria_ideas.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s- %(message)s'
)

class NotaConceptualController:
    def __init__(self, file_path: str = './data/ideas.json') -> None:
        self.file_path = file_path
        self.ideas: List[NotaConceptual] = self.cagar_ideas()
        
    def cargar_ideas(self) -> List[NotaConceptual]:
        """
        Cargar notas conceptuales del archivo JSON y los almacena en una lista
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try:
                    data = json.load(file)
                    ideas = []
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
        Guardar las ideas en el archvio JSON.
        Se sobreescribe el archivo con la lista actualizada
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
        UC12: Registrar Ideas de Anuncios
        """
        if any(i.descripcion == descripcion for i in self.ideas):
            logging.error("Error: Ya existe una idea con la misma descripción.")
            return False
        
        nueva_id = max((i.id for i in self.ideas), default = 0) + 1
        
        nueva_idea = NotaConceptual()
        nueva_idea.registrar_nota(descripcion, fecha)
        nueva_idea.id = nueva_id
        self.ideas.append(nueva_idea)
        self.guardar_ideas()
        logging.info("Registro de auditoría: Se agrego una nueva idea con id %s.", nueva_idea.id)
        return True
    
    def consultar_ideas(self) -> bool:
        """
        UC13: Consultar Ideas de Anuncios
        """
        pass