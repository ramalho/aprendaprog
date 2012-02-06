# coding: utf-8

import random

def pede_int(msg):
    while True:
        try:
            resp = raw_input(msg)
            resp = int(resp)
        except:
            print 'Digite apenas dígitos'
        else:
            break
    return resp

# programa principal

print 'Chute um número de 1 a 10:'

nosso_numero = random.randint(1, 10)
tentativas = 4

while tentativas > 0:
    resp = pede_int(':')
    if resp == nosso_numero:
        print 'Acertou!'
        break
    elif resp > nosso_numero:
        print 'Muito alto...'
    else:
        print 'Muito baixo...'
    tentativas = tentativas - 1 
else:
    print 'Game over'
