def soma(*numeros):
    total = 0
    for num in numeros:
        total += num
    print("A soma dos numeros é: %d" % total)

lista = [3,5,6,7,3,3,6,7]
soma(*lista)