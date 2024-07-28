import control as ct
import numpy as np
import matplotlib.pyplot as plt
import scienceplots

# Configurações de plot:
plt.style.use([
    'grid',
    'retro'
])
#plt.rcParams['lines.linewidth'] = 3
#plt.rcParams['font.size'] = 20
plt.rcParams['figure.figsize'] = (12, 5)

s = ct.tf('s')

G = (16.17/((s**2)+(8.421*s)+21.41))

# pade = ct.pade(0.118, 1)
# G = G*ct.tf(pade[0], pade[1])

a = 8
b = 10

Gpid = (((s+a)*(s+b))/s)

ct.root_locus(Gpid*G)
plt.show()