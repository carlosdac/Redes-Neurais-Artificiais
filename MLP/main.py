from random import random
from math import *
def tangente_hiperbolica(u, derivada=False, beta=1):
    if derivada:
        return 2 * ((beta * exp(-beta * u)) / (1 + exp(-beta * u)))
    else:
        return (1 - exp(-beta * u))/ (1 + exp(-beta * u))

class MLP():
    def __init__(self, camadas, entradas, funcao_ativacao, taxa_aprendizagem, precisao):
        self.camadas = camadas
        self.entradas = entradas
        self.peso_sinaptico = []
        self.potencial_ativacao = []
        self.saida = []
        self.gradiente_local = []
        self.funcao_ativacao = funcao_ativacao
        self.taxa_aprendizagem = taxa_aprendizagem
        self.precisao = precisao
        self.definir_matrizes()
        print(self.peso_sinaptico)

    def definir_matrizes(self):
        for i in range(0, len(self.camadas)):
            self.peso_sinaptico.append([])
            tamanho_camada_anterior = 0
            if i == 0:
                tamanho_camada_anterior = len(self.entradas)
            else:
                tamanho_camada_anterior = self.camadas[i - 1]
            for j in range(0, self.camadas[i]):
                pesos_neuronio = [round(random(), 2) for k in range(0, tamanho_camada_anterior)]
                self.peso_sinaptico[i].append(pesos_neuronio)
            self.potencial_ativacao.append([0 for k in range(0, self.camadas[i])])
            self.saida.append([0 for k in range(0, self.camadas[i])])
            self.gradiente_local.append([0 for k in range(0, self.camadas[i])])
    
    def eqm(self):
        pass

    def calcular_potencial(self, w, x):
        soma = 0
        print(w)
        print(x)
        for i in range(0, len(w)):
            soma += w[i] * x[i]
        return soma

    def calcular_gradiente_local(self, i, j):
        soma = 0
        for k in range(0, self.camadas[i + 1]):
            soma += self.gradiente_local[i + 1][k] * self.peso_sinaptico[i + 1][k][j]
        return soma
    def treinar(self):
        for amostra in self.entradas:
            for i in range(0, len(self.camadas)):
                #passo foward
                for j in  range(0, self.camadas[i]):
                    if i == 0:
                        entrada = amostra[0]
                    else:
                        entrada = self.saida[i - 1]
                    u = self.calcular_potencial(self.peso_sinaptico[i][j], entrada)
                    self.potencial_ativacao[i][j] = u
                    self.saida[i][j] = self.funcao_ativacao(u)
                #passo backward
            for i in range(len(self.camadas) - 1, 0, -1):
                if i == 0:
                    saida = amostra[0]
                else:
                    saida = self.saida[i - 1]
                for j in range (0, self.camadas[i]):
                    if i == len(self.camadas) - 1:
                        self.gradiente_local[i][j] = (amostra[1][j] - self.saida[i][j]) * self.funcao_ativacao(self.potencial_ativacao[i][j], derivada=True)
                    else:
                        self.gradiente_local[i][j] = self.calcular_gradiente_local(i, j) * self.funcao_ativacao(self.potencial_ativacao[i][j], derivada=True)
                    # self.gradiente_local[i][j] =  valor * self.funcao_ativacao(self.potencial_ativacao[i][j], derivada=True)
                    for k in range(0, len(self.peso_sinaptico[i][j])):
                        self.peso_sinaptico[i][j][k]  += self.taxa_aprendizagem * self.gradiente_local[i][j] * saida[k]
        print(self.peso_sinaptico)
        print(self.potencial_ativacao)
        print(self.saida)
mlp = MLP([1, 3, 2], [[[2, 2, 4, 1], [1, 2]]], tangente_hiperbolica, 0.5, 0.0001)
mlp.treinar()