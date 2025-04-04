from src.model.Empleado import Empleado
from src.model.CategoriaLaboral import CategoriaLaboral
from typing import List
import logging

logging.basicConfig(
    filename = './logging/auditoria_empleados.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class NominaController:
    def __init__(self, empleados: List[Empleado]) -> None:
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
        nominas = []
        for emp in self.empleados:
            try:
                sueldo_base = emp.usuario.rol.sueldo_base
                nomina = {
                    "id": emp.id,
                    "nombre": emp.nombre,
                    "categoria": emp.usuario.rol.nombre,
                    "sueldo_base": sueldo_base,
                    "nomina_final": sueldo_base
                }
                nominas.append(nomina)
            except Exception as e:
                logging.error("Error al calcular nómina empleado %s:", e)
        return nominas