# somadora1.py - somadora infinita - versão 1

print('Digite cada valor a somar seguido de [ENTER].')
print('Para encerrar digite 0 (zero).')
n = float(input(':'))
total = n
while n != 0:
    n = float(input(':'))
    total = total + n
print('TOTAL: %s' % total)
