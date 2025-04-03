from __future__ import annotations
from src.model.Campana import Campana
from typing import List
import json, os, logging

logging.basicConfig(
    filename = './logging/auditoria_campaña.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class CampañaController:
    def __init__(self, file_path: str = './data/campana.json') -> None:
        self.file_path = file_path
        self.campaña: List[Campana]