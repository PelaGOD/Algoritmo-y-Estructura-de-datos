def sumaSerie(num):
    if num == 1:
        return 1
    else:
        return 1 / num + sumaSerie(num - 1)


numero=int(input('Ingrese numero entero: '))
print(sumaSerie(numero))