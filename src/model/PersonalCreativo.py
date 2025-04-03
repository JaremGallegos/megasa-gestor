from src.model.Empleado import Empleado
from src.model.NotaConceptual import NotaConceptual
import json

class PersonalCreativo(Empleado):
    def registrar_nota_conceptual(self, n: NotaConceptual) -> None:
        # Lógica para registrar nota conceptual
        pass

    def consultar_notas(self) -> list:
        # Lógica para consultar notas
        pass

    def to_json(self) -> str:
        return super().to_json()

    @classmethod
    def from_json(cls, data: str) -> 'PersonalCreativo':
        empleado = Empleado.from_json(data)
        return cls(empleado.id, empleado.nombre, empleado.email, empleado.rol, empleado.usuario, empleado.categoria)