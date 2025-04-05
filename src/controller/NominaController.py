from __future__ import annotations
# Se importan las clases necesarias del modelo.
from src.model.Empleado import Empleado
from src.model.CategoriaLaboral import CategoriaLaboral
from typing import List
import logging

# Configuración de logging para auditoría de empleados (nómina en este caso).
logging.basicConfig(
    filename = './logging/auditoria_empleados.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class NominaController:
    def __init__(self, empleados: List[Empleado]) -> None:
        """
        Inicializa el controlador de nómina con la lista de empleados.
        
        Args:
            empleados (List[Empleado]): Lista de empleados para calcular la nómina.
        """
        self.empleados = empleados
        
    def calcular_nomina(self) -> List[dict]:
        """
        UC16: Calcula la nómina de cada empleado basándose en su categoría laboral y sueldo base.
        
        Para cada empleado, se obtiene el sueldo base definido en la categoría (almacenado en el Enum)
        a través del atributo 'rol' del usuario asignado.
        
        Si faltan datos críticos para un empleado, se omite o se marca para revisión.
        
        Returns:
            List[dict]: Lista de nóminas con detalles del empleado, categoría y sueldo.
        """
        # Lista para almacenar la nómina de cada empleado.
        nominas = []
        # Itera sobre cada empleado de la lista.
        for emp in self.empleados:
            try:
                # Se obtiene el sueldo base a partir del rol asociado al usuario del empleado.
                sueldo_base = emp.usuario.rol.sueldo_base
                # Se construye el diccionario con la información relevante de la nómina.
                nomina = {
                    "id": emp.id,
                    "nombre": emp.nombre,
                    "categoria": emp.usuario.rol.nombre,
                    "sueldo_base": sueldo_base,
                    "nomina_final": sueldo_base # Aquí se puede extender para incluir otros cálculos.
                }
                nominas.append(nomina)
            except Exception as e:
                # Se registra un error en caso de que falten datos críticos o surja alguna excepción.
                logging.error("Error al calcular nómina empleado %s:", e)
        return nominas