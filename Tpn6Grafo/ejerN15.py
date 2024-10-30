import heapq

class GrafoMaravillas:
    def __init__(self):
        self.vertices = {}

    def insertar_vertice(self, nombre, data):
        if nombre not in self.vertices:
            self.vertices[nombre] = {'adyacentes': {}, 'data': data}

    def insertar_arista(self, peso, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen]['adyacentes'][destino] = peso
            self.vertices[destino]['adyacentes'][origen] = peso

    def prim(self, tipo):
        visitados = set()
        bosque = []
        origen = next((v for v in self.vertices if self.vertices[v]['data']['tipo'] == tipo), None)
        aristas = [(peso, origen, destino) for destino, peso in self.vertices[origen]['adyacentes'].items()]
        heapq.heapify(aristas)
        visitados.add(origen)

        while aristas:
            peso, origen, destino = heapq.heappop(aristas)
            if destino not in visitados and self.vertices[destino]['data']['tipo'] == tipo:
                visitados.add(destino)
                bosque.append((peso, (origen, destino)))
                for siguiente, peso in self.vertices[destino]['adyacentes'].items():
                    if siguiente not in visitados:
                        heapq.heappush(aristas, (peso, destino, siguiente))

        return bosque

    def verificar_paises_con_ambos_tipos(self):
        pais_maravillas = {}
        for nombre, datos in self.vertices.items():
            paises = datos['data']['pais'].split(', ')
            tipo = datos['data']['tipo']
            for pais in paises:
                if pais not in pais_maravillas:
                    pais_maravillas[pais] = set()
                pais_maravillas[pais].add(tipo)

        return [pais for pais, tipos in pais_maravillas.items() if len(tipos) > 1]

# Crear el grafo para las maravillas del mundo
grafo_maravillas = GrafoMaravillas()

# Agregar las maravillas con su tipo y país
maravillas = [
    ('Gran Muralla China', 'China', 'arquitectónica'),
    ('Petra', 'Jordania', 'arquitectónica'),
    ('Cristo Redentor', 'Brasil', 'arquitectónica'),
    ('Machu Picchu', 'Perú', 'arquitectónica'),
    ('Chichen Itza', 'México', 'arquitectónica'),
    ('Coliseo', 'Italia', 'arquitectónica'),
    ('Taj Mahal', 'India', 'arquitectónica'),
    ('Amazonas', 'Brasil, Perú, Colombia', 'natural'),
    ('Bahía de Ha-Long', 'Vietnam', 'natural'),
    ('Cataratas del Iguazú', 'Argentina, Brasil', 'natural'),
    ('Isla de Komodo', 'Indonesia', 'natural'),
    ('Montaña de la Mesa', 'Sudáfrica', 'natural'),
    ('Parque Nacional de Jeju', 'Corea del Sur', 'natural'),
    ('Parque Nacional de Puerto Princesa', 'Filipinas', 'natural')
]

for nombre, pais, tipo in maravillas:
    grafo_maravillas.insertar_vertice(nombre, data={'pais': pais, 'tipo': tipo})

# Agregar aristas entre maravillas del mismo tipo
distancias_arq = [
    (1000, 'Gran Muralla China', 'Petra'), (1200, 'Gran Muralla China', 'Cristo Redentor'),
    (800, 'Gran Muralla China', 'Machu Picchu'), (500, 'Petra', 'Chichen Itza'),
    (900, 'Cristo Redentor', 'Chichen Itza'), (600, 'Machu Picchu', 'Taj Mahal')
]

distancias_nat = [
    (700, 'Amazonas', 'Bahía de Ha-Long'), (1200, 'Amazonas', 'Cataratas del Iguazú'),
    (800, 'Isla de Komodo', 'Montaña de la Mesa'), (500, 'Parque Nacional de Jeju', 'Parque Nacional de Puerto Princesa')
]

for peso, origen, destino in distancias_arq:
    grafo_maravillas.insertar_arista(peso, origen, destino)

for peso, origen, destino in distancias_nat:
    grafo_maravillas.insertar_arista(peso, origen, destino)

# Árbol de expansión mínima para maravillas arquitectónicas
bosque_arq = grafo_maravillas.prim('arquitectónica')
print('\nÁrbol de expansión mínima para maravillas arquitectónicas:')
for conexion in bosque_arq:
    print(conexion[1][0], '-', conexion[1][1], '->', conexion[0], 'km')

# Verificación de países con maravillas de ambos tipos
paises_ambos_tipos = grafo_maravillas.verificar_paises_con_ambos_tipos()
print('\nPaíses con maravillas de ambos tipos (arquitectónica y natural):', paises_ambos_tipos)

