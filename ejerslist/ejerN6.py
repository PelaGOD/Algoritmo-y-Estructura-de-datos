class Superheroe:
    def __init__(self, nombre, año_aparicion, casa_comic, biografia):
        self.nombre = nombre
        self.año_aparicion = año_aparicion
        self.casa_comic = casa_comic
        self.biografia = biografia

class Nodo:
    def __init__(self, superheroe=None):
        self.superheroe = superheroe
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, superheroe):
        nuevo_nodo = Nodo(superheroe)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def eliminar(self, nombre):
        actual = self.cabeza
        previo = None
        while actual and actual.superheroe.nombre != nombre:
            previo = actual
            actual = actual.siguiente
        if actual is None:
            return False
        if previo is None:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        return True
    
    def buscar(self, nombre):
        actual = self.cabeza
        while actual and actual.superheroe.nombre != nombre:
            actual = actual.siguiente
        return actual.superheroe if actual else None
    
    def mostrar(self, condicion=None):
        resultado = []
        actual = self.cabeza
        while actual:
            if not condicion or condicion(actual.superheroe):
                resultado.append(actual.superheroe)
            actual = actual.siguiente
        return resultado
    
    def contar_por_casa(self):
        conteo = {'Marvel': 0, 'DC': 0}
        actual = self.cabeza
        while actual:
            if actual.superheroe.casa_comic in conteo:
                conteo[actual.superheroe.casa_comic] += 1
            actual = actual.siguiente
        return conteo

def eliminar_linterna_verde(lista):
    return lista.eliminar("Linterna Verde")

def año_aparicion_wolverine(lista):
    superheroe = lista.buscar("Wolverine")
    return superheroe.año_aparicion if superheroe else None

def cambiar_casa_dr_strange(lista):
    superheroe = lista.buscar("Dr. Strange")
    if superheroe:
        superheroe.casa_comic = "Marvel"

def superheroe_con_traje_armadura(lista):
    return [s.nombre for s in lista.mostrar(lambda s: "traje" in s.biografia.lower() or "armadura" in s.biografia.lower())]

def superheroe_antes_de_1963(lista):
    return [(s.nombre, s.casa_comic) for s in lista.mostrar(lambda s: s.año_aparicion < 1963)]

def casa_capitana_marvel_mujer_maravilla(lista):
    capitana_marvel = lista.buscar("Capitana Marvel")
    mujer_maravilla = lista.buscar("Mujer Maravilla")
    return {
        "Capitana Marvel": capitana_marvel.casa_comic if capitana_marvel else None,
        "Mujer Maravilla": mujer_maravilla.casa_comic if mujer_maravilla else None
    }

def info_flash_star_lord(lista):
    flash = lista.buscar("Flash")
    star_lord = lista.buscar("Star-Lord")
    return {
        "Flash": vars(flash) if flash else None,
        "Star-Lord": vars(star_lord) if star_lord else None
    }

def superheroe_por_letra(lista):
    letras = ['B', 'M', 'S']
    return [s.nombre for s in lista.mostrar(lambda s: s.nombre[0] in letras)]

def conteo_por_casa(lista):
    return lista.contar_por_casa()

# Crear la lista enlazada de superhéroes
lista_superheroes = ListaEnlazada()

# Agregar algunos superhéroes
lista_superheroes.agregar(Superheroe("Linterna Verde", 1940, "DC", "Usa un anillo de poder."))
lista_superheroes.agregar(Superheroe("Wolverine", 1974, "Marvel", "Tiene garras retráctiles y factor de curación."))
lista_superheroes.agregar(Superheroe("Dr. Strange", 1963, "DC", "Es un hechicero supremo."))
lista_superheroes.agregar(Superheroe("Capitana Marvel", 1968, "Marvel", "Tiene super fuerza y puede volar."))
lista_superheroes.agregar(Superheroe("Mujer Maravilla", 1941, "DC", "Es una guerrera amazona."))
lista_superheroes.agregar(Superheroe("Flash", 1940, "DC", "Es el hombre más rápido del mundo."))
lista_superheroes.agregar(Superheroe("Star-Lord", 1976, "Marvel", "Lidera a los Guardianes de la Galaxia."))

# Llamar las funciones implementadas
print(eliminar_linterna_verde(lista_superheroes))
print(año_aparicion_wolverine(lista_superheroes))
cambiar_casa_dr_strange(lista_superheroes)
print(superheroe_con_traje_armadura(lista_superheroes))
print(superheroe_antes_de_1963(lista_superheroes))
print(casa_capitana_marvel_mujer_maravilla(lista_superheroes))
print(info_flash_star_lord(lista_superheroes))
print(superheroe_por_letra(lista_superheroes))
print(conteo_por_casa(lista_superheroes))
