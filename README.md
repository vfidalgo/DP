# DP


# Shodan Scanner

![Python version](https://img.shields.io/badge/python-3.9-blue)
![License](https://img.shields.io/github/license/yourusername/shodan-scanner)

Este proyecto es una herramienta para escanear en búsqueda de banners en Shodan, con el fin de identificar posibles vulnerabilidades en los sistemas encontrados.

## Requisitos

- Python 3.9 o superior
- Clave de API de Shodan

## Instalación

1. Clonar el repositorio: `git clone https://github.com/yourusername/shodan-scanner.git`
2. Instalar las dependencias: `pip install -r requirements.txt`
3. Configurar la clave de API de Shodan en el archivo `.env`

## Uso

Ejecutar el archivo `main.py` para iniciar la herramienta. Se puede acceder a la interfaz web en la dirección `http://localhost:8000`.

## Versiones

### Versión 0.1
- Escaneo de banners en Shodan
- Almacenamiento de resultados en base de datos
- Interfaz web para visualizar los resultados

## Contribuir

Cualquier contribución al proyecto será bienvenida. Por favor, crea un pull request para que podamos revisarlo.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más información, revisar el archivo LICENSE.

## Autor

Desarrollado por [vfidalgo](https://github.com/vfidalgo)

main.py: El archivo principal que contendrá la lógica del proyecto y que se encargará de coordinar los distintos módulos y componentes.

utils.py: Un módulo que contendrá funciones útiles y reutilizables que podrán ser utilizadas en otros módulos del proyecto.

metabuscadores.py: Un módulo que se encargará de interactuar con los diferentes metabuscadores, utilizando sus APIs para realizar consultas y obtener información sobre los activos expuestos en Internet.

base_datos.py: Un módulo que se encargará de manejar la conexión y la gestión de la base de datos.

analisis_vulnerabilidades.py: Un módulo que se encargará de analizar la información recopilada de los banners para identificar posibles vulnerabilidades.

notificaciones.py: Un módulo que se encargará de enviar notificaciones y alertas en caso de que se identifiquen vulnerabilidades.

web.py: Un módulo que se encargará de construir una interfaz de usuario web para visualizar los resultados.
