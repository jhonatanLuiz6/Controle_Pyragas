
# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle Sistema de Lorenz através do método de Pyragas
# /*Controle de Pyragas*/
# **************************************************************************************************************/

import numpy as np
import matplotlib.pyplot as plt

# declarações de variaveis

n = 2000  # número de iterações
T = 0.01  # tempo de amostragem
tempo = np.zeros(n)

x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)

u = np.zeros(n)
erro = np.zeros(n)

# constantes da equação de lorenz
s = 10
b = 8 / 3
p = 28

# condições iniciais
x[0] = 0.1
y[0] = 0.2
z[0] = 0.3

# control parameters
atraso = 5
Tau = 5
K = 20

# evolução do sistema
for k in range(n-1):
#k = 1
#while k < n:
    k = k + 1

    x[k] = (-s * T + 1) * x[k - 1] + (s * T) * y[k - 1]
    y[k] = p * T * x[k - 1] + (-T + 1) * y[k - 1] - T * x[k - 1] * z[k - 1] + T*u[k-1]
    z[k] = T * x[k - 1] * y[k - 1] + (-b * T + 1) * z[k - 1]

    # control action
    if k > atraso:
        erro[k] = y[k - Tau] - y[k]
        u[k] = K * (y[k - Tau] - y[k])

    tempo[k] = (k - 1) * T

    if z[k] >= 25.65 and z[k] <= 28.35 and tempo[k] > 8 and tempo[k] < 12:
    #if z[k] >= 28.35 or z[k] <= 25.65:
        print('t = {}; z = {}'.format(tempo[k], z[k]))



IAE = np.trapz(np.abs(erro), tempo, T)
print('Integral do erro: ', IAE)

# Plotagem das respostas sobrepostas

plt.plot(tempo, x, color='r', lw=2, label='x');
plt.plot(tempo, y, color='b', lw=2, label='y');
plt.plot(tempo, z, color='g', lw=2, label='z');
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Controle através do método DFC')
plt.legend()
plt.show()

# plotar ação de controle
plt.plot(tempo, u, color='r', lw=2, label='ação de controle');
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('ação de Controle do método DFC')
plt.legend()
plt.show()


ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, z, lw=2)
plt.title('Diagrama de Fases')
plt.show()

print('x = ', x[n-1])
print('y = ', y[n-1])
print('z = ', z[n-1])
