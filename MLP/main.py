from random import random
from math import *
def tangente_hiperbolica(u, derivada=False, beta=1):
    if derivada:
        return 2 * ((beta * exp(-beta * u)) / (1 + exp(-beta * u)))
    else:
        return (1 - exp(-beta * u))/ (1 + exp(-beta * u))

def logistica(u, derivada=False, beta=1):
    if derivada:
        return ((beta * exp(-beta * u)) / pow((1 + exp(-beta * u)), 2))
    else:
        return 1 / (1 + exp(-beta * u))

def linear(u, derivada=False):
    if derivada:
        return 1
    else:
        return u

class MLP():
    def __init__(self, camadas, entradas, funcao_ativacao, taxa_aprendizagem, precisao):
        self.camadas = camadas
        self.entradas = entradas
        self.peso_sinaptico = []
        self.potencial_ativacao = []
        self.saida = []
        self.gradiente_local = []
        self.epocas = 0
        self.funcao_ativacao = funcao_ativacao
        self.taxa_aprendizagem = taxa_aprendizagem
        self.precisao = precisao
        self.entradas_limiar_ativacao()
        self.definir_matrizes()

    def entradas_limiar_ativacao(self):
        for amostra in self.entradas:
            amostra[0].insert(0, -1)
            amostra[1].insert(0, 0)

    def definir_matrizes(self):
        for i in range(0, len(self.camadas)):
            self.peso_sinaptico.append([])
            tamanho_camada_anterior = 0
            if(i == len(self.camadas) - 1):
                tamanho_saida = self.camadas[i]
            else:
                tamanho_saida = self.camadas[i] + 1
            if i == 0:
                tamanho_camada_anterior = len(self.entradas[0][0])
            else:
                tamanho_camada_anterior = self.camadas[i - 1] + 1
            # for j in range(0, self.camadas[i] + 1):
            #     pesos_neuronio = [[[0.2, -0.1, -0.3], [-0.5, -0.8, 0.4], [-0.1, 0.1, 0.6]], [[0.1, 0.5, -0.3, 0.1], [0.3, 0.2, 0.6, -0.9]]]#[round(random(), 2) for k in range(0, tamanho_camada_anterior)]
            #     if j == 0:
            #         pesos_neuronio = []
            #     self.peso_sinaptico[i].append(pesos_neuronio)
            self.peso_sinaptico = [[[], [0.2, -0.1, 0.3], [-0.5, -0.8, 0.4], [-0.1, 0.1, -0.6]], [[], [0.1, 0.5, -0.3, 0.1], [0.3, 0.2, 0.6, -0.9]]]
            self.potencial_ativacao.append([0 for k in range(0, self.camadas[i] + 1)])
            saida = []
            for k in range(0, self.camadas[i] + 1):
                saida.append(-1)
            self.saida.append(saida)
            self.gradiente_local.append([0 for k in range(0, self.camadas[i] + 1)])
    def eqm(self):
        soma = [0 for i in range(0, (len(self.entradas)))]
        for j in range(0, len(self.entradas)):
            for i in range(1, len(self.saida[len(self.saida) - 1])):
                soma[j] += pow((self.entradas[j][1][i] - self.saida[len(self.saida) - 1][i]), 2)
                print("d(k) = " + str(round(self.entradas[j][1][i], 6)) + " ; y = " + str(round(self.saida[len(self.saida) - 1][i], 6)))
            soma[j] /= len(self.saida[len(self.saida) - 1]) - 1 
        soma_final = 0
        for valor in soma:
            soma_final += valor
        soma_final /= len(self.entradas)
        return soma_final

    def calcular_potencial(self, w, x):
        soma = 0
        for i in range(0, len(w)):
            soma += w[i] * x[i]
        return soma

    def calcular_gradiente_local(self, i, j):
        soma = 0
        for k in range(1, self.camadas[i + 1] + 1):
            soma += self.gradiente_local[i + 1][k] * self.peso_sinaptico[i + 1][k][j]
        return soma
    def treinar(self):
        while(True):
            EQM_ANTERIOR = round(self.eqm(), 6)
            for amostra in self.entradas:
                for i in range(0, len(self.camadas)):
                    #passo foward
                    for j in  range(1, self.camadas[i] + 1):
                        if i == 0:
                            entrada = amostra[0]
                        else:
                            entrada = self.saida[i - 1]
                        u = self.calcular_potencial(self.peso_sinaptico[i][j], entrada)
                        self.potencial_ativacao[i][j] = round(u,6)
                        self.saida[i][j] = round(self.funcao_ativacao[i](u), 6)
                    #passo backward
                    print("Potencial de ativação camada " + str(i) + ": " + str(self.potencial_ativacao[i]))
                    print(self.peso_sinaptico[i][j])
                    print(entrada)
                    print("Saída: " + str(self.saida[i]))
                    input('')
                for i in range(len(self.camadas) - 1, -1, -1):
                    if i == 0:
                        saida = amostra[0]
                    else:
                        saida = self.saida[i - 1]
                    for j in range (1, self.camadas[i] + 1):
                        if i == len(self.camadas) - 1:
                            self.gradiente_local[i][j] = round((amostra[1][j] - self.saida[i][j]) * self.funcao_ativacao[i](self.potencial_ativacao[i][j], derivada=True), 6)
                        else:
                            self.gradiente_local[i][j] = round(self.calcular_gradiente_local(i, j) * self.funcao_ativacao[i](self.potencial_ativacao[i][j], derivada=True), 6)
                        # self.gradiente_local[i][j] =  valor * self.funcao_ativacao(self.potencial_ativacao[i][j], derivada=True)
                        print("Gradiente Local " + str(i) + ", " + str(j) + ": " + str(self.gradiente_local[i][j]))
                        input('')
                        for k in range(0, len(self.peso_sinaptico[i][j])):
                            print(str(self.peso_sinaptico[i][j][k]) + " + " + str(self.taxa_aprendizagem) + " * " + str(self.gradiente_local[i][j]) + "*" + str(saida[k]))
                            input('')
                            self.peso_sinaptico[i][j][k]  += round((self.taxa_aprendizagem * self.gradiente_local[i][j] * saida[k]), 6)
            EQM_ATUAL = round(self.eqm(), 6)
            print("|" + str(EQM_ANTERIOR) + "-" + str(EQM_ATUAL) + "| = " + str(abs(round((EQM_ANTERIOR - EQM_ATUAL), 6))))
            self.epocas += 1
            if abs(EQM_ANTERIOR - EQM_ATUAL) <= self.precisao or self.epocas == 1:
                print(self.epocas)
                for i in range(0, len(self.camadas)):
                    print("Camada " + str(i) + ":" + str(self.peso_sinaptico[i]))
                    print("Gradiente: " + str(i) + ":" + str(self.gradiente_local[i]))
                break
mlp = MLP([3, 2], [[[2,1], [1, 0]]], [logistica, linear], 0.1, 0.000001)
mlp.treinar()