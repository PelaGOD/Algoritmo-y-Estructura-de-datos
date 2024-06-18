class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre  # Nombre del superhéroe o villano
        self.es_heroe = es_heroe  # True si es un héroe, False si es un villano
        self.izquierdo = None  # Subárbol izquierdo
        self.derecho = None  # Subárbol derecho

# Función para insertar en el árbol (por orden alfabético del nombre)
def insertar_nodo(raiz, nombre, es_heroe):
    if raiz is None:
        return NodoArbol(nombre, es_heroe)
    if nombre < raiz.nombre:
        raiz.izquierdo = insertar_nodo(raiz.izquierdo, nombre, es_heroe)
    else:
        raiz.derecho = insertar_nodo(raiz.derecho, nombre, es_heroe)
    return raiz

# a. Insertamos los nodos en el árbol con sus respectivos valores (héroe o villano)
def crear_arbol_mcu():
    personajes = [
        ("Iron Man", True), ("Thanos", False), ("Capitán América", True),
        ("Doctor Strange", True), ("Loki", False), ("Black Widow", True),
        ("Red Skull", False), ("Ultron", False), ("Scarlet Witch", True),
        ("Winter Soldier", True), ("Spider-Man", True)
    ]
    raiz = None
    for nombre, es_heroe in personajes:
        raiz = insertar_nodo(raiz, nombre, es_heroe)
    return raiz

# b. Listar los villanos ordenados alfabéticamente
def listar_villanos(raiz, villanos=[]):
    if raiz is not None:
        listar_villanos(raiz.izquierdo, villanos)
        if not raiz.es_heroe:
            villanos.append(raiz.nombre)
        listar_villanos(raiz.derecho, villanos)
    return villanos

# c. Mostrar todos los superhéroes que empiezan con 'C'
def listar_superheroes_con_c(raiz, resultado=[]):
    if raiz is not None:
        listar_superheroes_con_c(raiz.izquierdo, resultado)
        if raiz.es_heroe and raiz.nombre.startswith('C'):
            resultado.append(raiz.nombre)
        listar_superheroes_con_c(raiz.derecho, resultado)
    return resultado

# d. Determinar cuántos superhéroes hay en el árbol
def contar_superheroes(raiz):
    if raiz is None:
        return 0
    conteo = 1 if raiz.es_heroe else 0
    conteo += contar_superheroes(raiz.izquierdo)
    conteo += contar_superheroes(raiz.derecho)
    return conteo

# e. Buscar Doctor Strange por proximidad y corregir su nombre
def buscar_y_modificar(raiz, nombre_incorrecto, nombre_correcto):
    if raiz is None:
        return None
    if nombre_incorrecto in raiz.nombre:  # Búsqueda por proximidad
        raiz.nombre = nombre_correcto
        return raiz
    if nombre_incorrecto < raiz.nombre:
        return buscar_y_modificar(raiz.izquierdo, nombre_incorrecto, nombre_correcto)
    else:
        return buscar_y_modificar(raiz.derecho, nombre_incorrecto, nombre_correcto)

# f. Listar los superhéroes ordenados de manera descendente
def listar_superheroes_descendente(raiz, superheroes=[]):
    if raiz is not None:
        listar_superheroes_descendente(raiz.derecho, superheroes)
        if raiz.es_heroe:
            superheroes.append(raiz.nombre)
        listar_superheroes_descendente(raiz.izquierdo, superheroes)
    return superheroes

# Crear el árbol MCU
raiz_mcu = crear_arbol_mcu()

# b. Listar los villanos ordenados alfabéticamente
villanos = listar_villanos(raiz_mcu)
print("Villanos ordenados alfabéticamente:", villanos)

# c. Mostrar todos los superhéroes que empiezan con 'C'
superheroes_con_c = listar_superheroes_con_c(raiz_mcu)
print("Superhéroes que comienzan con 'C':", superheroes_con_c)

# d. Determinar cuántos superhéroes hay en el árbol
total_superheroes = contar_superheroes(raiz_mcu)
print("Cantidad de superhéroes en el árbol:", total_superheroes)

# e. Doctor Strange está mal cargado, corregir su nombre
buscar_y_modificar(raiz_mcu, "Doctor Strange", "Dr. Strange")
print("Nombre corregido de Doctor Strange:", "Dr. Strange" if buscar_y_modificar else "No encontrado")

# f. Listar los superhéroes ordenados de manera descendente
superheroes_descendente = listar_superheroes_descendente(raiz_mcu)
print("Superhéroes ordenados de manera descendente:", superheroes_descendente)
