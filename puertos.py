import nmap
from typing import List

class Puerto:
    def __init__(self, numero: int, servicio: str):
        self.numero = numero
        self.servicio = servicio
        self.vulnerabilidades = []

    def __str__(self):
        return f"{self.numero}/{self.servicio}"

class Nmap:
    def __init__(self, targets: List[str]):
        self.targets = targets
        self.nm = nmap.PortScanner()

    def scan(self):
        self.nm.scan(hosts=" ".join(self.targets), arguments="-p-")

    def puertos_abiertos(self):
        result = []
        for host in self.nm.all_hosts():
            for port in self.nm[host]['tcp']:
                if self.nm[host]['tcp'][port]['state'] == 'open':
                    p = Puerto(port, self.nm[host]['tcp'][port]['name'])
                    result.append(p)
        return result

def buscar_vulnerabilidades(puertos: List[Puerto]):
    for puerto in puertos:
        banner = puerto.servicio
        # Aquí iría la lógica para buscar vulnerabilidades a partir del banner
        # por ejemplo, utilizando la API de un proveedor de vulnerabilidades
        # o haciendo web scraping en busca de información relevante.
        # En este caso, como ejemplo, simplemente añadimos algunas vulnerabilidades
        # de ejemplo.
        puerto.vulnerabilidades = ['CVE-2021-1234', 'CVE-2022-5678']
