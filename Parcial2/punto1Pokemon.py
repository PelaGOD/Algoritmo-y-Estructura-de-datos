class Pokemon:
    def __init__(self, number, name, types):
        self.number = number
        self.name = name
        self.types = types  # Lista de tipos (puede tener más de un tipo)

    def __repr__(self):
        return f"Pokemon(number={self.number}, name='{self.name}', types={self.types})"


class BSTNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = BSTNode(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key, data)
            else:
                self._insert_recursive(node.left, key, data)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key, data)
            else:
                self._insert_recursive(node.right, key, data)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def in_order(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left is not None:
            self.in_order(node.left, result)
        result.append(node.data)
        if node.right is not None:
            self.in_order(node.right, result)
        return result

    def level_order(self):
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result


# Creación de los arboles
nombre_tree = BST()
numero_tree = BST()
tipo_dict = {}  

# ejemplo de Pokémon
pokemons = [
    Pokemon(25, 'Pikachu', ['Electric']),
    Pokemon(6, 'Charizard', ['Fire', 'Flying']),
    Pokemon(1, 'Bulbasaur', ['Grass', 'Poison']),
    Pokemon(133, 'Eevee', ['Normal']),
    Pokemon(135, 'Jolteon', ['Electric']),
    Pokemon(745, 'Lycanroc', ['Rock']),
    Pokemon(697, 'Tyrantrum', ['Rock', 'Dragon']),
    Pokemon(3, 'Squirtle', ['Water'])
]

# Insertar cada Pokémon en los arboles y diccionarios
for p in pokemons:
    nombre_tree.insert(p.name, p)  # Ordenado por nombre
    numero_tree.insert(p.number, p)  # Ordenado por número
    for tipo in p.types:
        if tipo not in tipo_dict:
            tipo_dict[tipo] = []
        tipo_dict[tipo].append(p)


# Funciones 

# b) Buscada parcial
def buscar_pokemon_por_nombre_parcial(tree, partial_name):
    result = []
    for pokemon in tree.in_order():
        if partial_name.lower() in pokemon.name.lower():
            result.append(pokemon)
    return result


def buscar_pokemon_por_numero(tree, number):
    return tree.search(number)


# c) Mostrar todos los nombres de un tipo específico
def mostrar_nombres_por_tipo(tipo_dict, tipo):
    return [pokemon.name for pokemon in tipo_dict.get(tipo, [])]


# d) Listado en orden ascendente por número y por nombre, y por nivel (orden de anchura)
def listado_ascendente_por_numero(tree):
    return sorted(tree.in_order(), key=lambda p: p.number)


def listado_ascendente_por_nombre(tree):
    return sorted(tree.in_order(), key=lambda p: p.name)


def listado_por_nivel(tree):
    return tree.level_order()


# e) Mostrar todos los datos de Pokémon específicos
def mostrar_datos_especificos(tree, nombres):
    result = []
    for nombre in nombres:
        pokemon = tree.search(nombre)
        if pokemon:
            result.append(pokemon)
    return result


# f) Contar Pokémon de tipos específicos
def contar_pokemons_por_tipo(tipo_dict, tipo):
    return len(tipo_dict.get(tipo, []))


# Ejemplo de uso de cada punto:

# Punto b: Buscar por nombre parcial y por número
print("Búsqueda por nombre parcial 'bul':", buscar_pokemon_por_nombre_parcial(nombre_tree, 'bul'))
print("Búsqueda por número 25:", buscar_pokemon_por_numero(numero_tree, 25))

# Punto c: Nombres de Pokémon de tipo Electric
print("Nombres de tipo Electric:", mostrar_nombres_por_tipo(tipo_dict, 'Electric'))

# Punto d: Listado en orden ascendente y por nivel
print("Listado por número:", listado_ascendente_por_numero(numero_tree))
print("Listado por nombre:", listado_ascendente_por_nombre(nombre_tree))
print("Listado por nivel (orden de anchura):", listado_por_nivel(nombre_tree))

# Punto e: Mostrar datos de Pokémon específicos
print("Datos de Jolteon, Lycanroc y Tyrantrum:", mostrar_datos_especificos(nombre_tree, ['Jolteon', 'Lycanroc', 'Tyrantrum']))

# Punto f: Contar Pokémon de tipo Eléctrico y Acero
print("Cantidad de tipo Eléctrico:", contar_pokemons_por_tipo(tipo_dict, 'Electric'))
print("Cantidad de tipo Acero:", contar_pokemons_por_tipo(tipo_dict, 'Steel'))

