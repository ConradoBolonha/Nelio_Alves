### AUMENTO DE SALÁRIO ###

sal = float(input('Valor salário: '))
vl_novo_sal = ''
aumento = ''
porcent = ''

if sal <= 1000:
	vl_novo_sal = sal * 0.2 + sal
	aumento = sal * 0.2
	porcent = vl_novo_sal / sal
elif sal <= 3000:
	vl_novo_sal = sal * 0.15 + sal
	aumento = (sal * 0.15)
	porcent = (vl_novo_sal - sal) * 0.15
elif sal <= 8000:
	vl_novo_sal = sal * 0.1 + sal
	aumento = (sal * 0.1)
	porcent = (vl_novo_sal - sal) * 0.10
else:
	vl_novo_sal = sal * 0.05 + sal
	aumento = (sal * 0.05)
	porcent = (vl_novo_sal - sal) * 0.10

print(f'Novo salário = R$ {vl_novo_sal:.2f}')
print(f'Aumento = R$ {aumento:.2f}')
print(f'Porcentagem = {porcent:.0f}%')
