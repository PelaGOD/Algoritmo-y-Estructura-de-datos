import heapq

class GrafoCasa:
    def __init__(self):
        self.vertices = {}

    def insertar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = {'adyacentes': {}}

    def insertar_arista(self, peso, origen, destino):
        if origen in self.vertices and destino in self.vertices:
            self.vertices[origen]['adyacentes'][destino] = peso
            self.vertices[destino]['adyacentes'][origen] = peso

    def dijkstra(self, inicio, fin):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[inicio] = 0
        predecesores = {inicio: None}
        cola = [(0, inicio)]

        while cola:
            distancia_actual, vertice_actual = heapq.heappop(cola)
            if vertice_actual == fin:
                break
            for vecino, peso in self.vertices[vertice_actual]['adyacentes'].items():
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    predecesores[vecino] = vertice_actual
                    heapq.heappush(cola, (distancia, vecino))

        camino = []
        vertice = fin
        while vertice:
            camino.insert(0, vertice)
            vertice = predecesores.get(vertice)

        return distancias[fin], camino

    def prim(self):
        visitados = set()
        bosque = []
        origen = next(iter(self.vertices))
        aristas = [(peso, origen, destino) for destino, peso in self.vertices[origen]['adyacentes'].items()]
        heapq.heapify(aristas)
        visitados.add(origen)

        while aristas:
            peso, origen, destino = heapq.heappop(aristas)
            if destino not in visitados:
                visitados.add(destino)
                bosque.append((peso, (origen, destino)))
                for siguiente, peso in self.vertices[destino]['adyacentes'].items():
                    if siguiente not in visitados:
                        heapq.heappush(aristas, (peso, destino, siguiente))

        return bosque

# Crear el grafo para la casa
grafo_casa = GrafoCasa()

# Agregar los ambientes como vértices
ambientes = ['cocina', 'comedor', 'cochera', 'quincho', 'baño 1', 'baño 2', 'habitación 1', 
            'habitación 2', 'sala de estar', 'terraza', 'patio']

for ambiente in ambientes:
    grafo_casa.insertar_vertice(ambiente)

# Agregar las aristas (distancias en metros)
aristas = [
    (5, 'cocina', 'comedor'), (7, 'cocina', 'baño 1'), (10, 'cocina', 'sala de estar'),
    (5, 'comedor', 'cocina'), (8, 'comedor', 'terraza'), (9, 'comedor', 'patio'),
    (6, 'cochera', 'patio'), (12, 'cochera', 'terraza'), (5, 'cochera', 'baño 1'),
    (7, 'quincho', 'patio'), (4, 'quincho', 'baño 2'), (8, 'quincho', 'habitación 1'),
    (10, 'habitación 1', 'sala de estar'), (5, 'habitación 1', 'habitación 2'),
    (8, 'baño 1', 'baño 2'), (7, 'baño 2', 'habitación 2')
]

for peso, origen, destino in aristas:
    grafo_casa.insertar_arista(peso, origen, destino)

# Obtener el árbol de expansión mínima
bosque = grafo_casa.prim()
total_cable = sum([arista[0] for arista in bosque])
print('Árbol de expansión mínima:')
for conexion in bosque:
    print(conexion[1][0], '-', conexion[1][1], '->', conexion[0], 'metros')
print('Total de metros de cable para conectar todos los ambientes:', total_cable)

# Obtener el camino más corto de habitación 1 a sala de estar
distancia, camino = grafo_casa.dijkstra('habitación 1', 'sala de estar')
print('\nCamino más corto de "habitación 1" a "sala de estar":')
print(' -> '.join(camino), '| Distancia total:', distancia, 'metros')
