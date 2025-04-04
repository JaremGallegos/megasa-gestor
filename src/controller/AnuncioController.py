from __future__ import annotations
from src.model.Anuncio import Anuncio
from typing import List
import json, os, logging

logging.basicConfig(
    filename = './logging/auditoria_anuncio.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class AnuncioController:
    def __init__(self, file_path: str = '/data/anuncio.json') -> None:
        self.file_path = file_path
        self.anuncios: List[Anuncio] = self.cargar_anuncios()
        
    def cargar_anuncios(self) -> List[Anuncio]:
        """
        Cargar anuncios del archivo JSON y los almacena en una lista
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    data = json.load(file)
                    anuncios = []
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
        data = [json.loads(anuncio.to_json()) for anuncio in self.anuncios]
        try:
            with open(self.file_path, 'w', encoding = 'utf-8') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            logging.error("Error al guardar anuncios en JSON: %s", e)
        
    def registrar_anuncio(self, descripcion: str) -> bool:
        """
        UC8: Registrar Anuncio de Campaña
        
        """
        if any(a.descripcion == descripcion for a in self.anuncios):
            logging.error("Error: Ya existe un anuncio con la misma descripción.")
            return False
        
        nueva_id = max((a.id for a in self.anuncios), default = 0) + 1
        
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
        
        
        """
        for anuncio in self.anuncios:
            if anuncio.id == id:
                try:
                    anuncio.registrar_finalizacion()
                    self.guardar_anuncios()
                    logging.info("Registro de auditoría: Se finalizó el anuncio con id %s.", id)
                    return True
                except Exception as e:
                    logging.error("Error al finalizar el anuncio con id %s: %s", id, e)
                    return False
                
        logging.error("Anuncio con id %s no encontrado para finalización.", id)
        return False