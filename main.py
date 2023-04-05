from metabuscador import Metabuscador
from reporte import Reporte
from base_datos import BaseDatos
from web import app

def main():
    # Configuración de la base de datos
    bd = BaseDatos()

    # Configuración del metabuscador
    mb = Metabuscador()
    lista_activos = mb.buscar_activos('country:"ES"')
    bd.insertar_activos(lista_activos)
    
    # Configuración del generador de reportes
    rpt = Reporte()

    # Configuración de la aplicación web
    app.config['BD'] = bd
    app.config['MB'] = mb
    app.config['RPT'] = rpt

    # Inicio de la aplicación web
    app.run()

if __name__ == '__main__':
    main()
