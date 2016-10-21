# despdom3.py - Calculadora de despesas domesticas - versao 3

print('Balanco de despesas domesticas')
ana = float(input('Quanto gastou Ana? '))
bia = float(input('Quanto gastou Bia? '))
print()
total = ana + bia
print('Total de gastos: R$ %s' % total)
media = total/2
print('Gastos por pessoa: R$ %s' % media)
if ana < media:
    diferenca = media - ana
    print('Ana deve pagar: R$ %s' % diferenca)
elif bia < media:
    diferenca = media -  bia
    print('Bia deve pagar: R$ %s' % diferenca)
else:
    print('Ana e Bia gastaram a mesma Quantia.')
