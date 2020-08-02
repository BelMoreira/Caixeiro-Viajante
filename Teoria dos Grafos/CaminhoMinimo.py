# Retornar o caminho mínimo a partir do vetor predecessor
def CAMINHO1(s, t, pred):
    C = []
    C += [t]
    aux = t
    while(aux!= s):
        aux = pred[aux]
        C.insert(0, aux)
    return C

# Algoritmo de Dijkstra
def DIJSKSTRA(matAdj, s, t):

    inf = float('inf')
    vago = ('-')
    # Atribui infinito ao vetor que armazena a distância da origem a cada vértice
    dist = [inf for x in range(len(matAdj))]
    # Atribui nulo ao vetor que indica o predecessor de cada vértice no caminho mínimo a partir da origem
    pred = [vago for x in range(len(matAdj))]

    dist[s] = 0

    # Conjunto de vértices que seram processados
    Q = [x for x in range(len(matAdj))]

    while (len(Q)!=0):
        minimo = 999999
        for i in Q:
            if dist[i] <= minimo:
                # u : vértice de menor distância dentre os vértices de Q
                u = i
                minimo = dist[i]
        Q.remove(u) # Removendo vértice u de Q(depois de processado)

        for i in range(len(matAdj)):
            v = i
            if matAdj[u][v] != 0:
                if dist[v] > dist[u] + matAdj[u][v]:
                    dist[v] = dist[u] + matAdj[u][v]
                    pred[v] = u

    print('Caminho : {}'.format(CAMINHO1(s, t,pred)))
    print('Custo : {}'.format(dist[t]))

# Algoritmo de Bellman-Ford
def BELLMANFORD(matAdj, s, t,E):

# Criar uma lista de arestas e percorre-lá

    inf = float('inf')
    vago = ('-')
    # Atribui infinito ao vetor que armazena a distância da origem a cada vértice
    dist = [inf for x in range(len(matAdj))]
    # Atribui nulo ao vetor que vetor que indica o predecessor de cada vértice no caminho mínimo
    pred = [vago for x in range(len(matAdj))]

    dist[s] = 0

    for i in range(len(matAdj)):
        for u_v in E:
         u = u_v[0]
         v = u_v[1]
         if dist[v] > dist[u] + matAdj[u][v]:
            dist[v] = dist[u] + matAdj[u][v]
            pred[v] = u

    print(dist)
    print(pred)

    print('Caminho : {}'.format(CAMINHO1(s, t, pred)))
    print('Custo : {}'.format(dist[t]))


    for u_v in E:
        u = u_v[0]
        v = u_v[1]
        if dist[v] > dist[u] + matAdj[u][v]:
            return False
    return True

# Retornar o caminho mínimo a partir da matriz de predecessores
def CAMINHO2(s, t, pred):
    C = []
    C += [t]
    aux = t
    while(aux != s):
        aux = pred[s][aux]
        C.insert(0, aux)
    return C

# Algoritmo de Floyd-Warshall
def FLOYDWARSHALL(matAdj, s, t):

   inf = float('inf')
   vago= ('--')
   null=('-')
   # dist: matriz que armazena a distância de cada vértice (linha) a cada vértice (coluna)
   dist = [[vago for x in range(len(matAdj))] for x in range(len(matAdj))]
   # pred:matriz que indica o predecessor de cada vértice (coluna) no caminho mínimo a partir de cada vértice (linha)
   pred = [[vago for x in range(len(matAdj))] for x in range(len(matAdj))]

   for i in range(len(matAdj)):
       for j in range(len(matAdj[i])):
          if i == j:
              dist[i][j] = 0

          elif matAdj[i][j] != 0: # Verificando se existe aresta entre i e j
              dist[i][j] = matAdj[i][j]
              pred[i][j] = i

          else:

              dist[i][j] = inf
              pred[i][j] = null

   for k in range(len(matAdj)):
       for i in range(len(matAdj[k])):
           for j in range(len(matAdj[i])):
               if dist[i][j] > dist[i][k] + dist[k][j]:
                   dist[i][j] = dist[i][k] + dist[k][j]
                   pred[i][j] = pred[k][j]

   print('Caminho : {}'.format(CAMINHO2(s, t, pred)))
   print('Custo : {}'.format(dist[s][t]))