import pygame
import sys
from buscas import busca_profundidade, busca_largura, heuristica_manhattan, heuristica_euclidiana

# Função que exibe o menu de opções de busca
def exibir_menu(tela):
    fonte = pygame.font.SysFont("Arial", 30)
    tela.fill((255, 255, 255))
    
    texto = fonte.render("Escolha a Busca", True, (0, 0, 0))
    tela.blit(texto, (200, 100))
    
    texto_profundidade = fonte.render("1. Busca em Profundidade", True, (0, 0, 0))
    tela.blit(texto_profundidade, (150, 200))
    
    texto_largura = fonte.render("2. Busca em Largura", True, (0, 0, 0))
    tela.blit(texto_largura, (150, 250))
    
    texto_estrela = fonte.render("3. Busca Gulosa", True, (0, 0, 0))
    tela.blit(texto_estrela, (150, 300))
    
    pygame.display.flip()

    # Loop de eventos para esperar a escolha do usuário
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return busca_profundidade  
                elif event.key == pygame.K_2:
                    return busca_largura  
                elif event.key == pygame.K_3:
                    return exibir_heuristica_menu  

# Função que exibe o menu para escolher a heurística
def exibir_heuristica_menu(tela):
    fonte = pygame.font.SysFont("Arial", 30)
    tela.fill((255, 255, 255))

    texto = fonte.render("Escolha a Heurística", True, (0, 0, 0))
    tela.blit(texto, (200, 100))
    
    texto_manhattan = fonte.render("1. Distância Manhattan", True, (0, 0, 0))
    tela.blit(texto_manhattan, (150, 200))
    
    texto_euclidiana = fonte.render("2. Distância Euclidiana", True, (0, 0, 0))
    tela.blit(texto_euclidiana, (150, 250))
    
    pygame.display.flip()

    # Loop de eventos para esperar a escolha da heurística
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return heuristica_manhattan  
                elif event.key == pygame.K_2:
                    return heuristica_euclidiana  
