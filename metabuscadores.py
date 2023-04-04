import shodan

class Metabuscador:
    def __init__(self, api_key):
        self.api_key = api_key

    def buscar_activos(self, query):
        pass

class Shodan(Metabuscador):
    def __init__(self, api_key):
        super().__init__(api_key)
        self.api = shodan.Shodan(api_key)

    def buscar_activos(self, query):
        try:
            resultados = self.api.search(query)
            return resultados['matches']
        except shodan.APIError as e:
            print('Error al realizar la búsqueda en Shodan:', e)
            return []
