# somadora4.py - somadora infinita - versão 4

print('Digite cada valor a somar seguido de [ENTER].')
print('Para encerrar apenas [ENTER].')
total = 0
while True:
    try:
        linha = input(':')
        n = float(linha)
        total = total + n
    except ValueError:
        if len(linha) == 0:
             break
        elif ',' in linha:
             print('Use o . (ponto) como separador decimal.')
        else:
             print('Isso não parece um número válido.')
print('TOTAL: %s' % total)
