from collections import deque

# Definimos una clase para manejar los personajes
class PersonajeMCU:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero

# Crear una cola con personajes del MCU
cola_mcu = deque([
    PersonajeMCU("Tony Stark", "Iron Man", "M"),
    PersonajeMCU("Steve Rogers", "Capitán América", "M"),
    PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
    PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
    PersonajeMCU("Scott Lang", "Ant-Man", "M"),
    PersonajeMCU("Peter Parker", "Spider-Man", "M"),
    PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F")
])

# a. Determinar el nombre del personaje de la superheroína Capitana Marvel
def obtener_personaje_por_superheroe(cola, nombre_superheroe):
    for personaje in cola:
        if personaje.nombre_superheroe == nombre_superheroe:
            return personaje.nombre_personaje
    return None

# b. Mostrar los nombres de los superhéroes femeninos
def mostrar_superheroes_femeninos(cola):
    print("Superhéroes femeninos:")
    for personaje in cola:
        if personaje.genero == "F":
            print(f"- {personaje.nombre_superheroe}")

# c. Mostrar los nombres de los personajes masculinos
def mostrar_personajes_masculinos(cola):
    print("Personajes masculinos:")
    for personaje in cola:
        if personaje.genero == "M":
            print(f"- {personaje.nombre_personaje}")

# d. Determinar el nombre del superhéroe del personaje Scott Lang
def obtener_superheroe_por_personaje(cola, nombre_personaje):
    for personaje in cola:
        if personaje.nombre_personaje == nombre_personaje:
            return personaje.nombre_superheroe
    return None

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
def mostrar_datos_por_inicial(cola, letra):
    print(f"Personajes o superhéroes cuyos nombres comienzan con '{letra}':")
    for personaje in cola:
        if personaje.nombre_personaje.startswith(letra) or personaje.nombre_superheroe.startswith(letra):
            print(f"Personaje: {personaje.nombre_personaje}, Superhéroe: {personaje.nombre_superheroe}, Género: {personaje.genero}")

# Ejecutar las actividades

# a. Determinar el nombre del personaje de la superheroína Capitana Marvel
nombre_capitana_marvel = obtener_personaje_por_superheroe(cola_mcu, "Capitana Marvel")
print(f"El nombre del personaje de Capitana Marvel es: {nombre_capitana_marvel}")

# b. Mostrar los nombres de los superhéroes femeninos
mostrar_superheroes_femeninos(cola_mcu)

# c. Mostrar los nombres de los personajes masculinos
mostrar_personajes_masculinos(cola_mcu)

# d. Determinar el nombre del superhéroe del personaje Scott Lang
superheroe_scott_lang = obtener_superheroe_por_personaje(cola_mcu, "Scott Lang")
print(f"El nombre del superhéroe de Scott Lang es: {superheroe_scott_lang}")

# e. Mostrar todos los datos de los superhéroes o personajes cuyos nombres comienzan con la letra S
mostrar_datos_por_inicial(cola_mcu, "S")
