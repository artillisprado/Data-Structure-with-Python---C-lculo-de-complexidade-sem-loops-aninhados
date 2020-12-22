lista = []

consulta = int(input())

for el in range(0,consulta):
    perg = input().split()
    valor = (perg[0], perg[1], perg[2])
    lista.append(valor)

for el in lista:
    a = int(el[0])
    b = int(el[1])
    limite = int(el[2])
    resultado = a*b
    if resultado <= limite:
        print(resultado)
    else:
        print(f'multiplication of {a} and {b} with bound {limite} not possible')
