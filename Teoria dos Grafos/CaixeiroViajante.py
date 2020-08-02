import random
import time

def NEARESTNEIGHBOR(listaAdj,matAdj):

    naoVisitados = [x for x in range(len(listaAdj))]
    naoVisitados.remove(naoVisitados[0])

    u = 0  //Vértice inicial do circuito hamiltoniano 
    S = [u]  //Lista que contém a sequência da vértices do ciclo hamiltoniano(inicialmente contem u) 

    while(len(naoVisitados) != 0):
        V = 0
        min = float('inf')
        for (v,w) in listaAdj[u]:
            if v in naoVisitados and w < min:
                min = w
                V = v

        S.append(V)
        naoVisitados.remove(V)
        u = V
    S.append(S[0])  //Adicionar o vértice origem para fechar o ciclo 

    print('Distância de NN: {}'.format(AVALIA(S, matAdj)))

    return S


def AVALIA(S, matAdj):

    custo = 0

    for i in range((len(S))-1):
        u = S[i]
        v = S[i + 1]
        custo += matAdj[u][v]

    return custo


def TWOOPT(S, matAdj):

    tempoDisponivel = 60
    aux = 0
    s = 0

    start = time.time()

    while(tempoDisponivel > (time.time() - start)):
        i1 = []
        i1.append(random.choice(list(enumerate(S[1:-1]))))
        i1 = i1[0][0]

        i2 = []
        i2.append(random.choice(list(enumerate(S[1:-1]))))
        i2 = i2[0][0]

        if (i1 != i2 and i1 != 0 and i2!= 0)
            s = S.copy()
            aux = s[i1]
            s[i1] = s[i2]  //Trocar elemento da posição i1 com elemento de i2 
            s[i2] = aux
            if AVALIA(s,matAdj) < AVALIA(S,matAdj):
                S = s.copy()  //s é melhor que a melhor solução corrente S, que é atualizada

    print('Distância 2opt : {}'.format(AVALIA(S, matAdj)))
    print('Rota : {}'.format(S))
