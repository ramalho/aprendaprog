# somadora3.py - somadora infinita - versao 3

print 'Digite os valores a somar seguidos de [ENTER].'
print 'Para encerrar apenas [ENTER].'
total = 0
while True:
    try:
        n = float(raw_input(':'))
        total = total + n
    except:
        break
print 'TOTAL: %s' % total

  # somadora3.py - somadora infinita - versao 3

  print 'Digite os valores a somar seguidos de [ENTER].'
  print 'Para encerrar apenas [ENTER].'
  total = 0
  while True:
      try:
          n = float(raw_input(':'))
          total = total + n
      except:
          break
  print 'TOTAL: %s' % total
