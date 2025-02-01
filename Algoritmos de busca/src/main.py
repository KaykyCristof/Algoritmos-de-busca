from matriz import carregar_matriz  # type: ignore
from labirinto import inicializar_pygame, desenhar_labirinto  
from config import posicao_inicial, posicao_destino
from menu import exibir_menu, exibir_heuristica_menu  
from buscas import busca_gulosa

# Loop principal
def main():

    global tela
    tela = inicializar_pygame()

    matriz_labirinto = carregar_matriz()
    if matriz_labirinto is None:
        return  
    
    busca_escolhida = exibir_menu(tela)

    if busca_escolhida == exibir_heuristica_menu:
        heuristica_escolhida = exibir_heuristica_menu(tela)
        busca_gulosa(matriz_labirinto, posicao_inicial, posicao_destino, tela, desenhar_labirinto, heuristica_escolhida)
    else:
        busca_escolhida(matriz_labirinto, posicao_inicial, posicao_destino, tela, desenhar_labirinto)

if __name__ == "__main__":
    main()
