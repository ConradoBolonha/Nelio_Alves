x = float(input('Valor do eixo X: '))
y = float(input('Valor do eixo Y: '))
quadrante = ''

if x >= 1 and y >= 1:
    quadrante = 'Q1'
elif y >= 1 and x <= -1:
    quadrante = 'Q2'
elif x <= -1 and y <= -1:
    quadrante = 'Q3'
elif y <= -1 and x >= 0:
    quadrante = 'Q4'
elif y == 0 and x >= 1:
    quadrante = 'Eixo X'
elif x == 0 and y >= 1:
    quadrante = 'Eixo Y'
# if x == 0 and y == 0:
else:
    quadrante = 'Origem'

print(f'{quadrante}')