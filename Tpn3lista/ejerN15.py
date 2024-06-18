class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __repr__(self):
        return f"Pokemon({self.nombre}, Nivel: {self.nivel}, Tipo: {self.tipo}, Subtipo: {self.subtipo})"

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, pokemons=None):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = pokemons if pokemons is not None else []

    def __repr__(self):
        return (f"Entrenador({self.nombre}, Torneos ganados: {self.torneos_ganados}, "
                f"Batallas perdidas: {self.batallas_perdidas}, Batallas ganadas: {self.batallas_ganadas}, "
                f"Pokemons: {self.pokemons})")

entrenadores = [
    Entrenador("Ash", 5, 20, 80, [
        Pokemon("Pikachu", 25, "Eléctrico", ""),
        Pokemon("Charizard", 36, "Fuego", "Volador"),
        Pokemon("Bulbasaur", 18, "Planta", "Veneno")
    ]),
    Entrenador("Brock", 2, 10, 40, [
        Pokemon("Onix", 30, "Roca", "Tierra"),
        Pokemon("Geodude", 20, "Roca", "Tierra")
    ]),
    Entrenador("Misty", 4, 15, 60, [
        Pokemon("Starmie", 35, "Agua", "Psíquico"),
        Pokemon("Psyduck", 25, "Agua", "")
    ]),
]

def cantidad_pokemons(entrenador_nombre, entrenadores):
    for entrenador in entrenadores:
        if entrenador.nombre == entrenador_nombre:
            return len(entrenador.pokemons)
    return 0

print(cantidad_pokemons("Ash", entrenadores))  # Ejemplo

def entrenadores_mas_de_tres_torneos(entrenadores):
    return [entrenador.nombre for entrenador in entrenadores if entrenador.torneos_ganados > 3]

print(entrenadores_mas_de_tres_torneos(entrenadores))  # Ejemplo

def pokemon_mayor_nivel_mejor_entrenador(entrenadores):
    mejor_entrenador = max(entrenadores, key=lambda e: e.torneos_ganados)
    return max(mejor_entrenador.pokemons, key=lambda p: p.nivel)

print(pokemon_mayor_nivel_mejor_entrenador(entrenadores))  # Ejemplo

def mostrar_entrenador_y_pokemons(entrenador_nombre, entrenadores):
    for entrenador in entrenadores:
        if entrenador.nombre == entrenador_nombre:
            return entrenador
    return None

print(mostrar_entrenador_y_pokemons("Ash", entrenadores))  # Ejemplo

def entrenadores_con_porcentaje_ganadas_mayor_79(entrenadores):
    return [entrenador.nombre for entrenador in entrenadores 
            if entrenador.batallas_ganadas / (entrenador.batallas_ganadas + entrenador.batallas_perdidas) > 0.79]

print(entrenadores_con_porcentaje_ganadas_mayor_79(entrenadores))  # Ejemplo

def entrenadores_con_tipos_especiales(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        tipos = {pokemon.tipo for pokemon in entrenador.pokemons}
        subtipos = {pokemon.subtipo for pokemon in entrenador.pokemons}
        if ("Fuego" in tipos and "Planta" in tipos) or ("Agua" in tipos and "Volador" in subtipos):
            resultado.append(entrenador.nombre)
    return resultado

print(entrenadores_con_tipos_especiales(entrenadores))  # Ejemplo

def promedio_nivel_pokemons(entrenador_nombre, entrenadores):
    for entrenador in entrenadores:
        if entrenador.nombre == entrenador_nombre:
            if len(entrenador.pokemons) > 0:
                return sum(pokemon.nivel for pokemon in entrenador.pokemons) / len(entrenador.pokemons)
    return 0

print(promedio_nivel_pokemons("Ash", entrenadores))  # Ejemplo

def entrenadores_con_pokemon(pokemon_nombre, entrenadores):
    return sum(1 for entrenador in entrenadores if any(pokemon.nombre == pokemon_nombre for pokemon in entrenador.pokemons))

print(entrenadores_con_pokemon("Pikachu", entrenadores))  # Ejemplo

def entrenadores_con_pokemons_repetidos(entrenadores):
    resultado = []
    for entrenador in entrenadores:
        nombres = [pokemon.nombre for pokemon in entrenador.pokemons]
        if len(nombres) > len(set(nombres)):
            resultado.append(entrenador.nombre)
    return resultado

print(entrenadores_con_pokemons_repetidos(entrenadores))  # Ejemplo

def entrenadores_con_pokemons_especificos(entrenadores, pokemons_especificos):
    return [entrenador.nombre for entrenador in entrenadores 
            if any(pokemon.nombre in pokemons_especificos for pokemon in entrenador.pokemons)]

print(entrenadores_con_pokemons_especificos(entrenadores, {"Tyrantrum", "Terrakion", "Wingull"}))  # Ejemplo

def entrenador_tiene_pokemon(entrenador_nombre, pokemon_nombre, entrenadores):
    for entrenador in entrenadores:
        if entrenador.nombre == entrenador_nombre:
            for pokemon in entrenador.pokemons:
                if pokemon.nombre == pokemon_nombre:
                    return entrenador, pokemon
    return None

entrenador, pokemon = entrenador_tiene_pokemon("Ash", "Pikachu", entrenadores)
if entrenador:
    print(f"{entrenador.nombre} tiene a {pokemon.nombre}: {pokemon}")
else:
    print("No encontrado.")
