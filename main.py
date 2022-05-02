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
###############################################################################
# Código


vertices = lerVertices()
arestas = lerArestas()


for aresta in arestas:
    for i in range(len(vertices)):
        if int(aresta[0]) == i+1:
            vertices[i].append(aresta)
        


print("Arestas:")
print(arestas)
print("Quantidade de vértices: " + str(len(vertices)))
print("Quantidade de Arestas: " + str(len(arestas)))
print("Menor Grau: " + str(menorGrau(vertices)))
print("Maior Grau: " + str(maiorGrau(vertices)))