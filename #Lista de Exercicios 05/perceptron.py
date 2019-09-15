import xlrd
from random import random

def leitura_treinamento():
    amostras = []
    xls = xlrd.open_workbook("Treinamento_Perceptron.xls")
    plan = xls.sheets()[0]
    for i in range(1, plan.nrows):
        linha = plan.row_values(i)
        amostra = (linha[0:len(linha)-1], linha[len(linha)-1]) 
        amostra[0].insert(0, -1)
        amostras.append(amostra)
    return amostras

def leitura_teste():
    amostras = []
    xls = xlrd.open_workbook("Teste_Perceptron.xls")
    plan = xls.sheets()[0]
    for i in range(1, plan.nrows):
        linha = plan.row_values(i)
        amostra = linha 
        amostra.insert(0, -1)
        amostras.append(amostra)
    return amostras

def degrau(u):
    if u >= 0:
        return 1
    return 0

def degrau_bipolar(u):
    if u >= 0:
        return 1
    return -1

class Perceptron():
    def __init__(self, amostras, taxa_aprendizagem, funcao, maximo_epocas=1000000000000):
        self.amostras = amostras
        self.maximo_epocas = maximo_epocas
        self.taxa_aprendizagem = taxa_aprendizagem
        self.epocas = 0
        self.g = funcao

    def multiplicar_vetor(self, vetor1, vetor2):
        soma = 0
        for i in range(0, len(vetor1)):
            soma += (vetor1[i] * vetor2[i])
        return soma
    
    def treinar(self):
        self.epocas = 0
        self.pesos_sinapticos = [random() for i in range(0, len(self.amostras[0][0]))]
        print("Pesos Sinápticos Inicial: " + str(self.pesos_sinapticos))
        self.erro = True
        while self.erro and self.epocas <= self.maximo_epocas:
            self.erro = False
            for amostra in self.amostras:
                u = self.multiplicar_vetor(self.pesos_sinapticos, amostra[0])
                y = self.g(u)
                if y != amostra[1]:
                    for i in range(0, len(self.pesos_sinapticos)):
                        self.pesos_sinapticos[i] += (self.taxa_aprendizagem * (amostra[1] - y) * amostra[0][i])
                        self.erro = True
            self.epocas += 1
        print("Pesos Sinápticos Final: " + str(self.pesos_sinapticos))
        print("Épocas: " + str(self.epocas))
    
    def testar(self, amostra):
        u = self.multiplicar_vetor(self.pesos_sinapticos, amostra)
        y = self.g(u)
        return y

amostras = leitura_treinamento()
testes = leitura_teste()
print(testes)
taxa_aprendizagem = 0.01
funcao = degrau_bipolar
perceptron = Perceptron(amostras, taxa_aprendizagem, funcao)
for i in range(0, 5):
    print("Treinamento " + str(i + 1) + ": ")
    perceptron.treinar()
    print("\n\n")

for teste in testes:
    print("Amostra: " + str(teste) + " ; Classe: " + str(perceptron.testar(teste)))