from __future__ import annotations
from src.model.Cliente import Cliente
from src.model.Campana import Campana
from typing import List
import json, os

class ClienteController:
    def __init__(self, file_path: str = "./data/clientes.json") -> None:
        self.file_path = file_path
        self.clientes = self.cargar_clientes()
        
    def cargar_clientes(self) -> dict[str, Cliente]:
        """
        Cargar clientes del archivo JSON y los almacena en un diccionario
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                try:
                    data = json.load(file)
                    clientes = {}
                    for c in data:
                        cliente = Cliente(
                            id = c['id'],
                            nombre = c['nombre'], 
                            direccion = c['direccion'], 
                            detalle_contacto = c['detalle_contacto'], 
                            #campañas = List[Campana] = None
                        )
                    return clientes
                except json.JSONDecodeError:
                    return {}
    
    def guardar_clientes(self) -> None:
        """
        Guardar los clientes en el archivo JSON
        """
        data = []
        for cliente in self.clientes.values():
            data.append({
                'id': cliente.id,
                'nombre': cliente.nombre,
                'direccion': cliente.direccion,
                'detalle_contacto': cliente.detalle_contacto,
                'campañas': cliente.campañas
            })
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent = 4)
            