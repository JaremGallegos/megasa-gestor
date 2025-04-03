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
        self.campañas: List[Campana] = self.cargar_campaña()
        
    def cargar_campaña(self) -> List[Campana]:
        """
        Cargar campañas del archivo JSON y los almacena en una lista
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try: 
                    data = json.load(file)
                    campañas = []
                    for c in data:
                        campaña = Campana(
                            id = c["id"],
                            titulo = c['titulo'],
                            fecha_inicio = c['fecha_inicio'],
                            fecha_fin_prevista = c['fecha_fin_prevista'],
                            costes_estimados = c['costes_estimados'],
                            presupuesto = c["presupuesto"],
                            costes_reales = c["costes_reales"],
                            estado = c["estado"],
                            fecha_finalizacion = c["fecha_finalizacion"]
                        )
                        campañas.append(campaña)
                    return campañas
                except json.JSONDecodeError as e:
                    logging.error("Error al decodificar JSON: %s", e)
                    return []
        return []
    
    def guardar_campañas(self) -> None:
        """
        Guardar las campañas en el archivo JSON.
        Se sobreescribe el archivo con la lista actualizada.
        """
        data = [{
            'id': campaña.id,
            'titulo': campaña.titulo,
            'fecha_inicio': campaña.fecha_inicio,
            'fecha_fin_prevista': campaña.fecha_fin_prevista,
            'costes_estimados': campaña.costes_estimados,
            'presupuesto': campaña.presupuesto,
            'costes_reales': campaña.costes_reales,
            'estado': campaña.estado,
            'fecha_finalizacion': campaña.fecha_finalizacion
        } for campaña in self.campañas]
        
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent = 4)
        except Exception as e:
            logging.error("Error al guardar campañas en JSON: %s", e)
            
    def listar_campañas(self) -> List[Campana]:
        """
        Retorna la lista de campañas registradas.
        
        Returns:
            List[Campana]: Lista de Campañas.
        """
        return self.campañas
    
    def registrar_campaña(self, titulo: str, fecha_inicio: str, fecha_fin_prevista: str, costes_estimados: float, presupuesto: float) -> bool:
        """
        UC2: Registrar Campaña Publicitaria
        Antes de registrar, se verifica que no exista ya una campaña con la misma combinacion de titulo.
        Si la operación es exitosa, se guarda el archivo JSON y se registra la acción para auditoría.
        
        Args:
            titulo (str): Titulo de la Campaña
        
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado. 
        """
        if any(c.titulo == titulo for c in self.campañas):
            logging.error("Error: Ya existe una campaña con el mismo título")
            return False
        
        nueva_campaña = Campana()
        nueva_campaña.registrar_campana(titulo, fecha_inicio, fecha_fin_prevista, costes_estimados, presupuesto)
        self.campañas.append(nueva_campaña)
        self.guardar_campañas()
        logging.info("Registro de auditoría: Se agrego una nueva campaña con id %s.", nueva_campaña.id)
        return True