### AUMENTO DE SALÁRIO ###

sal = float(input('Valor salário: '))
vl_novo_sal = ''
aumento = ''
porcent = ''

if sal <= 1000:
	vl_novo_sal = sal * 0.2 + sal
	aumento = sal * 0.2
	porcent = 0.20 * 100
elif sal <= 3000:
	vl_novo_sal = sal * 0.15 + sal
	aumento = sal * 0.15
	porcent = 0.15 * 100
elif sal <= 8000:
	vl_novo_sal = sal * 0.1 + sal
	aumento = sal * 0.1
	porcent = 0.10 * 100
else:
	vl_novo_sal = sal * 0.05 + sal
	aumento = sal * 0.05
	porcent = 0.05 * 100

print(f'Valor salário atual = R$ {sal:.2f}')
print(f'Valor do aumento = R$ {aumento:.2f}')
print(f'Valor do novo salário = R$ {vl_novo_sal:.2f}')
print(f'% de aumento = {porcent:.0f}%')
