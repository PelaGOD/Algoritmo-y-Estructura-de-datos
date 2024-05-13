


def contar_digitos(numero):
    # Caso base: si el número tiene un solo dígito
    if abs(numero) < 10:
        return 1
    # Caso recursivo: contar el dígito actual y llamar recursivamente con el resto del número
    else:
        return 1 + contar_digitos(numero // 10)

# Ejemplo de uso
numero = int(input('Ingrese numero entero: '))
cantidad_digitos = contar_digitos(numero)
print("El número", numero, "tiene", cantidad_digitos, "dígitos.")
