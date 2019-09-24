
from random import random
from decimal import Decimal, getcontext
import xlrd
getcontext().prec = 6

def leitura_treinamento():
    amostras = []
    xls = xlrd.open_workbook("Treinamento_Adaline_PPA.xls")
    plan = xls.sheets()[0]
    for i in range(1, plan.nrows):
        linha = plan.row_values(i)
        amostra = (linha[0:len(linha)-1], linha[len(linha)-1]) 
        amostra[0].insert(0, -1)
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

class Adaline():
    def __init__(self, amostras, taxa_aprendizado, erro, funcao, maximo_epocas=10000):
        self.amostras = amostras
        self.taxa_aprendizado = taxa_aprendizado
        self.g = funcao
        self.maximo_epocas = maximo_epocas
        self.erro = erro

    def multiplicar_vetor(self, vetor1, vetor2):
        soma = 0
        for i in range(0, len(vetor1)):
            soma += (Decimal(vetor1[i]) * Decimal(vetor2[i]))
        return Decimal(soma)
    def eqm(self):
        eqm = 0
        for amostra in self.amostras:
            u = Decimal(self.multiplicar_vetor(self.pesos_sinapticos, amostra[0]))
            eqm += Decimal(((amostra[1]) - u) ** 2)
        eqm /= len(self.amostras)
        return Decimal(eqm)
    def treinar(self):
        self.pesos_sinapticos = [Decimal(random()) for i in range(len(self.amostras[0][0]))]
        self.epocas = 0
        while True:
            eqm_anterior = self.eqm()
            for amostra in self.amostras:
                u = self.multiplicar_vetor(self.pesos_sinapticos, amostra[0])
                for i in range(len(self.pesos_sinapticos)):
                    self.pesos_sinapticos[i] += Decimal(Decimal(self.taxa_aprendizado) * Decimal((amostra[1]) - u) * Decimal(amostra[0][i]))
            self.epocas += 1
            eqm_atual = self.eqm()
            if abs(eqm_anterior - eqm_atual) <= self.erro or self.epocas == self.maximo_epocas:
                break
    def testar(self, amostra):
        u = self.multiplicar_vetor(self.pesos_sinapticos, amostra)
        y = self.g(u)
        if y == -1:
            print("Classe A")
        if y == 1:
            print("Classe B")
        return

amostras = [([-1, 0, 0], 0), ([-1, 0, 1], 1), ([-1, 1, 0], 1), ([-1, 1, 1], 1)]#leitura_treinamento()
taxa_aprendizado = 0.5
adaline = Adaline(amostras, taxa_aprendizado, 0, degrau_bipolar)
adaline.treinar()
print(adaline.epocas)
for peso in adaline.pesos_sinapticos:
    print(peso.quantize(Decimal('1.000000')))
print(adaline.pesos_sinapticos)