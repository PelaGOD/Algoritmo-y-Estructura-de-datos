from collections import deque

def es_palindromo(entrada):
    # Inicializamos una cola y una pila
    cola = deque()
    pila = []
    
    # Limpiamos la entrada quitando espacios y poniéndola en minúsculas
    entrada = ''.join(entrada.lower().split())
    
    # Agregamos los caracteres a la cola y a la pila
    for char in entrada:
        cola.append(char)
        pila.append(char)
    
    # Comparamos los elementos de la cola y la pila
    while cola:
        if cola.popleft() != pila.pop():
            return False
    
    return True

# Ejemplo de uso
cadena = "Anita lava la tina"
if es_palindromo(cadena):
    print(f'"{cadena}" es un palíndromo.')
else:
    print(f'"{cadena}" no es un palíndromo.')
