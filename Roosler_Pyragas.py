
# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle do Sistema de Roosler através do método de Pyragas
# /*Controle de Pyragas*/
# **************************************************************************************************************/

import numpy as np
import matplotlib.pyplot as plt

T = 0.01               # tempo de amostragem
iteracoes = 8000      # numero de iteracoes

## constantes
a = 0.2
b = 0.2
c = 5.7

## criacao das variaveis de estado
x1 = np.zeros(iteracoes)
x2 = np.zeros(iteracoes)
x3 = np.zeros(iteracoes)

u = np.zeros(iteracoes)
erro = np.zeros(iteracoes)
## condicoes iniciais
x1[0] = 4
x2[0] = 4
x3[0] = 1
tempo = np.zeros(iteracoes)

atraso = 400
K = 4
Tau = 10


for k in range(1,iteracoes):
    x1[k] = x1[k-1]-T*(x2[k-1]+x3[k-1]) + T*u[k-1]
    x2[k] = x2[k-1]+T*(x1[k-1]+a*x2[k-1])
    x3[k] = x3[k-1]+T*(b+x1[k-1]*x3[k-1]-c*x3[k-1])

    # control action
    if k > atraso:
        erro[k] = x2[k - Tau] - x2[k]
        u[k] = K * (x2[k - Tau] - x2[k]) # +1 para SETPOINT


    #tempo[k] = tempo[k-1] + T
    tempo[k] = (k - 1) * T

    if x2[k] >= -0.05 and x2[k] <= 0.05 and tempo[k] > 20 and tempo[k] < 30:
    # if x2[k] >= -0.05 and x2[k] <= 0.05:
        print('t = {}; z = {}'.format(tempo[k], x2[k]))


IAE = np.trapz(np.abs(erro), tempo, T)
print('Integral do erro: ', IAE)

## Evolucao temporal das variaveis de estado
plt.figure()
plt.plot(tempo,x1)
plt.plot(tempo,x2)
plt.plot(tempo,x3)
plt.legend(['$x1$', '$x2$','$x3$'])
plt.title('Simulação em Malha Fechada')
#plt.title('Rossler - Evolução temporal das variáveis de estado (Euler)')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


ax = plt.figure().add_subplot(projection='3d')
ax.plot(x1, x2, x3, lw=2)
plt.title('Diagrama de Fases')
plt.show()
