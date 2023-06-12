
qtdade_colunas = 5
qtdade_linhas = 5

linha = 1

while linha <= qtdade_linhas:
    coluna = 1
    while coluna <= qtdade_colunas:
        print(f'{linha=}, {coluna=}')
        coluna += 1
    linha += 1
    
print('FIM')
