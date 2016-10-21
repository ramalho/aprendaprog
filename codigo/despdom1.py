# despdom1.py - Calculadora de despesas domesticas

print('Balanco de despesas domesticas')
ana = input('Quanto gastou Ana? ')
bia = input('Quanto gastou Bia? ')
total = float(ana) + float(bia)
print('Total de gastos = R$ %s.' % total)
media = total/2
print('Gastos por pessoa = R$ %s.' % media)
