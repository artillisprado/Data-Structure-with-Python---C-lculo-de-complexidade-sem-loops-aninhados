entrada  = input().replace('\n','').replace('\r','')
entrada = entrada.split()
lista = []
total = 0
cont = 0

for el in entrada:
    if el == 'loop'.upper() or el ==  'op'.upper():
        valor = entrada[cont+1]
        lista1 = el + ' ' + valor
        lista.append(lista1)
    elif el =='inicio'.upper() or el =='Fim'.upper() or el =='FimLoop'.upper():
        lista.append(el)
    cont += 1

while (int(len(lista)) > 2):
    Loop = 1
    Operacao = 0

    if 'FIMLOOP' in lista:
        valordofim = lista.index('FIMLOOP')
    else:
        valordofim = lista.index('FIM')

    for el in range(0,int(valordofim+1)):
        valor = lista[el]
        if valor != 'INICIO' and valor != 'FIMLOOP' and valor != 'FIM':    
            resultado = valor.split()
            if resultado[0] == 'LOOP':
                Loop *= int(resultado[1])
            elif Loop == 1 and 'OP' in valor:
                resultante = valor.split()
                total += int(resultante[1])
            elif resultado[0] == 'OP':
                Operacao += int(resultado[1])
        elif valor == 'FIMLOOP' or valor == 'FIM':
            total += Loop*Operacao
            while valordofim > 0:
                del lista[valordofim]
                valordofim -= 1

print(total)