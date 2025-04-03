from src.model.Empleado import Empleado
from src.model.CategoriaLaboral import CategoriaLaboral
import json

class PersonalContable(Empleado):
    def alta_trabajador(self, e: Empleado) -> None:
        # Lógica para dar de alta a un trabajador
        pass

    def crear_categoria_laboral(self, c: CategoriaLaboral) -> None:
        # Lógica para crear categoría laboral
        pass

    def modificar_sueldo(self, c: CategoriaLaboral, nuevo_sueldo: float) -> None:
        c.modificar_sueldo(nuevo_sueldo)

    def modificar_datos_trabajador(self, e: Empleado) -> None:
        # Lógica para modificar datos de trabajador
        pass

    def calcular_nominas(self) -> None:
        # Lógica para calcular nóminas
        pass

    def imprimir_factura(self) -> None:
        # Lógica para imprimir factura
        pass

    def to_json(self) -> str:
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'PersonalContable':
        empleado = Empleado.from_json(data)
        return cls(empleado.id, empleado.nombre, empleado.email, empleado.rol, empleado.usuario, empleado.categoria)