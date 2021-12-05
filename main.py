import random
import matplotlib.pyplot as plt


total_caras = 0
total_coroas = 0
total_jogos = 100
total_rodadas = 10000
vetor_texto = []
vetor_rel = []

for i in range(total_rodadas):
    for j in range(total_jogos):
        moeda = bool(random.getrandbits(1))
        if moeda == 1:
            total_caras = total_caras + 1
        else:
            total_coroas = total_coroas + 1

    vetor_texto.append(str(total_caras) + '/' + str(total_coroas))
    vetor_rel.append(total_caras/total_coroas)
    total_caras = 0
    total_coroas = 0

print(vetor_texto)
plt.hist(vetor_rel, bins = 16, rwidth = 0.95)
plt.show()