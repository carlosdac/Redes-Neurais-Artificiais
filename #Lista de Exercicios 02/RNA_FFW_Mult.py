import NA_MCP


class RNA_FFW_Mult:
    def __init__(self, arq_na):
        self.camadas = []
        for i in range(len(arq_na)):
            self.camadas.append([])
            for j in range(len(arq_na[i])):
                self.camadas[i].append(NA_MCP.NA_MCP(arq_na[i][j][0], arq_na[i][j][1], arq_na[i][j][2]))

    def process(self, x):
        y = [x]
        for i in range(len(self.camadas)):
            y.append([])
        for camada in range(len(self.camadas)):
            for na_mcp in self.camadas[camada]:
                y[camada+1].append(na_mcp.g(y[camada]))
        return y[-1]
