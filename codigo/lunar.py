# coding: utf-8
# lunar.py

# O jogo da alunissagem

# importar funcao sqrt do modulo math
from math import sqrt

x = 500.    # altitude em pes
v = -50.    # velocidade em pes/s
g = -5. # aceleracao gravitacional lunar em pes/s/s
t = 1.  # tempo entre jogadas em segundos
comb = 120. # quantidade de combustível

print 'Simulacao de alunissagem'
print
print '(digite a quantidade de combustivel a queimar)'

fmt = 'Alt: %6.2f  Vel: %6.2f  Comb: %3d'
while x > 0:  # enquanto nao tocamos o solo
    msg = fmt % (x, v, comb) # montar mensagem
    if comb > 0:  # ainda temos combustivel?
        # obter quantidade de combustivel a queimar
        resp = raw_input(msg + ' Queima = ')
        try:    # converter resposta em numero
            queima = float(resp)
        except: # a resposta nao era um numero
            queima = 0
        if queima > comb: # queimou mais do que tinha?
            queima = comb # entao queima o que tem
        comb = comb - queima    # subtrai queimado
        a = g + queima    # acel = grav + queima
    else:    # sem combustivel
        print msg   # mensagem sem perguntar
        a = g   # aceleracao = gravidade
    x0 = x  # armazenar posicao inicial
    v0 = v  # armazenar velocidade inicial
    x = x0 + v0*t + a*t*t/2     # calc. nova posicao
    v = v0 + a*t                # calc. nova vel.
# se o loop acabou, tocamos no solo (x <= 0)
vf = sqrt(v0*v0 + 2*-a*x0)  # calcular vel. final
print '>>>CONTATO! Velocidade final: %6.2f' % (-vf)
# avaliar pouso de acordo com a velocidade final
if vf == 0:
    msg = 'Alunissagem perfeita!'
elif vf <= 2:
    msg = 'Alunissagem dentro do padrao.'
elif vf <= 10:
    msg = 'Alunissagem com avarias leves.'
elif vf <= 20:
    msg = 'Alunissagem com avarias severas.'
else:
    msg = 'Modulo lunar destruido no impacto.'
print '>>>' + msg
