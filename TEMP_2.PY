
def maior():
    n1 = int(input('1º número: '))
    n2 = int(input('2º número: '))

    if n1 == n2:
        print(f'{n1} é igual a {n2}')
    elif n1 > n2:
        print(f'{n1} é maior que {n2}')
    else:
        print(f'{n2} é maior que {n1}')
maior()