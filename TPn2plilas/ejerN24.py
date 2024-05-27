# Definición de la clase Stack para representar una pila
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Definición de la clase Character para representar un personaje del MCU
class Character:
    def __init__(self, name, movies_count):
        self.name = name
        self.movies_count = movies_count

    def __str__(self):
        return f"{self.name} ({self.movies_count} películas)"

# Creación de la pila de personajes del MCU
mcu_stack = Stack()

# Agregando personajes a la pila
characters = [
    Character("Iron Man", 10),
    Character("Captain America", 9),
    Character("Thor", 8),
    Character("Black Widow", 7),
    Character("Hulk", 7),
    Character("Hawkeye", 6),
    Character("Rocket Raccoon", 5),
    Character("Groot", 5),
    Character("Doctor Strange", 4),
    Character("Spider-Man", 4),
    Character("Black Panther", 4),
    Character("Star-Lord", 4),
    Character("Gamora", 4),
    Character("Drax", 4),
    Character("Scarlet Witch", 4),
    Character("Vision", 4),
    Character("Ant-Man", 4),
    Character("Wasp", 3),
    Character("Falcon", 3),
    Character("Winter Soldier", 3),
    Character("War Machine", 3),
    Character("Nick Fury", 7),
    Character("Loki", 6),
    Character("Nebula", 5),
    Character("Mantis", 3),
    Character("Shuri", 2),
    Character("Okoye", 3),
    Character("Captain Marvel", 3),
]

for character in characters:
    mcu_stack.push(character)

# Función para encontrar posiciones de personajes específicos en la pila
def find_positions(stack, names):
    temp_stack = Stack()
    positions = {name: None for name in names}
    position = 1
    
    while not stack.is_empty():
        character = stack.pop()
        if character.name in positions:
            positions[character.name] = position
        temp_stack.push(character)
        position += 1
    
    # Restaurar la pila original
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return positions

# Función para encontrar personajes que han aparecido en más de n películas
def characters_in_more_than_n_movies(stack, n):
    temp_stack = Stack()
    result = []
    
    while not stack.is_empty():
        character = stack.pop()
        if character.movies_count > n:
            result.append(character)
        temp_stack.push(character)
    
    # Restaurar la pila original
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return result

# Función para contar las películas en las que ha aparecido un personaje específico
def movies_count_for_character(stack, name):
    temp_stack = Stack()
    movies_count = None
    
    while not stack.is_empty():
        character = stack.pop()
        if character.name == name:
            movies_count = character.movies_count
        temp_stack.push(character)
    
    # Restaurar la pila original
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return movies_count

# Función para encontrar personajes cuyos nombres empiezan con letras específicas
def characters_starting_with(stack, initials):
    temp_stack = Stack()
    result = []
    
    while not stack.is_empty():
        character = stack.pop()
        if character.name[0] in initials:
            result.append(character)
        temp_stack.push(character)
    
    # Restaurar la pila original
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())
    
    return result

# Ejecución de las actividades

# a. Posiciones de Rocket Raccoon y Groot
positions = find_positions(mcu_stack, ["Rocket Raccoon", "Groot"])
print("Posiciones de Rocket Raccoon y Groot:")
for name, pos in positions.items():
    print(f"{name}: {pos}")

# b. Personajes en más de 5 películas
more_than_5_movies = characters_in_more_than_n_movies(mcu_stack, 5)
print("\nPersonajes que participaron en más de 5 películas:")
for character in more_than_5_movies:
    print(character)

# c. Películas en las que participó Black Widow
black_widow_movies = movies_count_for_character(mcu_stack, "Black Widow")
print(f"\nBlack Widow participó en {black_widow_movies} películas")

# d. Personajes cuyos nombres empiezan con C, D y G
characters_with_initials = characters_starting_with(mcu_stack, {'C', 'D', 'G'})
print("\nPersonajes cuyos nombres empiezan con C, D y G:")
for character in characters_with_initials:
    print(character)


