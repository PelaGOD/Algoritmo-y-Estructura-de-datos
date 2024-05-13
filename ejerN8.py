def convert_to_binary(numero):
    if numero <= 1:
        return str(numero)
    else:
        return convert_to_binary(numero//2)+ str(numero % 2)
    

num=int(input('Ingrese numero: '))

print(convert_to_binary(num))