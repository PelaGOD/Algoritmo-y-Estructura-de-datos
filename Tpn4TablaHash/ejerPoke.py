class Pokemon:
    def __init__(self, numero, nombre, tipos, nivel):
        self.numero = numero
        self.nombre = nombre
        self.tipos = tipos
        self.nivel = nivel

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def insert(self, key, value):
        index = key % self.size
        self.table[index].append(value)

    def get_items(self, condition):
        # Retorna los elementos que cumplen con una condición dada
        results = []
        for bucket in self.table:
            for item in bucket:
                if condition(item):
                    results.append(item)
        return results

# Crear las tres tablas hash
pokemon_por_tipo = HashTable(20)  # Suponemos 20 tipos diferentes de Pokémon
pokemon_por_numero = HashTable(10)  # Último dígito del número, por lo tanto 10 posiciones
pokemon_por_nivel = HashTable(10)  # Niveles distribuidos en 10 posiciones

# Función para insertar un Pokémon en las tres tablas hash
def insertar_pokemon(pokemon):
    # Tabla 1: Hash por tipo de Pokémon
    for tipo in pokemon.tipos:
        tipo_hash = hash(tipo) % pokemon_por_tipo.size
        pokemon_por_tipo.insert(tipo_hash, pokemon)

    # Tabla 2: Hash por último dígito del número del Pokémon
    numero_hash = pokemon.numero % 10
    pokemon_por_numero.insert(numero_hash, pokemon)

    # Tabla 3: Hash por nivel del Pokémon (dividido en 10 posiciones)
    nivel_hash = pokemon.nivel % 10
    pokemon_por_nivel.insert(nivel_hash, pokemon)

# a. Insertar los Pokémons
pokemons = [
    Pokemon(3, "Bulbasaur", ["Planta", "Veneno"], 5),
    Pokemon(7, "Charmander", ["Fuego"], 10),
    Pokemon(9, "Squirtle", ["Agua"], 8),
    Pokemon(1, "Pikachu", ["Eléctrico"], 15),
    Pokemon(4, "Charizard", ["Fuego", "Volador"], 20),
    Pokemon(2, "Clefairy", ["Magia"], 12),
    Pokemon(6, "Jolteon", ["Eléctrico"], 18),
    Pokemon(8, "Gengar", ["Fantasma", "Veneno"], 22),

]
for p in pokemons:
    insertar_pokemon(p)

# e. Mostrar todos los Pokémons cuyos números terminan en 3, 7 y 9
def mostrar_por_numero_finales():
    numeros_finales = [3, 7, 9]
    for n in numeros_finales:
        resultados = pokemon_por_numero.get_items(lambda p: p.numero % 10 == n)
        for pokemon in resultados:
            print(f"Pokemon número {pokemon.numero}, nombre: {pokemon.nombre}")

# f. Mostrar todos los Pokémons cuyos niveles son múltiplos de 2, 5 y 10
def mostrar_por_nivel_multiplos():
    multiplos = [2, 5, 10]
    resultados = []
    for m in multiplos:
        resultados += pokemon_por_nivel.get_items(lambda p: p.nivel % m == 0)
    # Evitar duplicados al agregar resultados
    resultados = list({p.numero: p for p in resultados}.values())
    for pokemon in resultados:
        print(f"Pokemon número {pokemon.numero}, nombre: {pokemon.nombre}, nivel: {pokemon.nivel}")

# g. Mostrar todos los Pokémons de los tipos Acero, Fuego, Eléctrico, Hielo
def mostrar_por_tipo_especifico():
    tipos_especificos = ["Acero", "Fuego", "Eléctrico", "Hielo"]
    for tipo in tipos_especificos:
        tipo_hash = hash(tipo) % pokemon_por_tipo.size
        resultados = pokemon_por_tipo.get_items(lambda p: tipo in p.tipos)
        for pokemon in resultados:
            print(f"Pokemon número {pokemon.numero}, nombre: {pokemon.nombre}, tipo: {tipo}")

# Ejecutar las consultas
print("Pokémons cuyos números terminan en 3, 7 y 9:")
mostrar_por_numero_finales()

print("\nPokémons cuyos niveles son múltiplos de 2, 5 y 10:")
mostrar_por_nivel_multiplos()

print("\nPokémons de tipo Acero, Fuego, Eléctrico, Hielo:")
mostrar_por_tipo_especifico()
