from numpy import matrix


arq = open("grafo.txt")

# Funções

def formatarLinha(linha):
    format = linha.replace("\n", "")
    return(format)

def lerVertices(): #Ler quantidade de vértices
    v = []
    qtdVertices = formatarLinha(arq.readline())
    for i in range (int(qtdVertices)):
        v.append([])
    return(v)

def lerArestas():
    arestas = []
    for line in arq:
        format = formatarLinha(line)
        arestas.append(format.split())
    return(arestas)

def contarGrau(vert):
    return(len(vert))

def menorGrau(vertices):
    menor = 9999999
    for vertice in vertices:
        if len(vertice) <= menor:
            menor = len(vertice)
    return(menor)

def maiorGrau(vertices):
    maior = 0
    for vertice in vertices:
        if len(vertice) >= maior:
            maior = len(vertice)
    return(maior)

def criarMatriz(dimensao, vertices):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(0)
            for vertice in range(int(len(vertices[i]))):       
                if j+1 == int(vertices[i][vertice]):
                    linha[j] = 1
        matriz.append(linha)
    return(matriz)
###############################################################################
# Código


vertices = lerVertices()
arestas = lerArestas()


for aresta in arestas:
    for i in range(len(vertices)):
        if int(aresta[0]) == i+1:
            vertices[i].append(aresta[1])
        if int(aresta[1]) == i+1:
            vertices[i].append(aresta[0])
        
print("Quantidade de vértices: " + str(len(vertices)))
print("Quantidade de Arestas: " + str(len(arestas)))
print("Menor Grau: " + str(menorGrau(vertices)))
print("Maior Grau: " + str(maiorGrau(vertices)))

matrizAdj = criarMatriz(len(vertices), vertices)
print("Matriz de Adjacência: ")

string = "   "
for i in range(len(vertices)):
    string += str(i+1) + "  "
print(string)

for i in range(len(vertices)):
    print(str(i+1) + " " + str(matrizAdj[i]))