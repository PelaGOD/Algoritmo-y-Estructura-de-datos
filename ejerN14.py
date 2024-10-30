def existe_paso(grafo, origen, destino, visitados=None):
    if visitados is None:
        visitados = set()
    
    if origen == destino:
        return True

    visitados.add(origen)

    for vecino in grafo.get(origen, []):
        if vecino not in visitados:
            if existe_paso(grafo, vecino, destino, visitados):
                return True

    return False