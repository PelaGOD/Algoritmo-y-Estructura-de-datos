from dino import dinosaurios

def procesar_dinosaurios(pila):
    especies = []
    descubridores = []
    dinosaurios_con_t = []
    dinosaurios_ligeros = []
    pila_aqs = []

    while pila:
        dinosaurio = pila.pop()
        if dinosaurio['especie'] not in especies:
            especies.append(dinosaurio['especie'])
        if dinosaurio['descubridor'] not in descubridores:
            descubridores.append(dinosaurio['descubridor'])
        if dinosaurio['nombre'][0] == 'T':
            dinosaurios_con_t.append(dinosaurio)
        if int(dinosaurio['peso'].split()[0]) < 275:
            dinosaurios_ligeros.append(dinosaurio)
        if dinosaurio['nombre'][0] in ['A', 'Q', 'S']:
            pila_aqs.append(dinosaurio)

    print(f"Hay {len(especies)} especies distintas.")
    print(f"Hay {len(descubridores)} descubridores distintos.")
    print("Dinosaurios que empiezan con T:")
    for dino in dinosaurios_con_t:
        print(dino['nombre'])
    print("Dinosaurios que pesan menos de 275 Kg:")
    for dino in dinosaurios_ligeros:
        print(dino['nombre'])
    print("Dinosaurios que empiezan con A, Q, S:")
    while pila_aqs:
        print(pila_aqs.pop()['nombre'])


procesar_dinosaurios(dinosaurios)

