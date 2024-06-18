from collections import deque

# Definimos una clase para manejar los personajes
class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

# Crear una cola con personajes de Star Wars
cola_personajes = deque([
    Personaje("Luke Skywalker", "Tatooine"),
    Personaje("Leia Organa", "Alderaan"),
    Personaje("Han Solo", "Corellia"),
    Personaje("Yoda", "Dagobah"),
    Personaje("Jar Jar Binks", "Naboo"),
    Personaje("Chewbacca", "Kashyyyk"),
    Personaje("Darth Vader", "Tatooine")
])

# a. Mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrar_personajes_planetas(cola, planetas):
    print("Personajes de los planetas seleccionados:")
    for personaje in cola:
        if personaje.planeta in planetas:
            print(f"- {personaje.nombre} del planeta {personaje.planeta}")

# b. Indicar el planeta natal de Luke Skywalker y Han Solo
def planeta_personajes(cola, nombres):
    for personaje in cola:
        if personaje.nombre in nombres:
            print(f"{personaje.nombre} es de {personaje.planeta}")

# c. Insertar un nuevo personaje antes del maestro Yoda
def insertar_antes_de(cola, nuevo_personaje, nombre_objetivo):
    cola_aux = deque()  # Cola temporal
    while cola:
        personaje_actual = cola.popleft()
        if personaje_actual.nombre == nombre_objetivo:
            cola_aux.append(nuevo_personaje)  # Insertar el nuevo personaje antes del objetivo
        cola_aux.append(personaje_actual)
    return cola_aux

# d. Eliminar el personaje ubicado después de Jar Jar Binks
def eliminar_despues_de(cola, nombre_objetivo):
    cola_aux = deque()
    eliminar_siguiente = False
    while cola:
        personaje_actual = cola.popleft()
        if eliminar_siguiente:
            eliminar_siguiente = False  # Eliminar el personaje que sigue
            continue
        cola_aux.append(personaje_actual)
        if personaje_actual.nombre == nombre_objetivo:
            eliminar_siguiente = True
    return cola_aux


# Mostrar los personajes de los planetas Alderaan, Endor y Tatooine
mostrar_personajes_planetas(cola_personajes, ["Alderaan", "Endor", "Tatooine"])

# Indicar el planeta natal de Luke Skywalker y Han Solo
print("\nPlaneta natal de Luke Skywalker y Han Solo:")
planeta_personajes(cola_personajes, ["Luke Skywalker", "Han Solo"])

# Insertar un nuevo personaje antes del maestro Yoda
nuevo_personaje = Personaje("Obi-Wan Kenobi", "Stewjon")
cola_personajes = insertar_antes_de(cola_personajes, nuevo_personaje, "Yoda")
print("\nCola después de insertar a Obi-Wan Kenobi antes de Yoda:")
for personaje in cola_personajes:
    print(f"{personaje.nombre} del planeta {personaje.planeta}")

# Eliminar el personaje ubicado después de Jar Jar Binks
cola_personajes = eliminar_despues_de(cola_personajes, "Jar Jar Binks")
print("\nCola después de eliminar el personaje siguiente a Jar Jar Binks:")
for personaje in cola_personajes:
    print(f"{personaje.nombre} del planeta {personaje.planeta}")
