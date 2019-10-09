import RNA_FFW_Mult
import matplotlib.pyplot

valores = []
for i in range(0, 824):
    valores.append([i/100])

na1 = [3.38888, 'tang_hiper', [0.962803]]
na2 = [11.0847, 'tang_hiper', [1.88752]]
na3 = [1.55095, 'tang_hiper', [2.51054]]
naf = [-0.4186, 'linear', [-1.9956, 1.62524, 0.88538]]

rna = RNA_FFW_Mult.RNA_FFW_Mult([[na1, na2, na3], [naf]])
result = []
for i in range(len(valores)):
    result.append(rna.process(valores[i]))

matplotlib.pyplot.close()
matplotlib.pyplot.plot(valores, result)
matplotlib.pyplot.title("Projeto Prático B")
matplotlib.pyplot.savefig("Parte Pratica 2")

