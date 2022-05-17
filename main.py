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
     
print("a. Quantidade de vértices: " + str(len(vertices)))
print("b. Quantidade de Arestas: " + str(len(arestas)))
print("c. Grau Mínimo: " + str(menorGrau(vertices)))
print("d. Grau Máximo: " + str(maiorGrau(vertices)))

matrizAdj = criarMatriz(len(vertices), vertices)
print("e. Representação do Grafo: ")

string = "   "
for i in range(len(vertices)):
    string += str(i+1) + "  "
print(string)

for i in range(len(vertices)):
    print(str(i+1) + " " + str(matrizAdj[i]))


def buscarElemento(inicio, buscado):
    descoberto = [inicio]
    visitado = []
    notVisited = []
    encontrado = 0

    for i in range(len(vertices)):
        notVisited.append(i+1)

    while not len(descoberto) == 0:
        for j in vertices[int(descoberto[0])-1]:
            if j not in visitado:
                descoberto.append(j)
            
        if descoberto[0] == buscado:
            visitado.append(descoberto[0])
            encontrado = 1
            break
        else:
            visitado.append(descoberto[0])
            del(descoberto[0])
            del(notVisited[0])

    return encontrado, visitado

print("Busca em Largura: ")
numInicial = input("Digite apartir de qual vértice a busca será iniciada: ")
numBuscado = input("Digite o vértice a ser buscado: ")
busca = buscarElemento(numInicial, numBuscado)
if busca[0] == 1:
    print(f"Elemento {numBuscado} encontrado: {str(busca[1])}")
else:
    print(f"Elemento {numBuscado} não encontrado")

inicio = '1'
componentes = [[]]
qtdComp = 0
for i in range(len(vertices)):
    pergunta = buscarElemento(inicio, f'{i+1}')
    if pergunta[0] == 1:
        componentes[qtdComp].append(i+1)
    else:
        inicio = f'{i+1}'
        componentes.append([i+1])
        qtdComp += 1

print("\ng. Componentes: ")
if len(componentes) > 1:
    for i in componentes:
        print(f"Componente {componentes.index(i)+1}: {i}")
else: 
    print("Esse grafo não possui componentes conexos.")