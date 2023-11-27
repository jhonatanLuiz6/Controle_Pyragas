
# ***************************************************************************************************************/
# Eng. Controle e Automação */
# Autor: Jhonatan Luiz Souza Siqueira */
# Centro Federal de Educação e Tecnologia (CEFET-MG) */
# Monografia de Graduação */
# Controle de Sistemas Caoticos Utilizando Logica Fuzzy na Otimização do Método de Espaço de Estados Defasados*/
# Orientador: Marlon José do Carmo */
# **
# Simulação do controle do Mapa Logístico através do método de Pyragas
# /*Controle de Pyragas*/
# **************************************************************************************************************/

import numpy as np
import matplotlib.pyplot as plt

iteracoes = 100     # numero de iteracoes

# constantes
mi = 3.8   # número Malthusiano ( entre 3.56995 e 4 apresenta comportamento caotico)

# criacao das variaveis de estado
x = np.zeros(iteracoes)
n = np.zeros(iteracoes)

u = np.zeros(iteracoes)

# condicoes iniciais
x[0] = 0.2
n[0] = 0

# control parameters
atraso = 3
Tau = 1
K = -0.6

for k in range(1,iteracoes):
    x[k] = mi*x[k-1]*(1-x[k-1]) + u[k-1]
    n[k] = k+1

    # control action
    if k > atraso:
        u[k] = K * (x[k- Tau] - x[k])

print(x[49])
## grafico
plt.figure()
plt.plot(n,x,color='b', lw=2, label='x')
##plt.xlim([0, 100])
##plt.ylim([0, 0.9])
plt.xlabel('Iterações')
plt.ylabel('x')
plt.title('Mapa logístico')
plt.legend()
plt.grid(True)
plt.show()
