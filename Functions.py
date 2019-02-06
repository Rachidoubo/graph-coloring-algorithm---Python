def getMax_an_index(list): # RETOURNE UN TUPLE
    max = list[0]
    indice = 0
    for i in range(1,len(list)):
        if max < list[i]:
            max = list[i]
            indice = i
    return indice, max

def genererDict(list):
    dict = {}
    max = ()
    i = 0
    while i < len(list):
        max = getMax_an_index(list)
        dict[max[0]] = max[1]
        list[max[0]] = 0
        i += 1
    return dict
if __name__ == "__main__" :
    print(genererDict([3,5,1,6,8]))
