
distancia = []

for cont in range(1, 4):
    lancamento = float(input(f'Digite a {cont}ª distância: '))
    distancia.append(lancamento)
print(f'A maior distância foi {max(distancia)}')
