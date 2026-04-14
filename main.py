
import sys
from itertools import permutations

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
    Utiliza as coordenadas registradas no dicionário "pontos" e reliza todas as
    permutações possíveis
    '''
    permutacoes = []
    for j in permutations(pontos):
        permutacoes.append(j)
    
    print(permutacoes)
    
    '''Qunado retornar, devo consertar as funções e inicializar o código'''

    cont = 0
    for permutacao in permutacoes:
        tamanho = len(permutacao)
        for cidade in permutacao:
            if cont == 0:
                p1 = destino['R']
                cont += 1
            
            elif cont == tamanho:
                p2 = destino['R']
            
            if cidade:
                if cont == 0:
                    p2 = pontos[cidade]
                
                elif cont == tamanho:
                    p1 = pontos[cidade]
                    cont = 0
                
                else:
                    p1 = pontos[cidade]
                    '''p2 = '''
                    cont += 1


                


                
            
    

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

ler_matriz()
    