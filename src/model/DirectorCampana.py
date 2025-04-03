from src.model.Empleado import Empleado
import json

class DirectorCampana(Empleado):
    def registrar_campana(self) -> None:
        # Lógica para registrar campaña
        pass

    def asignar_empleados(self) -> None:
        # Lógica para asignar empleados a campaña
        pass

    def registrar_finalizacion_campana(self) -> None:
        # Lógica para finalizar campaña
        pass

    def registrar_finalizacion_anuncio(self) -> None:
        # Lógica para finalizar anuncio
        pass

    def imprimir_factura(self) -> None:
        # Lógica para imprimir factura
        pass

    def to_json(self) -> str:
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'DirectorCampana':
        empleado = Empleado.from_json(data)
        return cls(empleado.id, empleado.nombre, empleado.email, empleado.rol, empleado.usuario, empleado.categoria)