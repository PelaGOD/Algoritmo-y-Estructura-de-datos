class Superheroe:
    def __init__(self, nombre, ano_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.ano_aparicion = ano_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

    def __repr__(self):
        return f"Superheroe({self.nombre}, {self.ano_aparicion}, {self.casa_comic}, {self.biografia})"

# Lista de superhéroes
superheroes = [
    Superheroe("Linterna Verde", 1940, "DC", "Porta un anillo de poder."),
    Superheroe("Wolverine", 1974, "Marvel", "Tiene un traje amarillo y negro."),
    Superheroe("Dr. Strange", 1963, "DC", "El Hechicero Supremo."),
    Superheroe("Capitana Marvel", 1968, "Marvel", "Usa una armadura especial."),
    Superheroe("Mujer Maravilla", 1941, "DC", "Amazonas con traje de batalla."),
    Superheroe("Flash", 1940, "DC", "El hombre más rápido."),
    Superheroe("Star-Lord", 1976, "Marvel", "Guardián del cosmos con traje especial."),
]

def eliminar_superheroe(nombre, lista):
    lista[:] = [superheroe for superheroe in lista if superheroe.nombre != nombre]

def mostrar_ano_aparicion(nombre, lista):
    for superheroe in lista:
        if superheroe.nombre == nombre:
            return superheroe.ano_aparicion

def cambiar_casa(nombre, nueva_casa, lista):
    for superheroe in lista:
        if superheroe.nombre == nombre:
            superheroe.casa_comic = nueva_casa

def superheroes_con_traje_o_armadura(lista):
    return [superheroe.nombre for superheroe in lista if "traje" in superheroe.biografia or "armadura" in superheroe.biografia]

def superheroes_antes_de(ano, lista):
    return [(superheroe.nombre, superheroe.casa_comic) for superheroe in lista if superheroe.ano_aparicion < ano]

def mostrar_casa(nombres, lista):
    return {superheroe.nombre: superheroe.casa_comic for superheroe in lista if superheroe.nombre in nombres}

def mostrar_informacion(nombres, lista):
    return [superheroe for superheroe in lista if superheroe.nombre in nombres]

def superheroes_por_letra(letras, lista):
    return [superheroe.nombre for superheroe in lista if superheroe.nombre[0] in letras]

def contar_por_casa(lista):
    conteo = {}
    for superheroe in lista:
        if superheroe.casa_comic in conteo:
            conteo[superheroe.casa_comic] += 1
        else:
            conteo[superheroe.casa_comic] = 1
    return conteo

# Realizar las tareas solicitadas
eliminar_superheroe("Linterna Verde", superheroes)
print(mostrar_ano_aparicion("Wolverine", superheroes))
cambiar_casa("Dr. Strange", "Marvel", superheroes)
print(superheroes_con_traje_o_armadura(superheroes))
print(superheroes_antes_de(1963, superheroes))
print(mostrar_casa(["Capitana Marvel", "Mujer Maravilla"], superheroes))
print(mostrar_informacion(["Flash", "Star-Lord"], superheroes))
print(superheroes_por_letra("BMS", superheroes))
print(contar_por_casa(superheroes))
