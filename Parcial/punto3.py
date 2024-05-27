from Jedi import jedis


def ordenar_por_nombre_y_especie(jedis):
    jedis.sort(key = sort_key)
    for jedi in jedis:
        print(f"Nombre: {jedi['name']}")
        print(f"Especie: {jedi['species']}")
        print("-----")

def sort_key(jedi):
    return jedi['name'], jedi['species']


def mostrar_informacion(jedis, nombres):
    for jedi in jedis:
        if jedi['name'] in nombres:
            print(f"Nombre: {jedi['name']}")
            print(f"Especie: {jedi['species']}")
            print(f"Maestro: {'No tiene maestro' if jedi['master'] is None else jedi['master']}")
            print(f"Color del sable de luz: {'No tiene color' if jedi['lightsaber_color'] is None else jedi['lightsaber_color']}")
            print("-----")

def mostrar_padawans(jedis, maestros):
    for jedi in jedis:
        if jedi['master'] is not None and any(maestro in jedi['master'] for maestro in maestros):
            print(f"Nombre: {jedi['name']}")
            print(f"Maestro: {'No tiene maestro' if jedi['master'] is None else jedi['master']}")
            print("-----")

def mostrar_por_especie(jedis, especies):
    for jedi in jedis:
        if jedi['species'] in especies:
            print(f"Nombre: {jedi['name']}")
            print(f"Especie: {jedi['species']}")
            print("-----")

def listar_por_nombre(jedis, inicial):
    for jedi in jedis:
        if jedi['name'][0] == inicial:
            print(f"Nombre: {jedi['name']}")
            print("-----")

def mostrar_por_color(jedis, colores):
    for jedi in jedis:
        if jedi['lightsaber_color'] is not None and any(color in jedi['lightsaber_color'].split('/') for color in colores):
            print(f"Nombre: {jedi['name']}")
            print(f"Color del sable de luz: {'No tiene color' if jedi['lightsaber_color'] is None else jedi['lightsaber_color']}")
            print("-----")

def mostrar_por_rango(jedis, rango):
    for jedi in jedis:
        if jedi['rank'] == rango:
            print(f"Nombre: {jedi['name']}")
            print(f"Rango: {jedi['rank']}")
            print("-----")

# Ejemplo de uso
jedis_ordenados = ordenar_por_nombre_y_especie(jedis)
print("Jedis ordenados por nombre y especie:", jedis_ordenados)

info_jedis = mostrar_informacion(jedis, ["Ahsoka Tano", "Kit Fisto"])
print("Información de Ahsoka Tano y Kit Fisto:", info_jedis)

padawans = mostrar_padawans(jedis, ["Yoda", "Luke Skywalker"])
print("Padawans de Yoda y Luke Skywalker:", padawans)

jedis_por_especie = mostrar_por_especie(jedis, ["Human", "Twi'lek"])
print("Jedis de especie humana y twi'lek:", jedis_por_especie)

jedis_con_a = listar_por_nombre(jedis, 'A')
print("Jedis que comienzan con A:", jedis_con_a)

jedis_multicolor = mostrar_por_color(jedis, ["Green", "Blue"])
print("Jedis que usaron sable de luz de más de un color:", jedis_multicolor)

jedis_con_sable_amarillo_o_violeta = mostrar_por_color(jedis, ["Yellow", "Purple"])
print("Jedis que utilizaron sable de luz amarillo o violeta:", jedis_con_sable_amarillo_o_violeta)

grand_masters = mostrar_por_rango(jedis, "Grand Master")
print("Jedis que tienen el ranking de Grand Master:", grand_masters)

