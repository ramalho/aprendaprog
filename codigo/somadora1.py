# somadora1.py - somadora infinita - versao 1

print 'Digite os valores a somar seguidos de [ENTER].'
print 'Para encerrar digite zero: 0'
n = float(raw_input(':'))
total = n
while n != 0:
    n = float(raw_input(':'))
    total = total + n
print 'TOTAL: %s' % total
