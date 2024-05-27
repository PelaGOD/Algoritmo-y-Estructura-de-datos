# Definición de los datos
entrenadores = [
    ["Ash", 5, 30, 70, [["Pikachu", 25, "Eléctrico", None], ["Charizard", 50, "Fuego", "Volador"], ["Bulbasaur", 20, "Planta", "Veneno"]]],
    ["Misty", 4, 20, 60, [["Starmie", 35, "Agua", "Psíquico"], ["Psyduck", 25, "Agua", None]]],
    ["Brock", 3, 25, 55, [["Onix", 40, "Roca", "Tierra"], ["Geodude", 20, "Roca", "Tierra"]]]
]

# Funciones

# a. Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            return len(entrenador[4])
    return 0

# b. Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_con_mas_de_tres_torneos(entrenadores):
    return [entrenador[0] for entrenador in entrenadores if entrenador[1] > 3]

# c. El Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_mejor_entrenador(entrenadores):
    mejor_entrenador = max(entrenadores, key=lambda e: e[1])
    return max(mejor_entrenador[4], key=lambda p: p[1])

# d. Mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_datos_entrenador(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            return entrenador
    return None

# e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79 %
def entrenadores_con_alto_porcentaje_victorias(entrenadores):
    return [entrenador[0] for entrenador in entrenadores if (entrenador[3] / (entrenador[2] + entrenador[3])) > 0.79]

# f. Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
def entrenadores_con_pokemons_especiales(entrenadores):
    entrenadores_especiales = []
    for entrenador in entrenadores:
        tiene_fuego_y_planta = False
        tiene_agua_volador = False
        for pokemon in entrenador[4]:
            if pokemon[2] == "Fuego" and pokemon[3] == "Planta":
                tiene_fuego_y_planta = True
            if pokemon[2] == "Agua" and pokemon[3] == "Volador":
                tiene_agua_volador = True
        if tiene_fuego_y_planta or tiene_agua_volador:
            entrenadores_especiales.append(entrenador[0])
    return entrenadores_especiales

# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(entrenadores, nombre_entrenador):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            pokemons = entrenador[4]
            return sum(pokemon[1] for pokemon in pokemons) / len(pokemons)
    return 0

# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def entrenadores_con_pokemon(entrenadores, nombre_pokemon):
    return sum(1 for entrenador in entrenadores if any(pokemon[0] == nombre_pokemon for pokemon in entrenador[4]))

# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemons_repetidos(entrenadores):
    entrenadores_repetidos = []
    for entrenador in entrenadores:
        nombres_pokemons = [pokemon[0] for pokemon in entrenador[4]]
        if len(nombres_pokemons) != len(set(nombres_pokemons)):
            entrenadores_repetidos.append(entrenador[0])
    return entrenadores_repetidos

# j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos(entrenadores):
    pokemons_especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    return [entrenador[0] for entrenador in entrenadores if any(pokemon[0] in pokemons_especificos for pokemon in entrenador[4])]

# k. Determinar si un entrenador “X” tiene al Pokémon “Y”
def entrenador_tiene_pokemon(entrenadores, nombre_entrenador, nombre_pokemon):
    for entrenador in entrenadores:
        if entrenador[0] == nombre_entrenador:
            for pokemon in entrenador[4]:
                if pokemon[0] == nombre_pokemon:
                    return entrenador, pokemon
    return None

# Ejemplo de uso de las funciones
if __name__ == "__main__":
    print("a. Cantidad de Pokémons de Ash:", cantidad_pokemons(entrenadores, "Ash"))
    print("b. Entrenadores con más de tres torneos ganados:", entrenadores_con_mas_de_tres_torneos(entrenadores))
    print("c. Pokémon de mayor nivel del mejor entrenador:", pokemon_mayor_nivel_mejor_entrenador(entrenadores))
    print("d. Datos de Misty:", mostrar_datos_entrenador(entrenadores, "Misty"))
    print("e. Entrenadores con porcentaje de victorias > 79%:", entrenadores_con_alto_porcentaje_victorias(entrenadores))
    print("f. Entrenadores con Pokémons especiales:", entrenadores_con_pokemons_especiales(entrenadores))
    print("g. Promedio de nivel de los Pokémons de Brock:", promedio_nivel_pokemons(entrenadores, "Brock"))
    print("h. Entrenadores con Pikachu:", entrenadores_con_pokemon(entrenadores, "Pikachu"))
    print("i. Entrenadores con Pokémons repetidos:", entrenadores_con_pokemons_repetidos(entrenadores))
    print("j. Entrenadores con Tyrantrum, Terrakion o Wingull:", entrenadores_con_pokemons_especificos(entrenadores))
    entrenador, pokemon = entrenador_tiene_pokemon(entrenadores, "Ash", "Pikachu")
    if entrenador:
        print("k. Ash tiene a Pikachu:", entrenador, pokemon)
    else:
        print("k. Ash no tiene a Pikachu")
