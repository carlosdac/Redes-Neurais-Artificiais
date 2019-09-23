from sklearn.cluster import KMeans
import seaborn as sb
from random import randint
from math import *
amostras = [
    [0.1990, 0.9442],
    [0.6743, 0.8386],
    [0.9271, 0.2584],
    [0.3438, 0.0429],
    [0.5945, 0.0059],
    [0.6155, 0.5744],
    [0.0034, 0.7439],
    [0.9820, 0.8068],
    [0.8995, 0.6376],
    [0.6928, 0.2513],
    [0.4397, 0.1443],
    [0.7010, 0.6516],
    [0.6097, 0.9461],
    [0.2999, 0.8159],
    [0.8560, 0.9302],
    [0.1121, 0.3099],
    [0.2916, 0.2688],
    [0.0974, 0.5365],
    [0.3974, 0.1633],
    [0.3333, 0.2110]
]

kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(amostras)
print(kmeans.labels_)
def distancia_euclidiana(ponto1, ponto2):
	distancia = 0
	for i in range(0, len(ponto1)):
		distancia += ((ponto1[i] - ponto2[i]) ** 2)
	return sqrt(distancia)
def calcular_centro(grupo):
	x = 0
	y = 0
	for ponto in grupo:
		x += ponto[0]
		y += ponto[1]
	x /= len(grupo)
	y /= len(grupo)
	return [x, y]	
for i in range(1):
	GRUPOS = 2
	centros = [amostras[randint(0, len(amostras) - 1)] for i in range(GRUPOS)]
	grupos = [[] for i in range(GRUPOS)]
	for amostra in amostras:
		menor_distancia = inf
		for j in range(GRUPOS):
			if distancia_euclidiana(centros[j], amostra) < menor_distancia:
				menor_distancia = distancia_euclidiana(centros[j], amostra)
				indice = j
		grupos[indice].append(amostra)
		centros[indice] = calcular_centro(grupos[indice])
