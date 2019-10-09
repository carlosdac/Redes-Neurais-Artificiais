
from random import random
import matplotlib.pyplot as plt
import xlrd
import os
#getcontext().prec = 6

OFFLINE = 0
ONLINE = 1
HESSIANA = 2
APRENDIZADO = ONLINE
arquivos = []
for _, _, arquivo in os.walk('pesos/'):
    arquivos.append(arquivo)



def leitura_treinamento():
    amostras = []
    xls = xlrd.open_workbook("Treinamento_Adaline_PPA.xls")
    plan = xls.sheets()[0]
    for i in range(1, plan.nrows):
        linha = plan.row_values(i)
        amostra = (linha[0:len(linha)-1], linha[len(linha)-1]) 
        amostra[0].insert(0, -1)
        amostras.append(amostra)
    # x1 = []
    # x2 = []
    # x3 = []
    # x4 = []    
    # for amostra in amostras:
    #     for i in range(1, len(amostra[0])):
    #         if i == 1:
    #             x1.append(amostra[0][i])
    #         if i == 2:
    #             x2.append(amostra[0][i])
    #         if i == 3:
    #             x3.append(amostra[0][i])
    #         if i == 4:
    #             x4.append(amostra[0][i])
    # min_x1 = min(x1)
    # max_x1 = max(x1)
    # min_x2 = min(x2)
    # max_x2 = max(x2)
    # min_x3 = min(x3)
    # max_x3 = max(x3)
    # min_x4 = min(x4)
    # max_x4 = max(x4)
    # for amostra in amostras:
    #     for i in range(1, len(amostra[0])):
    #         if i == 1:
    #             min_x = min_x1
    #             max_x = max_x1
    #         if i == 2:
    #             min_x = min_x2
    #             max_x = max_x2
    #         if i == 3:
    #             min_x = min_x3
    #             max_x = max_x3
    #         if i == 4:
    #             min_x = min_x4
    #             max_x = max_x4
    #         amostra[0][i] = (amostra[0][i] - min_x)/(max_x - min_x)
    return amostras
def leitura_pesos(arquivo):
    xls = xlrd.open_workbook("pesos/"+ arquivo)
    plan = xls.sheets()[0]
    pesos = []
    for i in range(0, plan.nrows):
        linha = plan.row_values(i)
        pesos.append(linha)
    print(pesos)
    return pesos

def leitura_amostras():
    xls = xlrd.open_workbook("Teste_Adaline_PPA.xls")
    plan = xls.sheets()[0]
    pesos = []
    for i in range(1, plan.nrows):
        linha = plan.row_values(i)
        linha.insert(0, -1)
        pesos.append(linha)
    print(pesos)
    return pesos
def degrau(u):
    if u >= 0:
        return 1
    return 0

def degrau_bipolar(u):
    if u >= 0:
        return 1
    return -1

