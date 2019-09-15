from math import *
import matplotlib.pyplot as plt
from random import random

TANGENTE_HIPERBOLICA = 1
DEGRAU = 2
LOGISTICA = 3
class Neuronio():
	def __init__(self, n, pesos, limiar):
		self.n = n
		self.pesos = pesos
		self.limiar = limiar

	def obter_saida(self, entradas,funcao, beta=1):
		potencial_de_ativacao = self.combinador_linear(entradas) - self.limiar
		return self.funcao_ativacao(potencial_de_ativacao, funcao, beta)

	def combinador_linear(self, entradas):
		retorno = 0
		for i in range(0, self.n):
			retorno += (entradas[i] * self.pesos[i])
		return retorno

	def funcao_ativacao(self, potencial_de_ativacao, funcao, beta=1):
		if funcao == TANGENTE_HIPERBOLICA:
			y = (1 - exp(-1 * beta * potencial_de_ativacao))/(1 + exp(-1 * beta * potencial_de_ativacao))
		elif funcao == DEGRAU:
			if potencial_de_ativacao >= 0:
				y = 1
			else:
				y = 0
		elif funcao == LOGISTICA:
			y = 1/(1 + exp(-1 * beta * potencial_de_ativacao))
		return y

# pesos = [0.3, 0.7]
# entradas = [0.4 , 0.5]
# limiar = 0.2
# neuronio = Neuronio(len(pesos), pesos, limiar)
# print(neuronio.obter_saida(entradas, TANGENTE_HIPERBOLICA))
itens = [
# {'pesos': [0.1], 'limiar': 0, 'funcao': LOGISTICA, 'letra': 'a'},
# {'pesos': [0.5], 'limiar': 0, 'funcao': LOGISTICA, 'letra': 'b'},
# {'pesos': [0.9], 'limiar': 0, 'funcao': LOGISTICA, 'letra': 'c'},
# {'pesos': [0.1], 'limiar': 0, 'funcao': TANGENTE_HIPERBOLICA, 'letra': 'd'},
# {'pesos': [0.5], 'limiar': 0, 'funcao': TANGENTE_HIPERBOLICA, 'letra': 'e'},
# {'pesos': [0.9], 'limiar': 0, 'funcao': TANGENTE_HIPERBOLICA, 'letra': 'f'},
# {'pesos': [0.1, 0.7], 'limiar': 0, 'funcao': LOGISTICA, 'letra': 'g'},
# {'pesos': [0.5, 0.5], 'limiar': 0, 'funcao': LOGISTICA, 'letra': 'h'},
# {'pesos': [0.7, 0.1], 'limiar': 0, 'funcao': LOGISTICA, 'letra': 'i'},
# {'pesos': [0.1, 0.7], 'limiar': 0.25, 'funcao': LOGISTICA, 'letra': 'j'},
# {'pesos': [0.5, 0.5], 'limiar': 0.25, 'funcao': LOGISTICA, 'letra': 'k'},
# {'pesos': [0.7, 0.1], 'limiar': 0.25, 'funcao': LOGISTICA, 'letra': 'l'},
{'entradas': 2, 'funcao': LOGISTICA, 'letra': '1'},
{'entradas': 2, 'funcao': TANGENTE_HIPERBOLICA, 'letra': '2'},
]
def gerarPesos(tamanho):
	lista = []
	for i in range(0, tamanho):
		lista.append(random())
	return lista
def gerarLimiar():
	return random()
limites = [0, 1]
quantidade_pontos = 20

distancia = (limites[1] - limites[0])/quantidade_pontos
pontos = []
contador = limites[1]
while contador >= limites[0]:
	pontos.append([contador])
	contador -= distancia
# print(pontos)

for item in itens:
	for j in range(0, 5):
		array_y = []
		for ponto in pontos:
			auxiliar = list(ponto)
			pesos = gerarPesos(item['entradas'])
			print(pesos)
			limiar = gerarLimiar()
			print(limiar)
			if len(pesos) > 1:
				for i in range(1, len(pesos)):
					auxiliar.append(ponto[0])
			neuronio = Neuronio(len(pesos), pesos, limiar)
			y = neuronio.obter_saida(auxiliar, item['funcao'])
			array_y.append(y)
		fig, ax = plt.subplots()
		ax.plot(pontos, array_y)	
		plt.title('Questão: ' + item['letra'] + ', iteração: ' + str(j+1) + '\n ')
		plt.show()