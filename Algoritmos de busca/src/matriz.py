import os

# Função para carregar a matriz a partir do arquivo
def carregar_matriz():
    matriz = []
    
    diretorio_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    caminho_arquivo = os.path.join(diretorio_base, "data", "input", "matriz.txt")
    
    try:
        print( f"Caminho encontrado: {caminho_arquivo}" )
        with open(caminho_arquivo, 'r') as arquivo:
            for linha in arquivo:
                matriz.append([int(x) for x in linha.split()])
        return matriz
    except FileNotFoundError:
        print(f"Erro: O arquivo 'matriz.txt' não foi encontrado no caminho: {caminho_arquivo}")
        return None
