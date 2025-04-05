from __future__ import annotations
# Se importa la clase CategoriaLaboral del modelo.
from src.model.CategoriaLaboral import CategoriaLaboral
# Se importan funciones utilitarias para cargar la configuración y actualizar el sueldo base.
from src.util.categoria_config import cargar_config, set_sueldo_base
import logging

# Configuración de logging para auditoría de categorías laborales.
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
        # Retorna la configuración actual cargada desde el archivo o recurso configurado.
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
            # Actualiza el sueldo base utilizando la función utilitaria.
            set_sueldo_base(categoria, nuevo_sueldo)
            return True
        except Exception as e:
            # En caso de error, se registra el error en el log.
            logging.error("Error al actualizar la categoria %s.", e)
            return False