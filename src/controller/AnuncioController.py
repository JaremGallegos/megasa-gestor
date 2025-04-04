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
        
    def registrar_anuncio(self, descripcion: str, estado: str) -> bool:
        """
        UC8: Registrar Anuncio de Campaña
        
        """