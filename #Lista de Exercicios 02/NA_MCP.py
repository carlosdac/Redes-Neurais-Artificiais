import math


class NA_MCP:
    def __init__(self, limiar, func, w, a=1, beta=1, alpha=1):
        self.limiar = limiar
        self.func = func
        self.w = w
        self.a = a
        self.beta = beta
        self.alpha = alpha

    def mult_w_x(self, x):
        soma = 0
        for i in range(0, len(self.w)):
            soma += x[i] * self.w[i]
        return soma

    def g(self, x):
        u = self.mult_w_x(x) - self.limiar
        if self.func == 'degrau':
            if u >= 0:
                return 1
            else:
                return 0
        elif self.func == 'degrau_bipolar':
            if u > 0:
                return 1
            elif u < 0:
                return -1
            else:
                return 0
        elif self.func == 'rampa_simetrica':
            if u > self.a:
                return 1
            elif u < -self.a:
                return -1
            else:
                return u
        elif self.func == 'logistica':
            p1 = math.e**-(u*self.beta)
            return 1/(1 + p1)
        elif self.func == 'tang_hiper':
            p1 = math.e**-(u*self.beta)
            return (1-p1)/(1+p1)
        elif self.func == 'linear':
            return u
        elif self.func == 'gaussiana':
            return math.e**-((u-self.c)**2)/(2*self.alpha**2)
