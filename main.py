arq = open("grafo.txt")

# Funções

def lerQTDVertices(): #Ler quantidade de vértices
    return(arq.readline().replace("\n", ""))

v = lerQTDVertices()

for line in arq:
    format = line.replace("\n", "")
    print(format)


