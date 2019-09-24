
from random import random
from decimal import Decimal, getcontext
import matplotlib.pyplot as plt
import xlrd
getcontext().prec = 6

OFFLINE = 0
ONLINE = 1
APRENDIZADO = OFFLINE


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
            eqm += Decimal((Decimal(amostra[1]) - u) ** 2)
        eqm /= len(self.amostras)
        return Decimal(eqm)
    
    def soma_erro(self, u):
        erro = 0
        for amostra in self.amostras:
            erro += Decimal(Decimal(amostra[1]) - u)
        return Decimal(erro)

    def treinar(self):
        self.pesos_sinapticos = [Decimal(random()).quantize(Decimal("1.000000")) for i in range(len(self.amostras[0][0]))]#[Decimal(0), Decimal(0), Decimal(0)]
        print("Vetor de pesos inicial: " + str(self.pesos_sinapticos))
        self.epocas = 0
        erros = []
        epoca = []
        
        while True:
            eqm_anterior = self.eqm()
            
            for amostra in self.amostras:
                u = self.multiplicar_vetor(self.pesos_sinapticos, amostra[0])
                soma_erro = Decimal(self.soma_erro(u))
                
                for i in range(len(self.pesos_sinapticos)):
                    if APRENDIZADO == ONLINE:
                        self.pesos_sinapticos[i] += Decimal(Decimal(self.taxa_aprendizado) * Decimal(Decimal(amostra[1]) - u) * Decimal(amostra[0][i]))
                    else:
                        self.pesos_sinapticos[i] += Decimal(Decimal(self.taxa_aprendizado) * soma_erro * Decimal(amostra[0][i]))
            
            self.epocas += 1
            eqm_atual = self.eqm()
            
            erros.append(eqm_atual)
            epoca.append(self.epocas)
            
            if abs(eqm_anterior - eqm_atual) <= self.erro or self.epocas == self.maximo_epocas:
                return epoca, erros
    
    def testar(self, amostra):
        u = self.multiplicar_vetor(self.pesos_sinapticos, amostra)
        y = self.g(u)
        if y == -1:
            print("Classe A")
        if y == 1:
            print("Classe B")
        return

amostras = leitura_treinamento()#[([-1, 0, 0], 0), ([-1, 0, 1], 1), ([-1, 1, 0], 1), ([-1, 1, 1], 1)]#
taxa_aprendizado = 0.0025
adaline = Adaline(amostras, taxa_aprendizado, 0.000001, degrau_bipolar)
treinamentos = [1, 2, 3, 4, 5]
APRENDIZADO = ONLINE
for treinamento in treinamentos:
    erros, epoca = adaline.treinar()
    if treinamento <= 2:
        plt.plot(erros, epoca)
        plt.title("Treinamento: " + str(treinamento))
        plt.savefig("Treinamento3_" + str(treinamento) + ".png")
        plt.show()
    print(adaline.epocas)
    print("Vetor de pesos final: " + str(adaline.pesos_sinapticos))
    print("\n\n")
# for peso in adaline.pesos_sinapticos:
#     print(peso.quantize(Decimal('1.000000')))