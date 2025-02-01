import pygame
from config import LARGURA_JANELA, ALTURA_JANELA, TAMANHO_CELULA, COR_PAREDE, COR_CAMINHO, COR_INICIO, COR_DESTINO, COR_VISITADO, COR_AGENT, posicao_inicial, posicao_destino

# Inicializa o Pygame e a janela
def inicializar_pygame():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA_JANELA, ALTURA_JANELA))
    pygame.display.set_caption("Labirinto - Menu de Busca")
    return tela

# Função para desenhar o labirinto e os custos
def desenhar_labirinto(tela, matriz, visitados=set(), agente=None, passos=None, custos=None):
    fonte = pygame.font.SysFont("Arial", 16)  

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            x = coluna * TAMANHO_CELULA
            y = linha * TAMANHO_CELULA

            if matriz[linha][coluna] == 0:
                cor = COR_PAREDE
            elif (linha, coluna) in visitados:
                cor = COR_VISITADO
            else:
                cor = COR_CAMINHO

            pygame.draw.rect(tela, cor, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))

            
            if custos and (linha, coluna) in custos:
                custo_texto = fonte.render(str(custos[(linha, coluna)]), True, (0, 0, 0))
                tela.blit(custo_texto, (x + TAMANHO_CELULA // 4, y + TAMANHO_CELULA // 4))

    x_inicial, y_inicial = posicao_inicial[1] * TAMANHO_CELULA, posicao_inicial[0] * TAMANHO_CELULA
    pygame.draw.rect(tela, COR_INICIO, (x_inicial, y_inicial, TAMANHO_CELULA, TAMANHO_CELULA))

    x_destino, y_destino = posicao_destino[1] * TAMANHO_CELULA, posicao_destino[0] * TAMANHO_CELULA
    pygame.draw.rect(tela, COR_DESTINO, (x_destino, y_destino, TAMANHO_CELULA, TAMANHO_CELULA))

    if agente:
        x_agente, y_agente = agente[1] * TAMANHO_CELULA, agente[0] * TAMANHO_CELULA
        pygame.draw.rect(tela, COR_AGENT, (x_agente, y_agente, TAMANHO_CELULA, TAMANHO_CELULA))

    fonte_passos = pygame.font.SysFont("Arial", 20)
    texto_passos = fonte_passos.render(f"Passos: {passos}", True, (0, 0, 0))
    tela.blit(texto_passos, (10, 10))

