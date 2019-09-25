from sklearn.cluster import KMeans
import numpy as np
from copy import deepcopy
import seaborn as sb
import matplotlib.pyplot as plt
from random import randint
from math import *
import xlrd
# amostras = [
#     [0.1990, 0.9442],
#     [0.6743, 0.8386],
#     [0.9271, 0.2584],
#     [0.3438, 0.0429],
#     [0.5945, 0.0059],
#     [0.6155, 0.5744],
#     [0.0034, 0.7439],
#     [0.9820, 0.8068],
#     [0.8995, 0.6376],
#     [0.6928, 0.2513],
#     [0.4397, 0.1443],
#     [0.7010, 0.6516],
#     [0.6097, 0.9461],
#     [0.2999, 0.8159],
#     [0.8560, 0.9302],
#     [0.1121, 0.3099],
#     [0.2916, 0.2688],
#     [0.0974, 0.5365],
#     [0.3974, 0.1633],
#     [0.3333, 0.2110]
# ]
amostras = []
def ler_amostras():
	xls = xlrd.open_workbook("Amostras2.xls")
	plan = xls.sheets()[0]
	for i in range(0, plan.nrows):
		linha = plan.row_values(i)
		amostras.append(linha)

ler_amostras()
print(amostras)
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(amostras)
print(kmeans.labels_)
def distancia_euclidiana(ponto1, ponto2):
	distancia = 0
	for i in range(0, len(ponto1)):
		distancia += ((ponto1[i] - ponto2[i]) ** 2)
	return distancia
def calcular_centro(grupo):
	x = 0
	y = 0
	for ponto in grupo:
		x += ponto[0]
		y += ponto[1]
	x /= len(grupo)
	y /= len(grupo)
	return [x, y]	
for k in range(5):
	GRUPOS = 2
	centros = [amostras[randint(0, len(amostras) - 1)] for i in range(GRUPOS)]
	grupos = [[] for i in range(GRUPOS)]
	contador = 1
	erros  = []
	contadores = []
	while True:
		grupos_anterior = deepcopy(grupos)
		erro = 0
		for amostra in amostras:
			menor_distancia = inf
			for j in range(GRUPOS):
				distancia = distancia_euclidiana(centros[j], amostra)
				if  distancia < menor_distancia:
					menor_distancia = distancia
					indice = j
			
			if amostra in grupos[0]:
				grupos[0].remove(amostra)
			elif amostra in grupos[1]:
				grupos[1].remove(amostra)
			erro += menor_distancia
			grupos[indice].append(amostra)
			centros[indice] = calcular_centro(grupos[indice])
		erros.append(erro)
		contadores.append(contador)
		#verificacao = (grupos_anterior == np.array(grupos)).sum(1)
		#print(verificacao)
		if grupos_anterior == grupos and contador >= 10:
			plt.plot(contadores, erros)
			plt.title("Erro")
			plt.savefig('questao2_erro' + str(k) + '.png')
			plt.show()
			print("Algoritmo convergiu em " + str(contador) + " iterações.")
			break
		contador += 1
	grupo_0x = []
	grupo_0y = []

	grupo_1x = []
	grupo_1y = []

	for i in range(len(grupos)):
		for pontos in grupos[i]:
			if i == 0:
				grupo_0x.append(pontos[0])
				grupo_0y.append(pontos[1])
			if i == 1:
				grupo_1x.append(pontos[0])
				grupo_1y.append(pontos[1])
	
	plt.scatter(grupo_0x, grupo_0y, s=10, label="Grupo 0")
	plt.scatter([centros[0][0]], [centros[0][1]], s=10, label="Centro Grupo 0")
	plt.scatter([centros[1][0]], [centros[1][1]], s=10, label="Centro Grupo 1")
	plt.scatter(grupo_1x, grupo_1y, s=10, label="Grupo 1")
	plt.title("Grupos")
	plt.legend()
	plt.savefig('questao2_grupos' + str(k)+'.png')
	plt.show()
string = '['		
for amostra in amostras:
	if amostra in grupos[0]:
		string += '0 '
	elif amostra in grupos[1]:
		string += '1 '
print(string[0:len(string) -1] + ']')