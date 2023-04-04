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
