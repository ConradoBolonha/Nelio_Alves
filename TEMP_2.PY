
# from math import factorial

# num = int(input('Digite um número: '))
# print(f'O fatorial de {num} é {factorial(num)}')


num = int(input('Digite um número: '))
c = num
fatorial = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end=' ')
    fatorial *= c
    c -= 1
print(f'O fatorial de {num}! é {fatorial}')
