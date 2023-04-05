from datetime import datetime
import pymongo

class BaseDatos:
    def __init__(self, db_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.ips = self.db["ips"]

    def insertar_ip(self, ip, banners):
        # Si la ip ya existe, se actualizan los banners encontrados
        if self.ips.count_documents({"ip": ip}) > 0:
            self.ips.update_one({"ip": ip}, {"$set": {"banners": banners}})
        # Si la ip no existe, se inserta en la base de datos
        else:
            self.ips.insert_one({"ip": ip, "banners": banners})

    def insertar_activos(self, activos):
        fecha_hora_actual = datetime.now()
        activos_insertados = 0
        
        for activo in activos:
            ip = activo["ip"]
            banners = activo["banners"]
            self.insertar_ip(ip, banners)
            activos_insertados += 1
            
        print(f"{activos_insertados} activos insertados en la base de datos en {fecha_hora_actual}.")
    
    def obtener_activos(self):
        activos = []
        for activo in self.ips.find():
            activos.append(activo)
        return activos