# somadora2.py - somadora infinita - versão 2

print('Digite cada valor a somar seguido de [ENTER].')
print('Para encerrar digite 0 (zero).')
total = 0
while True:
    n = float(input(':'))
    if n == 0: break
    total = total + n
print('TOTAL: %s' % total)
