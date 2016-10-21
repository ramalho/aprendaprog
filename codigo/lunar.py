# lunar.py

# O jogo da alunissagem

# importar função sqrt do modulo math
from math import sqrt

x = 500.     # altitude em pés
v = -50.     # velocidade em pés/s
g = -5.      # aceleração gravitacional lunar em pes/s/s
t = 1.       # tempo entre jogadas em segundos
comb = 120.  # quantidade de combustível

print('Simulação de alunissagem')
print()
print('(digite a quantidade de combustível a queimar)')

fmt = 'Alt: %6.2f  Vel: %6.2f  Comb: %3d'
while x > 0:  # enquanto não tocamos o solo
    msg = fmt % (x, v, comb) # montar mensagem
    if comb > 0:  # ainda temos combustível?
        # obter quantidade de combustível a queimar
        resp = input(msg + ' Queima = ')
        try:    # converter resposta em número
            queima = float(resp)
        except: # a resposta não era um número
            queima = 0
        if queima > comb: # queimou mais do que tinha?
            queima = comb # então queima o que tem
        comb = comb - queima    # subtrai queimado
        a = g + queima    # acel = grav + queima
    else:    # sem combustível
        print(msg)   # mensagem sem perguntar
        a = g   # aceleração = gravidade
    x0 = x  # armazenar posição inicial
    v0 = v  # armazenar velocidade inicial
    x = x0 + v0*t + a*t*t/2     # calc. nova posição
    v = v0 + a*t                # calc. nova vel.
# se o loop acabou, tocamos no solo (x <= 0)
vf = sqrt(v0*v0 + 2*-a*x0)  # calcular vel. final
print('>>> CONTATO! Velocidade final: %6.2f' % (-vf))
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
print('>>>', msg)
