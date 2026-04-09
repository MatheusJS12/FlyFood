
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
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valor = matriz[i][j]
            if valor != '0':
                pontos[valor] = (i, j)
    return pontos