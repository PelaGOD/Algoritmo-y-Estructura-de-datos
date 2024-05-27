def invertir_lista(lista):
    if len(lista) < 2:
        return lista
    else:
        return [lista[-1]] + invertir_lista(lista[:-1])


mi_lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
print(invertir_lista(mi_lista))
