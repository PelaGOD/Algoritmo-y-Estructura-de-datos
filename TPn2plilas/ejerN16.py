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

# Función para obtener la intersección de dos pilas
def intersect_stacks(stack1, stack2):
    temp_stack1 = Stack()
    temp_stack2 = Stack()
    intersection = Stack()
    items_stack2 = set()

    # Pasar elementos de stack2 a un conjunto para una búsqueda rápida
    while not stack2.is_empty():
        item = stack2.pop()
        items_stack2.add(item)
        temp_stack2.push(item)

    # Restaurar stack2
    while not temp_stack2.is_empty():
        stack2.push(temp_stack2.pop())

    # Encontrar elementos comunes entre stack1 y stack2
    while not stack1.is_empty():
        item = stack1.pop()
        if item in items_stack2:
            intersection.push(item)
        temp_stack1.push(item)

    # Restaurar stack1
    while not temp_stack1.is_empty():
        stack1.push(temp_stack1.pop())

    return intersection

# Crear las pilas de personajes para los episodios V y VII
stack_episode_v = Stack()
stack_episode_vii = Stack()

# Agregar personajes del episodio V a la pila correspondiente
characters_episode_v = ["Luke Skywalker", "Darth Vader", "Han Solo", "Leia Organa", "Chewbacca", "Yoda", "Boba Fett"]
for character in characters_episode_v:
    stack_episode_v.push(character)

# Agregar personajes del episodio VII a la pila correspondiente
characters_episode_vii = ["Luke Skywalker", "Han Solo", "Leia Organa", "Chewbacca", "Rey", "Finn", "Kylo Ren", "Poe Dameron"]
for character in characters_episode_vii:
    stack_episode_vii.push(character)

# Obtener la intersección de las dos pilas
intersection_stack = intersect_stacks(stack_episode_v, stack_episode_vii)

# Mostrar los personajes que aparecen en ambos episodios
print("Personajes que aparecen en ambos episodios V y VII:")
while not intersection_stack.is_empty():
    print(intersection_stack.pop())

