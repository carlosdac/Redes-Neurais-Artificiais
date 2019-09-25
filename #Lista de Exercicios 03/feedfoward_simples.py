from random import random
from math import *
def degrau_bipolar(u):
    if u >= 0:
        return 1
    return -1

def tangente_hiperbolica(u, beta=1):
    return (1 - exp(-1 * beta * u))/(1 + exp(-1 * beta * u))

class FeedFoward():
    def __init__(self, pesos, limiar, funcao):
        self.pesos = pesos
        self.limiar = limiar
        self.funcao = funcao
    def treinar(amostras):
        self.amostras = amostras
        self.epocas = 0
        for lista in self.pesos:
            for peso in lista:
                peso = random()
        for amostra in self.amostras:
            pass