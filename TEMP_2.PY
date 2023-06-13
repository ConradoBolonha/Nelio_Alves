n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0

while opcao != 5:
    print('''\n[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa''')
    opcao = int(input('\n>>>> Esolha uma opção: '))
    print()
    if opcao == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif opcao == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        else:
            print(f'{n2} é maior que {n1}')
    elif opcao == 4:
        print('Informe novos números.')
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:
        print('Opção inválida. Tente novamente!')
print('Fim do programa')
