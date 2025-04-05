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
    """
    Convierte una cadena de fecha en formato "YYYY-MM-DD" a un objeto date.
    
    Args:
        fecha_str (str): Cadena que representa la fecha.
    
    Returns:
        date: Objeto de fecha.
    """
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()
    
def date_to_str(fecha_date: date) -> str:
    """
    Convierte un objeto date a una cadena en formato "YYYY-MM-DD".
    
    Args:
        fecha_date (date): Objeto de fecha.
    
    Returns:
        str: Cadena que representa la fecha.
    """
    return fecha_date.strftime("%Y-%m-%d")

class Campana:
    # Atributo de clase para llevar la cuenta del último ID asignado a una campaña.
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
                 cliente: Cliente = None,
                 contacto: Empleado = None) -> None:
        """
        Inicializa una nueva instancia de Campana con los datos proporcionados.
        
        Args:
            id (int, opcional): Identificador de la campaña.
            titulo (str, opcional): Título de la campaña.
            fecha_inicio (str, opcional): Fecha de inicio en formato "YYYY-MM-DD".
            fecha_fin_prevista (str, opcional): Fecha fin prevista en formato "YYYY-MM-DD".
            costes_estimados (float, opcional): Costes estimados para la campaña.
            presupuesto (float, opcional): Presupuesto asignado.
            costes_reales (float, opcional): Costes reales acumulados.
            estado (str, opcional): Estado de la campaña (por defecto "En ejecución").
            fecha_finalizacion (str, opcional): Fecha de finalización en formato "YYYY-MM-DD".
            pagos (List[Pago], opcional): Lista de pagos realizados.
            anuncios (List[Anuncio], opcional): Lista de anuncios asociados.
            empleados (List[Empleado], opcional): Lista de empleados asignados.
            cliente (Cliente, opcional): Cliente asociado a la campaña.
            contacto (Empleado, opcional): Empleado designado como contacto.
        """
        self._id = id
        self._titulo = titulo
        # Convierte las fechas de string a objeto date, si la cadena es válida.
        self._fecha_inicio = str_to_date(fecha_inicio) if isinstance(fecha_inicio, str) and fecha_inicio.strip() != "" else None
        self._fecha_fin_prevista = str_to_date(fecha_fin_prevista) if isinstance(fecha_fin_prevista, str) and fecha_fin_prevista.strip() != "" else None
        self._costes_estimados = costes_estimados
        self._presupuesto = presupuesto
        self._costes_reales = costes_reales
        self._estado = estado
        self._fecha_finalizacion = str_to_date(fecha_finalizacion) if fecha_finalizacion and fecha_finalizacion.strip() != "" else None
        # Inicializa las listas o utiliza las proporcionadas.
        self._pagos = pagos if pagos is not None else []
        self._anuncios = anuncios if anuncios is not None else []
        self._empleados = empleados if empleados is not None else []
        self._cliente = cliente if cliente is not None else []
        self._contacto = contacto if contacto is not None else []
        
    @property
    def id(self) -> int:
        """
        Obtiene el ID de la campaña.
        
        Returns:
            int: El identificador de la campaña.
        """
        return self._id
    
    @id.setter
    def id(self, id: int) -> None:
        """
        Establece el ID de la campaña.
        
        Args:
            id (int): Nuevo identificador.
        """
        self._id = id

    @property
    def titulo(self) -> str:
        """
        Obtiene el título de la campaña.
        
        Returns:
            str: El título de la campaña.
        """
        return self._titulo
    
    @titulo.setter
    def titulo(self, titulo: str) -> None:
        """
        Establece el título de la campaña.
        
        Args:
            titulo (str): Nuevo título.
        """
        self._titulo = titulo

    @property
    def fecha_inicio(self) -> str:
        """
        Obtiene la fecha de inicio de la campaña en formato string.
        
        Returns:
            str: Fecha de inicio en formato "YYYY-MM-DD", o None si no está definida.
        """
        return self._fecha_inicio if self._fecha_inicio else None
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio: str) -> None:
        """
        Establece la fecha de inicio de la campaña a partir de un string.
        
        Args:
            fecha_inicio (str): Fecha de inicio en formato "YYYY-MM-DD".
        """
        self._fecha_inicio = str_to_date(fecha_inicio) if fecha_inicio and fecha_inicio.strip() else None

    @property
    def fecha_fin_prevista(self) -> str:
        """
        Obtiene la fecha fin prevista de la campaña en formato string.
        
        Returns:
            str: Fecha fin prevista en formato "YYYY-MM-DD", o None si no está definida.
        """
        return self._fecha_fin_prevista if self._fecha_fin_prevista else None
    
    @fecha_fin_prevista.setter
    def fecha_fin_prevista(self, fecha_fin_prevista: str) -> None:
        """
        Establece la fecha fin prevista de la campaña a partir de un string.
        
        Args:
            fecha_fin_prevista (str): Fecha fin prevista en formato "YYYY-MM-DD".
        """
        self._fecha_fin_prevista = str_to_date(fecha_fin_prevista) if fecha_fin_prevista and fecha_fin_prevista.strip() else None

    @property
    def costes_estimados(self) -> float:
        """
        Obtiene los costes estimados de la campaña.
        
        Returns:
            float: Costes estimados.
        """
        return self._costes_estimados
    
    @costes_estimados.setter
    def costes_estimados(self, costes_estimados: float) -> None:
        """
        Establece los costes estimados de la campaña.
        
        Args:
            costes_estimados (float): Nuevos costes estimados.
        """
        self._costes_estimados = costes_estimados

    @property
    def presupuesto(self) -> float:
        """
        Obtiene el presupuesto asignado a la campaña.
        
        Returns:
            float: Presupuesto.
        """
        return self._presupuesto
    
    @presupuesto.setter
    def presupuesto(self, presupuesto: float) -> None:
        """
        Establece el presupuesto asignado a la campaña.
        
        Args:
            presupuesto (float): Nuevo presupuesto.
        """
        self._presupuesto = presupuesto

    @property
    def costes_reales(self) -> float:
        """
        Obtiene los costes reales acumulados de la campaña.
        
        Returns:
            float: Costes reales.
        """
        return self._costes_reales
    
    @costes_reales.setter
    def costes_reales(self, costes_reales: float) -> None:
        """
        Establece los costes reales acumulados de la campaña.
        
        Args:
            costes_reales (float): Nuevos costes reales.
        """
        self._costes_reales = costes_reales

    @property
    def estado(self) -> str:
        """
        Obtiene el estado actual de la campaña.
        
        Returns:
            str: Estado de la campaña.
        """
        return self._estado
    
    @estado.setter
    def estado(self, estado: str) -> None:
        """
        Establece el estado de la campaña.
        
        Args:
            estado (str): Nuevo estado.
        """
        self._estado = estado

    @property
    def fecha_finalizacion(self) -> str:
        """
        Obtiene la fecha de finalización de la campaña en formato string.
        
        Returns:
            str: Fecha de finalización en formato "YYYY-MM-DD", o None si no está definida.
        """
        return self._fecha_finalizacion if self._fecha_finalizacion else None
    
    @fecha_finalizacion.setter
    def fecha_finalizacion(self, fecha_finalizacion: str) -> None:
        """
        Establece la fecha de finalización de la campaña a partir de un string.
        
        Args:
            fecha_finalizacion (str): Fecha de finalización en formato "YYYY-MM-DD".
        """
        self._fecha_finalizacion = str_to_date(fecha_finalizacion) if fecha_finalizacion and fecha_finalizacion.strip() else None

    @property
    def pagos(self) -> List[Pago]:
        """
        Obtiene la lista de pagos asociados a la campaña.
        
        Returns:
            List[Pago]: Lista de pagos.
        """
        return self._pagos
    
    @pagos.setter
    def pagos(self, pagos: List[Pago]) -> None:
        """
        Establece la lista de pagos asociados a la campaña.
        
        Args:
            pagos (List[Pago]): Nueva lista de pagos.
        """
        self._pagos = pagos

    @property
    def anuncios(self) -> List[Anuncio]:
        """
        Obtiene la lista de anuncios asociados a la campaña.
        
        Returns:
            List[Anuncio]: Lista de anuncios.
        """
        return self._anuncios
    
    @anuncios.setter
    def anuncios(self, anuncios: List[Anuncio]) -> None:
        """
        Establece la lista de anuncios asociados a la campaña.
        
        Args:
            anuncios (List[Anuncio]): Nueva lista de anuncios.
        """
        self._anuncios = anuncios

    @property
    def empleados(self) -> List[Empleado]:
        """
        Obtiene la lista de empleados asignados a la campaña.
        
        Returns:
            List[Empleado]: Lista de empleados.
        """
        return self._empleados
    
    @empleados.setter
    def empleados(self, empleados: List[Empleado]) -> None:
        """
        Establece la lista de empleados asignados a la campaña.
        
        Args:
            empleados (List[Empleado]): Nueva lista de empleados.
        """
        self._empleados = empleados

    @property
    def cliente(self) -> Cliente:
        """
        Obtiene el cliente asociado a la campaña.
        
        Returns:
            Cliente: Cliente de la campaña.
        """
        return self._cliente
    
    @cliente.setter
    def cliente(self, cliente: Cliente) -> None:
        """
        Establece el cliente asociado a la campaña.
        
        Args:
            cliente (Cliente): Nuevo cliente.
        """
        self._cliente = cliente
        
    @property
    def contacto(self) -> Empleado:
        """
        Obtiene el contacto designado de la campaña.
        
        Returns:
            Empleado: Empleado designado como contacto.
        """
        return self._contacto
    
    @contacto.setter
    def contacto(self, empleado: Empleado) -> None:
        """
        Establece el contacto designado para la campaña.
        
        Args:
            empleado (Empleado): Nuevo empleado designado como contacto.
        """
        self._contacto = empleado
    
    def registrar_campana(self, titulo: str, fecha_inicio: str, fecha_fin_prevista: str, costes_estimados: float, presupuesto: float) -> None:
        """
        Registra la campaña validando que los campos obligatorios estén completos y
        establece el estado inicial de la campaña.
        
        Args:
            titulo (str): Título de la campaña.
            fecha_inicio (str): Fecha de inicio en formato "YYYY-MM-DD".
            fecha_fin_prevista (str): Fecha fin prevista en formato "YYYY-MM-DD".
            costes_estimados (float): Costes estimados.
            presupuesto (float): Presupuesto asignado.
        """
        # Incrementa el último ID y lo asigna a la campaña.
        Campana.ultimo_id += 1
        self.id = Campana.ultimo_id
        self.titulo = titulo
        self.fecha_inicio = fecha_inicio
        self.fecha_fin_prevista = fecha_fin_prevista
        self.costes_estimados = costes_estimados
        self.presupuesto = presupuesto        
        self.estado = "En ejecución"

        print(f"Campaña '{self.titulo}' registrada correctamente con estado '{self.estado}'.")

    def registrar_finalizacion(self) -> None:
        """
        Finaliza la campaña verificando que se encuentre en ejecución y actualiza el estado
        a 'Finalizada', registrando la fecha de finalización.
        
        Raises:
            ValueError: Si la campaña no está en ejecución.
        """
        if self.estado != "En ejecución":
            raise ValueError("Solo se puede finalizar una campaña en ejecución.")
        
        # Se registra la fecha de finalización utilizando la fecha y hora actuales.
        self.fecha_finalizacion = datetime.now().isoformat()
        self.estado = "Finalizada"
        print(f"Campaña '{self.titulo}' finalizada correctamente el {self.fecha_finalizacion}.")

    def agregar_pago(self, p: Pago) -> None:
        """
        Agrega un pago a la lista de pagos de la campaña.
        
        Args:
            p (Pago): Pago a agregar.
        """
        self.pagos.append(p)

    def asignar_empleado(self, e: Empleado) -> None:
        """
        Asigna un empleado a la campaña, si es que no ha sido asignado previamente.
        
        Args:
            e (Empleado): Empleado a asignar.
        """
        if e not in self.empleados:
            self.empleados.append(e)

    def registrar_gasto(self, gasto: float) -> None:
        """
        Registra un gasto en la campaña sumándolo a los costes reales.
        
        Args:
            gasto (float): Monto del gasto.
        """
        self.costes_reales += gasto
    
    def to_json(self) -> str:
        """
        Serializa la campaña a una cadena en formato JSON.
        
        Returns:
            str: Cadena JSON que representa la campaña.
        """
        return json.dumps({
            'id': self.id,
            'titulo': self.titulo,
            'fecha_inicio': date_to_str(self.fecha_inicio) if self.fecha_inicio else None,
            'fecha_fin_prevista': date_to_str(self.fecha_fin_prevista) if self.fecha_fin_prevista else None,
            'costes_estimados': self.costes_estimados,
            'presupuesto': self.presupuesto,
            'costes_reales': self.costes_reales,
            'estado': self.estado,
            'fecha_finalizacion': date_to_str(self.fecha_finalizacion) if self.fecha_finalizacion else None,
            'pagos': [p.to_json() for p in self.pagos],
            'anuncios': [a.to_json() for a in self.anuncios],
            'empleados': [e.id for e in self.empleados],
            'cliente': self.cliente.id if self.cliente else None,
            'contacto': self.contacto.id if self.contacto else None
        })

    @classmethod
    def from_json(cls, data: str) -> 'Campana':
        """
        Crea una instancia de Campana a partir de una cadena JSON.
        
        Args:
            data (str): Cadena JSON con los datos de la campaña.
        
        Returns:
            Campana: Instancia de Campana creada a partir del JSON.
        """
        data_dict = json.loads(data)
        return cls(
            id = data_dict['id'],
            titulo = data_dict['titulo'],
            fecha_inicio = data_dict['fecha_inicio'],
            fecha_fin_prevista = data_dict['fecha_fin_prevista'],
            costes_estimados = data_dict['costes_estimados'],
            presupuesto = data_dict['presupuesto'],
            costes_reales = data_dict['costes_reales'],
            estado = data_dict['estado'],
            fecha_finalizacion = data_dict['fecha_finalizacion']
        )