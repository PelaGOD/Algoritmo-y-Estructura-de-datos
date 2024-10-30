def barrido_profundidad(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()

    print(inicio)
    visitados.add(inicio)

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            barrido_profundidad(grafo, vecino, visitados)