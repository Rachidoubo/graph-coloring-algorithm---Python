import Functions
import ColorerGraph
list_sommets = []
list_adjacence = []
list_degre = []

# Recupération des sommets et leurs adjacences :
n = int(input("donner le degre du graphes: "))
for i in range(n):
    list_sommets += input("Sommet "+str(i+1)+" : ")
    print("Donner les adjacents du sommet ",list_sommets[i]," séparé par des espaces: ")
    adjcents = input()
    list_adjacence += [adjcents.split()]
    list_degre += [len(adjcents.split())]
l_temp =[] + list_degre
D = Functions.genererDict(l_temp)
print(D)
graphColore = ColorerGraph.ColorerGraph(list_sommets, list_adjacence, list_degre)

#Output:
print(list_sommets)
print(list_adjacence)
print(list_degre)
print(graphColore)
