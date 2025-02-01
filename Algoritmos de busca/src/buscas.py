import pygame
import sys
from collections import deque
import heapq
from math import sqrt

# Função de busca em profundidade
def busca_profundidade(matriz, inicio, destino, tela, desenhar_labirinto):
    visitados = set()
    pilha = [inicio]
    passos = 0

    while pilha:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        no_atual = pilha.pop()

        if no_atual not in visitados:
            visitados.add(no_atual)
            passos += 1

        tela.fill((255, 255, 255))
        desenhar_labirinto(tela, matriz, visitados, agente=no_atual, passos=passos)
        pygame.display.flip()

        if no_atual == destino:
            print(f"Objetivo alcançado em {passos} passos!")

            esperando = True
            while esperando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        esperando = False
                pygame.time.delay(100)

            return

        x, y = no_atual
        for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
            vizinho = (x + dx, y + dy)
            if 0 <= vizinho[0] < len(matriz) and 0 <= vizinho[1] < len(matriz[0]) and matriz[vizinho[0]][vizinho[1]] == 1:
                if vizinho not in visitados:
                    pilha.append(vizinho)

        pygame.time.delay(300)

# Função de busca em largura
def busca_largura(matriz, inicio, destino, tela, desenhar_labirinto):
    visitados = set()
    fila = deque([inicio])
    passos = 0

    while fila:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        no_atual = fila.popleft()

        if no_atual not in visitados:
            visitados.add(no_atual)
            passos += 1

        tela.fill((255, 255, 255))
        desenhar_labirinto(tela, matriz, visitados, agente=no_atual, passos=passos)
        pygame.display.flip()

        if no_atual == destino:
            print(f"Objetivo alcançado em {passos} passos!")

            esperando = True
            while esperando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        esperando = False
                pygame.time.delay(100)

            return

        x, y = no_atual
        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            vizinho = (x + dx, y + dy)
            if 0 <= vizinho[0] < len(matriz) and 0 <= vizinho[1] < len(matriz[0]) and matriz[vizinho[0]][vizinho[1]] == 1:
                if vizinho not in visitados:
                    fila.append(vizinho)

        pygame.time.delay(300)

# Função de heurística de Manhattan
def heuristica_manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Função de heurística Euclidiana
def heuristica_euclidiana(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Função de busca gulosa
def busca_gulosa(matriz, inicio, destino, tela, desenhar_labirinto, heuristica):
    visitados = set()
    fila_prioridade = []
    heapq.heappush(fila_prioridade, (heuristica(inicio, destino), inicio))  
    custos = {inicio: heuristica(inicio, destino)}
    passos = 0

    while fila_prioridade:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        _, no_atual = heapq.heappop(fila_prioridade)

        if no_atual in visitados:
            continue

        visitados.add(no_atual)
        passos += 1

        tela.fill((255, 255, 255))
        desenhar_labirinto(tela, matriz, visitados, agente=no_atual, passos=passos, custos=custos)
        pygame.display.flip()

        if no_atual == destino:
            print(f"Objetivo alcançado em {passos} passos!")

            esperando = True
            while esperando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                        esperando = False
                pygame.time.delay(100)

            return

        x, y = no_atual
        movimentos = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for dx, dy in movimentos:
            vizinho = (x + dx, y + dy)
            if 0 <= vizinho[0] < len(matriz) and 0 <= vizinho[1] < len(matriz[0]) and matriz[vizinho[0]][vizinho[1]] == 1:
                if vizinho not in visitados:
                    custo = heuristica(vizinho, destino)
                    custos[vizinho] = custo
                    heapq.heappush(fila_prioridade, (custo, vizinho))

        pygame.time.delay(300)
