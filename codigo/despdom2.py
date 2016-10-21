# despdom2.py - Calculadora de despesas domesticas - versao 2

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
    print('Ana deve pagar: R$ %s' %diferenca)
else:
    diferenca = media - bia
    print('Bia deve pagar: R$ %s' % diferenca)
