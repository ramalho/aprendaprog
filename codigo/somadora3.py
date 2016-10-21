# somadora3.py - somadora infinita - versão 3

print('Digite cada valor a somar seguido de [ENTER].')
print('Para encerrar apenas [ENTER].')
total = 0
while True:
    try:
        n = float(input(':'))
        total = total + n
    except ValueError:
        break
print('TOTAL: %s' % total)
