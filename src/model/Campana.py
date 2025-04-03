from __future__ import annotations
from typing import List, TYPE_CHECKING
from datetime import datetime, date
from src.model.Pago import Pago
from src.model.Anuncio import Anuncio
from src.model.Empleado import Empleado
import json

if TYPE_CHECKING:
    from src.model.Cliente import Cliente

def str_to_date(fecha_str: str) -> date:
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()
    
def date_to_str(fecha_date: date) -> str:
    return fecha_date.strftime("%Y-%m-%d")

class Campana:
    ultimo_id: int = 0
    def __init__(self, 
                 id: int = 0, 
                 titulo: str = "", 
                 fecha_inicio: str = "", 
                 fecha_fin_prevista: str = "",
                 costes_estimados: float = 0.0, 
                 presupuesto: float = 0.0, 
                 costes_reales: float = 0.0,
                 estado: str = "En ejecución", 
                 fecha_finalizacion: str = None, 
                 pagos: List[Pago] = None, 
                 anuncios: List[Anuncio] = None, 
                 empleados: List[Empleado] = None,
                 cliente: Cliente = None) -> None:
        self._id = id
        self._titulo = titulo
        self._fecha_inicio = str_to_date(fecha_inicio) if isinstance(fecha_inicio, str) else fecha_inicio
        self._fecha_fin_prevista = str_to_date(fecha_fin_prevista) if isinstance(fecha_fin_prevista, str) else fecha_fin_prevista
        self._costes_estimados = costes_estimados
        self._presupuesto = presupuesto
        self._costes_reales = costes_reales
        self._estado = estado
        self._fecha_finalizacion = str_to_date(fecha_finalizacion) if fecha_finalizacion else None
        self._pagos = pagos if pagos is not None else []
        self._anuncios = anuncios if anuncios is not None else []
        self._empleados = empleados if empleados is not None else []
        self._cliente = cliente
        
    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        self._id = id

    @property
    def titulo(self) -> str:
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str) -> None:
        self._titulo = titulo

    @property
    def fecha_inicio(self) -> str:
        return self._fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str) -> None:
        self._fecha_inicio = str_to_date(fecha_inicio)

    @property
    def fecha_fin_prevista(self) -> str:
        return self._fecha_fin_prevista
    
    @fecha_fin_prevista.setter
    def fecha_fin_prevista(self, fecha_fin_prevista: str) -> None:
        self._fecha_fin_prevista = str_to_date(fecha_fin_prevista)

    @property
    def costes_estimados(self) -> float:
        return self._costes_estimados
    
    @costes_estimados.setter
    def costes_estimados(self, costes_estimados: float) -> None:
        self._costes_estimados = costes_estimados

    @property
    def presupuesto(self) -> float:
        return self._presupuesto
    
    @presupuesto.setter
    def presupuesto(self, presupuesto: float) -> None:
        self._presupuesto = presupuesto

    @property
    def costes_reales(self) -> float:
        return self._costes_reales
    
    @costes_reales.setter
    def costes_reales(self, costes_reales: float) -> None:
        self._costes_reales = costes_reales

    @property
    def estado(self) -> str:
        return self._estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        self._estado = estado

    @property
    def fecha_finalizacion(self) -> str:
        return self._fecha_finalizacion
    
    @fecha_finalizacion.setter
    def fecha_finalizacion(self, fecha_finalizacion: str) -> None:
        self._fecha_finalizacion = str_to_date(fecha_finalizacion)

    @property
    def pagos(self) -> List[Pago]:
        return self._pagos
    
    @pagos.setter
    def pagos(self, pagos: List[Pago]) -> None:
        self._pagos = pagos

    @property
    def anuncios(self) -> List[Anuncio]:
        return self._anuncios
    
    @anuncios.setter
    def anuncios(self, anuncios: List[Anuncio]) -> None:
        self._anuncios = anuncios

    @property
    def empleados(self) -> List[Empleado]:
        return self._empleados
    
    @empleados.setter
    def empleados(self, empleados: List[Empleado]) -> None:
        self._empleados = empleados

    @property
    def cliente(self) -> Cliente:
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente) -> None:
        self._cliente = cliente
    
    def registrar_campana(self, titulo: str, fecha_inicio: str, fecha_fin_prevista: str, costes_estimados: float, presupuesto: float) -> None:
        """
        Registra la campaña validando que los campos obligatorios estén completos y
        establece el estado inicial de la campaña.
        """
        Campana.ultimo_id += 1
        self.id = Campana.ultimo_id
        self.titulo = titulo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_prevista = fecha_fin_prevista
        self.costes_estimados = costes_estimados
        self.presupuesto = presupuesto        
        self.estado = "En ejecución"

        print(f"Campaña '{self._titulo}' registrada correctamente con estado '{self._estado}'.")

    def registrar_finalizacion(self) -> None:
        """
        Finaliza la campaña verificando que se encuentre en ejecución y actualiza el estado
        a 'Finalizada', registrando la fecha de finalización.
        """
        if self._estado != "En ejecución":
            raise ValueError("Solo se puede finalizar una campaña en ejecución.")
        
        self._fecha_finalizacion = datetime.now().isoformat()
        self._estado = "Finalizada"
        print(f"Campaña '{self._titulo}' finalizada correctamente el {self._fecha_finalizacion}.")

    def agregar_pago(self, p: Pago) -> None:
        self._pagos.append(p)

    def asignar_empleado(self, e: Empleado) -> None:
        if e not in self._empleados:
            self._empleados.append(e)

    def imprimir_resumen_gastos(self) -> None:
        """
        Genera e imprime un resumen de los gastos de la campaña, comparando el presupuesto
        con los costes reales acumulados.
        """
        resumen = f"Resumen de gastos para la campaña '{self._titulo}':\n"
        resumen += f"Presupuesto: {self._presupuesto}\n"
        resumen += f"Costes reales acumulados: {self._costes_reales}\n"
        diferencia = self._presupuesto - self._costes_reales
        resumen += f"Diferencia (Presupuesto - Costes reales): {diferencia}\n"
        print(resumen)

    def imprimir_factura(self) -> None:
        """
        Genera e imprime una factura de la campaña utilizando el detalle de los pagos realizados.
        Se calcula el total pagado y se compara con el presupuesto para mostrar la diferencia.
        """
        total_pagado = sum([p.get_monto() for p in self._pagos])
        factura = f"Factura de la campaña '{self._titulo}':\n"
        factura += f"Presupuesto: {self._presupuesto}\n"
        factura += f"Costes reales: {self._costes_reales}\n"
        factura += f"Total pagado: {total_pagado}\n"
        diferencia = self._presupuesto - total_pagado
        factura += f"Diferencia a pagar: {diferencia}\n"
        print(factura)

    def registrar_gasto(self, gasto: float) -> None:
        self._costes_reales += gasto
    
    def to_json(self) -> str:
        return json.dumps({
            'id': self.id,
            'titulo': self.titulo,
            'fecha_inicio': date_to_str(self.fecha_inicio),
            'fecha_fin_prevista': date_to_str(self.fecha_fin_prevista),
            'costes_estimados': self.costes_estimados,
            'presupuesto': self.presupuesto,
            'costes_reales': self.costes_reales,
            'estado': self.estado,
            'fecha_finalizacion': date_to_str(self.fecha_finalizacion) if self.fecha_finalizacion else None,
            'pagos': [p.to_json() for p in self.pagos],
            'anuncios': [a.to_json() for a in self.anuncios],
            'empleados': [e.id for e in self.empleados],
            'cliente': self.cliente.id if self.cliente else None
        })

    @classmethod
    def from_json(cls, data: str) -> 'Campana':
        data_dict = json.loads(data)
        return cls(
            id=data_dict['id'],
            titulo=data_dict['titulo'],
            fecha_inicio=data_dict['fecha_inicio'],
            fecha_fin_prevista=data_dict['fecha_fin_prevista'],
            costes_estimados=data_dict['costes_estimados'],
            presupuesto=data_dict['presupuesto'],
            costes_reales=data_dict['costes_reales'],
            estado=data_dict['estado'],
            fecha_finalizacion=data_dict['fecha_finalizacion']
        )