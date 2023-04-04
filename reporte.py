from typing import List
import json
from datetime import datetime

class Reporte:
    def __init__(self, activos: List, fecha: str):
        self.activos = activos
        self.fecha = fecha

    def generar_reporte(self):
        datos = {}
        datos["fecha"] = self.fecha
        datos["activos"] = []
        for activo in self.activos:
            activo_datos = {}
            activo_datos["ip"] = activo.ip
            activo_datos["puertos"] = activo.puertos_abiertos
            activo_datos["vulnerabilidades"] = activo.vulnerabilidades
            datos["activos"].append(activo_datos)

        nombre_archivo = f"reporte_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json"
        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)
        
        print(f"Reporte generado en el archivo {nombre_archivo}")
