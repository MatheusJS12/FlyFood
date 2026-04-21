
import sys
from itertools import permutations
import datetime

def ler_matriz():
    """
    Transforma o arquivo de texto em uma lista organizada de linhas.
    Pula a primeira linha de dimensões e foca apenas no mapa do drone 
    retornando uma lista de listas (matriz) para facilitar a localização
    dos pontos
    """
    entrada = sys.stdin.read().splitlines()
    if not entrada:
        return []
    
    primeira_linha = entrada[0].split()
    if not primeira_linha:
        return []
        
    qtd_linhas = int(primeira_linha[0])
    matriz = []
   
    for i in range(1, qtd_linhas + 1):
        if i < len(entrada):
            elementos = entrada[i].split()
            if elementos:
                matriz.append(elementos)
    
    return matriz

def buscar_pontos(matriz):
    """
    Armazena as coordenadas de cada ponto onde é diferente de 0 
    em um dicionário para acesso rápido durante o cálculo das distâncias
    """
    pontos = {}
    destino = {}
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            if valor != '0' and valor != 'R':
                pontos[valor] = (i, j)
            
            elif valor == 'R':
                destino[valor] = (i, j)
    return pontos, destino

def permutacao(pontos, destino):
    '''
    Utiliza as coordenadas registradas no dicionário "pontos" e realiza todas as
    permutações possíveis
    '''
    permutacoes = []
    todas_distancias = []
    '''for j in permutations(pontos):
        permutacoes.append(j)
    
    print(permutacoes)'''

    cont = 0
    menor = 1000000
    permut = None
    
    origem = destino['R']

    for permutacao in permutations(pontos):
        tamanho = len(permutacao)
        cont = 0
        soma = 0
        for cidade in permutacao:

            atual = pontos[cidade]

            if cont == 0:
                soma += distancia(origem, atual)
            
            elif cont == tamanho - 1:
                soma += distancia(prox, atual)
                soma += distancia(atual, origem)
                if soma < menor:
                    menor = soma
                    permut = permutacao
            
            else:
                soma += distancia(prox, atual)
            
            prox = atual
            cont += 1
        
    print('\nmenor distância: {}'.format(menor))
    print('permutação: {}'.format(permut))



def distancia(p1, p2):
    x0, y0 = p1
    x1, y1 = p2

    if x0 >= x1:
        dx = x0 - x1
    else:
        dx = x1 - x0

    if y0 >= y1:
        dy = y0 - y1
    else:
        dy = y1 - y0

    return dx + dy

inicio = datetime.datetime.now()
matriz = ler_matriz()
pontos, destino = buscar_pontos(matriz)
permutacao(pontos, destino)
fim = datetime.datetime.now()
print('tempo de execução: {}'.format(fim - inicio))

'''Get-Content input.txt | python main.py'''