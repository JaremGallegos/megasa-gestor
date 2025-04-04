from __future__ import annotations
# Se importan las clases necesarias del modelo.
from src.model.Campana import Campana
from src.model.Pago import Pago
from src.model.Empleado import Empleado
from typing import List
import json, os, logging

# Configuración de logging para auditoría de campaña.
# Se define el archivo de log, nivel de detalle y formato.
logging.basicConfig(
    filename = './logging/auditoria_campaña.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class CampañaController:
    def __init__(self, file_path: str = './data/campana.json') -> None:
        """
        Inicializa el controlador cargando las campañas desde el archivo JSON.
        
        Args:
            file_path (str): Ruta del archivo donde se almacenan las campañas.
        """
        # Ruta del archivo de persistencia de campañas.
        self.file_path = file_path
        # Lista de campañas cargadas al inicializar la clase.
        self.campañas: List[Campana] = self.cargar_campaña()
        
    def cargar_campaña(self) -> List[Campana]:
        """
        Cargar campañas del archivo JSON y los almacena en una lista.

        Returns:
            List[Campana]: Lista de campañas cargadas, o vacía si hay error.
        """
        # Verifica si el archivo existe.
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding = 'utf-8') as file:
                try: 
                    # Carga los datos JSON.
                    data = json.load(file)
                    campañas = []
                    # Itera sobre cada registro para crear instancias de Campana.
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
                    # Registra un error si ocurre un problema al decodificar el JSON.
                    logging.error("Error al decodificar JSON: %s", e)
                    return []
        # Retorna una lista vacía si el archivo no existe.
        return []
    
    def guardar_campañas(self) -> None:
        """
        Guarda la lista de campañas en el archivo JSON correspondiente.
        """
        # Convierte cada objeto Campana a un diccionario JSON.
        data = [json.loads(campaña.to_json()) for campaña in self.campañas]
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            # Registra un error si ocurre un problema al guardar el archivo.
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
        # Verifica que no exista una campaña con el mismo título.
        if any(c.titulo == titulo for c in self.campañas):
            logging.error("Error: Ya existe una campaña con el mismo título.")
            return False
        
        # Genera un nuevo id incrementando el máximo existente.
        nueva_id = max((c.id for c in self.campañas), default = 0) + 1
        
        # Crea una nueva campaña y la registra con los datos ingresados.
        nueva_campaña = Campana()
        nueva_campaña.registrar_campana(titulo, fecha_inicio, fecha_fin_prevista, costes_estimados, presupuesto)
        nueva_campaña.id = nueva_id
        
        # Agrega la campaña a la lista y la persiste en el archivo JSON.
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
        # Busca la campaña por id.
        for campaña in self.campañas:
            if campaña.id == id:
                try:
                    # Registra la finalización de la campaña.
                    campaña.registrar_finalizacion()
                    self.guardar_campañas()
                    logging.info("Registro de auditoría: Se finalizó la campaña con id %s.", id)
                    return True
                except Exception as e:
                    logging.error("Error al finalizar la campaña con id %s: %s", id, e)
                    return False
        # Registra error si no se encuentra la campaña.
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
        # Busca la campaña en la lista por su id.
        for campaña in self.campañas:
            if campaña.id == id:
                try:
                    # Agrega el pago a la campaña.
                    campaña.agregar_pago(pago)
                    self.guardar_campañas()
                    logging.info("Registro de auditoría: Se registró un pago en la campaña con id %s.", id)
                    return True
                except Exception as e:
                    logging.error("Error al registrar pago en la campaña con id %s: %s", id, e)
                    return False
        # Error en caso de que no se encuentre la campaña.
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
        # Itera sobre las campañas para encontrar la correspondiente.
        for campaña in self.campañas:
            if campaña.id == id:
                # Retorna los pagos si existen.
                if campaña.pagos:
                    return campaña.pagos
                else:
                    logging.info("No hay pagos registrados para la campaña con id %s.", id)
                    return []
        # Error si la campaña no se encuentra.        
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
        # Busca la campaña correspondiente.
        for campaña in self.campañas:
            if campaña.id == id:
                # Verifica que la campaña esté en ejecución.
                if campaña.estado != "En ejecución":
                    logging.error("La campaña con id %s no está en ejecución.", id)
                    return False
                # Verifica que el empleado no esté ya asignado.
                if empleado in campaña.empleados:
                    logging.warning("El empleado con id %s ya está asignado a la campaña.", empleado.id)
                    return False
                # Asigna el empleado y guarda los cambios.
                campaña.asignar_empleado(empleado)
                self.guardar_campañas()
                logging.info("Empleado con id %s asignado a la campaña con id %s.", empleado.id, id)
                return True
        # Registra error si la campaña no se encuentra.
        logging.error("Campaña con id %s no encontrada.", id)
        return False
    
    def registrar_contacto_campaña(self, id: int, empleado: Empleado) -> bool:
        """
        UC7: Registrar Empleado de Contacto para Campaña
        
        Permite designar a un empleado asignado a la campaña como contacto 
        principal
        
        Args:
            id (int): Identificador de la campaña.
            empleado (Empleado): Empleado a designar como contacto.
        
        Returns:
            bool: True si se designa correctamente, False en caso de error.
        """
        # Busca la campaña por id.
        for campaña in self.campañas:
            if campaña.id == id:
                # Verifica que la campaña esté en ejecución.
                if campaña.estado != "En ejecución":
                    logging.error("La campaña con id %s no está en ejecución.", id)
                    return False
                # Verifica que el empleado esté asignado a la campaña.
                if empleado not in campaña.empleados:
                    logging.error("El empleado con id %s no está asignado a la campaña.", empleado.id)
                    return False
                # Asigna al empleado como contacto.
                campaña.contacto = empleado
                self.guardar_campañas()
                logging.info("Empleado con id %s designado como contacto para la campaña con id %s.", empleado.id, id)
                return True
        # Error si no se encuentra la campaña.
        logging.error("Campaña con id %s no encontrada.", id)
        return False
    
    def registrar_gastos_campana(self, id: int, monto: float, descripcion: str, fecha: str) -> bool:
        """
        UC10: Registrar Gastos de Campaña
        
        Permite ingresar y actualizar los gastos reales incurridos durante la 
        ejecución de una campaña.
        
        Args:
            id (int): Identificador de la campaña.
            monto (float): Monto del gasto.
            descripcion (str): Descripción del gasto.
            fecha (str): Fecha del gasto (formato "YYYY-MM-DD").
            
        Returns:
            bool: True si se registra el gasto correctamente, False en caso de error.
        """
        # Busca la campaña correspondiente.
        for campaña in self.campañas:
            if campaña.id == id:
                # La campaña debe estar en ejecución para poder registrar gastos.
                if campaña.estado != "En ejecución":
                    logging.error("La campaña con id %s no está en ejecución.", id)
                    return False
                
                # Guarda el valor actual de costes reales en caso de error.
                prev = campaña.costes_reales
                try:
                    # Registra el gasto, actualizando los costes reales.
                    campaña.registrar_gasto(monto)
                    self.guardar_campañas()
                    logging.info("Gasto registrado en campaña id %s: monto=%.2f, descripción='%s', fecha=%s", id, monto, descripcion, fecha)
                    return True
                except Exception as e:
                    # En caso de error, revierte el valor de costes reales.
                    campaña.costes_reales = prev
                    logging.error("Error al registrar gasto en campaña id %s: %s", id, e)
                    return False
        # Registra error si no se encuentra la campaña.
        logging.error("Campaña con id %s no encontrada para registrar gasto.", id)
        return False
    
    def consultar_gastos_campana(self, id: int) -> str:
        """
        UC11: Consultar Gastos de Campaña
        
        Retorna un resumen de los gastos incurridos en una campaña.
        
        Args:
            id (int): Identificador de la campaña.
            
        Returns:
            str: Resumen de gastos o mensaje informativo si no se encuentra la campaña.
        """
        # Itera sobre las campañas para encontrar la indicada.
        for campaña in self.campañas:
            if campaña.id == id:
                # Crea un resumen de la campaña con los gastos.
                resumen = f"Resumen de gastos para la campaña '{campaña.titulo}':\n"
                resumen += f"Presupuesto: {campaña.presupuesto}\n"
                resumen += f"Costes reales acumulados: {campaña.costes_reales}\n"
                diferencia = campaña.presupuesto - campaña.costes_reales
                resumen += f"Diferencia (Presupuesto - Costes reales): {diferencia}\n"
                return resumen
        # Retorna mensaje en caso de no encontrar la campaña.
        return f"Campaña con id {id} no encontrada."