class Adaline():
    def __init__(self, amostras, taxa_aprendizado, erro, funcao, maximo_epocas=20000):
        self.amostras = amostras
        self.taxa_aprendizado = taxa_aprendizado
        self.g = funcao
        #self.hessiana()
        self.maximo_epocas = maximo_epocas
        self.erro = erro

    def hessiana(self, amostra):
        hess = [[] for i in range(0, len(amostra) + 1)]
        aux = [1] + amostra[0]
        hess[0] = aux

        for i in range(1, len(hess)):
            hess[i] += amostra[0]
            for j in range(0, len(amostra)):
                if j == i - 1:
                    for k in range(0, len(hess[i])):
                        print(hess[i][k])
                        hess[i][k] *= amostra[0][j]
        print(hess)
        return hess


    def multiplicar_vetor(self, vetor1, vetor2):
        soma = 0
        for i in range(0, len(vetor1)):
            soma += ((vetor1[i]) * (vetor2[i]))
        return (soma)
    
    def eqm(self):
        eqm = 0
        for amostra in self.amostras:
            u = (self.multiplicar_vetor(self.pesos_sinapticos, amostra[0]))
            eqm += (((amostra[1]) - u) ** 2)
        eqm /= len(self.amostras)
        return (eqm)
    
    def soma_erro(self, u):
        erro = 0
        for amostra in self.amostras:
            erro += ((amostra[1]) - u)
        return (erro)

    def treinar(self):
        self.pesos_sinapticos = [(0), (0), (0)]#[(random()).quantize(("1.000000")) for i in range(len(self.amostras[0][0]))]#
        print("Vetor de pesos inicial: " + str(self.pesos_sinapticos))
        self.epocas = 0
        erros = []
        epoca = []
        
        soma_erro = (0)
        while True:
            print("Época: " + str(self.epocas))
            eqm_anterior = self.eqm()
            print("EQM anterior: " + str(eqm_anterior))
            
            for amostra in self.amostras:
                u = self.multiplicar_vetor(self.pesos_sinapticos, amostra[0])
                soma_erro += ((amostra[1]) - u)
            
            for amostra in self.amostras:
                hess = self.hessiana(amostra)
                u = self.multiplicar_vetor(self.pesos_sinapticos, amostra[0])
                print("u = " + str(u))
                print("w = " + str(self.pesos_sinapticos).replace(",", "") + "T + " + str((self.taxa_aprendizado)) + " * " + str(((amostra[1]) - u)) + " * " + str((amostra[0])).replace(",", "") )
                
                for i in range(len(self.pesos_sinapticos)):
                    if APRENDIZADO == ONLINE:
                        self.pesos_sinapticos[i] += ((self.taxa_aprendizado) * ((amostra[1]) - u) * (amostra[0][i]))
                    elif APRENDIZADO == HESSIANA:
                        self.pesos_sinapticos[i] += ((self.taxa_aprendizado) * soma_erro * (amostra[0][i]))
                    else:
                        self.pesos_sinapticos[i] += ((self.taxa_aprendizado) * soma_erro * (amostra[0][i]))
                
                print("w = " + str(self.pesos_sinapticos).replace(",", ""))
            
            eqm_atual = self.eqm()
            print("EQM atual: " + str(eqm_atual))
            print("Erro = |" + str(eqm_anterior) +" - " + str(eqm_atual) + "|")
            print("Erro = " + str(abs(eqm_anterior - eqm_atual)))
            erros.append(eqm_atual)
            epoca.append(self.epocas)
            
            self.epocas += 1
            if abs(eqm_anterior - eqm_atual) <= self.erro or self.epocas == self.maximo_epocas:
                print("Época: "+ str(self.epocas))
                return epoca, erros
            print("\n\n")
    def testar(self, amostra):
        u = self.multiplicar_vetor(self.pesos_sinapticos, amostra)
        y = self.g(u)
        if y == -1:
            print("-1")
        if y == 1:
            print("1")
        return

amostras = leitura_treinamento()#[([-1, 0, 0], 0), ([-1, 0, 1], 1), ([-1, 1, 0], 1), ([-1, 1, 1], 1)]#
taxa_aprendizado = 0.5
adaline = Adaline(amostras, taxa_aprendizado, 0.0001, degrau_bipolar, 10)
adaline.treinar()
input()
#print(adaline.treinar())
treinamentos = [1, 2, 3, 4, 5]
APRENDIZADO = HESSIANA
for treinamento in treinamentos:
    erros, epoca = adaline.treinar()
    if treinamento <= 2:
        plt.plot(erros, epoca)
        plt.title("Treinamento: " + str(treinamento))
        plt.savefig("Treinamento4_" + str(treinamento) + ".png")
        plt.show()
    print(adaline.epocas)
    print("Vetor de pesos final: " + str(adaline.pesos_sinapticos))
    print("\n\n")
for peso in adaline.pesos_sinapticos:
    print(peso.quantize(('1.000000')))
# adaline = Adaline(None, None, None, degrau_bipolar)
# amostras = leitura_amostras()
# for arquivo in arquivos[0]:
#     i = 1
#     print("------------"+arquivo+"-----------")
#     for peso in leitura_pesos(arquivo):
#         adaline.pesos_sinapticos = peso
#         print("Treinamento " + str(i))
#         for amostra in amostras:
#             adaline.testar(amostra)
#         print("==============================")
#         i += 1