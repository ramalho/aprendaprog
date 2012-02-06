# somadora4.py - somadora infinita - versao 4

print 'Digite os valores a somar seguidos de .'
print 'Para encerrar apenas .'
total = 0
while True:
    try:
        linha = raw_input(':')
        n = float(linha)
        total = total + n
    except:
        if len(linha) == 0:
             break
        elif ',' in linha:
             print 'Use o . (ponto) como separador decimal.'
        else:
             print 'Isso nao parece um numero valido.'
print 'TOTAL: %s' % total
