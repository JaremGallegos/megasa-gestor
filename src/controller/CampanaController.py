from __future__ import annotations
from src.model.Campana import Campana
from src.model.Pago import Pago
from src.model.Empleado import Empleado
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
        data = [json.loads(campaña.to_json()) for campaña in self.campañas]
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
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
            titulo (str): Título de la campaña.
            fecha_inicio (str): Fecha de inicio (formato "YYYY-MM-DD").
            fecha_fin_prevista (str): Fecha fin prevista (formato "YYYY-MM-DD").
            costes_estimados (float): Costes estimados de la campaña.
            presupuesto (float): Presupuesto asignado.
        
        Returns:
            bool: True si se registró exitosamente, False en caso de duplicado. 
        """
        if any(c.titulo == titulo for c in self.campañas):
            logging.error("Error: Ya existe una campaña con el mismo título")
            return False
        
        nueva_id = max((c.id for c in self.campañas), default = 0) + 1
        
        nueva_campaña = Campana()
        nueva_campaña.registrar_campana(titulo, fecha_inicio, fecha_fin_prevista, costes_estimados, presupuesto)
        nueva_campaña.id = nueva_id
        self.campañas.append(nueva_campaña)
        self.guardar_campañas()
        logging.info("Registro de auditoría: Se agrego una nueva campaña con id %s.", nueva_campaña.id)
        return True
    
    def registrar_finalizacion_campaña(self, id: int) -> bool:
        """
        UC3: Registrar Finalización de Campaña Publicitaria
        Finaliza la campaña verificando que se encuentre en ejecución y actualiza el estado
        a 'Finalizada', registrando la fecha de finalización.
        
        Args:
            id (int): Identificador de la campaña a finalizar.
        
        Returns:
            bool: True si la campaña se finalizó correctamente, False en caso de error o duplicidad.
        """
        for campaña in self.campañas:
            if campaña.id == id:
                try:
                    campaña.registrar_finalizacion()
                    self.guardar_campañas()
                    logging.info("Registro de auditoría: Se finalizó la campaña con id %s.", id)
                    return True
                except Exception as e:
                    logging.error("Error al finalizar la campaña con id %s: %s", id, e)
                    return False
                
        logging.error("Campaña con id %s no encontrada para finalización.", id)
        return False
        
    def registrar_pago_campaña(self, id: int, pago: Pago) -> bool:
        """
        UC4: Registrar Pago de Campaña
        Registra un pago parcial en la campaña especificada. Se valida la existencia de la campaña
        y se asocia el pago a ella, actualizando la persistencia y registrando la operación para auditoría.

        Args:
            id (int): Identificador de la campaña.
            pago (Pago): Objeto Pago con los datos del pago a registrar.
        
        Returns:
            bool: True si el pago se registró correctamente, False en caso de error.
        """
        for campaña in self.campañas:
            if campaña.id == id:
                try:
                    campaña.agregar_pago(pago)
                    self.guardar_campañas()
                    logging.info("Registro de auditoría: Se registró un pago en la campaña con id %s.", id)
                    return True
                except Exception as e:
                    logging.error("Error al registrar pago en la campaña con id %s: %s", id, e)
                    return False
        
        logging.error("Campaña con id %s no encontrada para registrar pago.", id)
        return False
    
    def consultar_pagos_campaña(self, id: int) -> list:
        """
        UC5: Consultar Pagos de Campaña
        Recupera y retorna la lista de pagos asociados a la campaña especificada.
        
        Args:
            id (int): Identificador de la campaña.
        
        Returns:
            list: Lista de objetos Pago asociados a la campaña. Si no hay pagos, 
            se retorna una lista vacía.
        """
        for campaña in self.campañas:
            if campaña.id == id:
                if campaña.pagos:
                    return campaña.pagos
                else:
                    logging.info("No hay pagos registrados para la campaña con id %s.", id)
                    return []
                
        logging.error("Campaña con id %s no encontrada para consultar pagos.", id)
        return []
    
    def asignar_empleados_campaña(self, id: int, empleado: Empleado) -> bool:
        """
        UC6: Asignar Empleados a Campaña
        Permite asignar a la campaña (que debe estar en ejecución) un empleado, 
        validando que no se asigne uno ya presente.
        
        Args:
            id (int): Identificador de la campaña.
            empleado (Empleado): Empleado a asignar.
            
        Returns:
            bool: True si se asigna correctamente, False en caso de error o duplicado.
        """
        for campaña in self.campañas:
            if campaña.id == id:
                if campaña.estado != "En ejecución":
                    logging.error("La campaña con id %s no está en ejecución.", id)
                    return False
                if empleado in campaña.empleados:
                    logging.warning("El empleado con id %s ya está asignado a la campaña.", empleado.id)
                    return False
                campaña.asignar_empleado(empleado)
                self.guardar_campañas()
                logging.info("Empleado con id %s asignado a la campaña con id %s.", empleado.id, id)
                return True
            
        logging.error("Campaña con id %s no encontrada.", id)
        return False
    
    def registrar_contacto_campaña(self, id: int, empleado: Empleado) -> bool:
        """
        UC7: Registrar Empleado de Contacto para Campaña
        Permite designar a un empleado asignado a la campaña como contacto principal
        
        Args:
            id (int): Identificador de la campaña.
            empleado (Empleado): Empleado a designar como contacto.
        
        Returns:
            bool: True si se designa correctamente, False en caso de error.
        """
        for campaña in self.campañas:
            if campaña.id == id:
                if campaña.estado != "En ejecución":
                    logging.error("La campaña con id %s no está en ejecución.", id)
                    return False
                if empleado not in campaña.empleados:
                    logging.error("El empleado con id %s no está asignado a la campaña.", empleado.id)
                    return False
                campaña.contacto = empleado
                self.guardar_campañas()
                logging.info("Empleado con id %s designado como contacto para la campaña con id %s.", empleado.id, id)
                return True
        
        logging.error("Campaña con id %s no encontrada.", id)
        return False