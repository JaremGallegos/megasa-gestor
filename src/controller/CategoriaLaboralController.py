from __future__ import annotations
from src.model.CategoriaLaboral import CategoriaLaboral
from typing import List
import json, os, logging

logging.basicConfig(
    filename = './logging/auditoria_categoria.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class CategoriaLaboralController:
    def __init__(self, file_path: str = './data/categoria.json') -> None:
        self.file_path = file_path
        self.categorias: List[CategoriaLaboral] = self.cargar_categorias()
        
    def cargar_categorias(self) -> List[CategoriaLaboral]:
        """
        Cargar categorias laborales del archivo JSON y los almacena en una lista
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                pass