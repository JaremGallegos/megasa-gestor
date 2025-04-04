from __future__ import annotations
from src.model.CategoriaLaboral import CategoriaLaboral
from src.util.categoria_config import cargar_config, set_sueldo_base, get_sueldo_base
import logging

logging.basicConfig(
    filename = './logging/auditoria_categoria.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class CategoriaLaboralController:
    def listar_categorias(self) -> dict:
        """
        UC15: Retorna la configuración actual de las categorías laborales.
        
        Returns:
            dict: Diccionario con la configuración de sueldos.
        """
        return cargar_config()
    
    def actualizar_categoria(self, categoria: CategoriaLaboral, nuevo_sueldo: float) -> bool:
        """
        UC15: Actualiza el sueldo base de la categoría y guarda la configuración.
        
        Args:
            categoria (CategoriaLaboral): Categoría a actualizar.
            nuevo_sueldo (float): Nuevo sueldo base.
        
        Returns:
            bool: True si la actualización fue exitosa.
        """
        try:
            set_sueldo_base(categoria, nuevo_sueldo)
            return True
        except Exception as e:
            logging.error("Error al actualizar la categoria %s.", e)
            return False