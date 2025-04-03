from src.model.Empleado import Empleado
import json

class PersonalContacto(Empleado):
    def registrar_finalizacion_anuncio(self) -> None:
        pass

    def comunicar_detalles_campana(self) -> None:
        pass

    def to_json(self) -> str:
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'PersonalContacto':
        empleado = Empleado.from_json(data)
        return cls(empleado.id, empleado.nombre, empleado.email, empleado.rol, empleado.usuario, empleado.categoria)