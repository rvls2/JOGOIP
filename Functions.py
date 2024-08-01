# functions.py

import pygame
from settings import *

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 40)
    texto = fonte.render(f"Pontos: {pontuacao}", True, branca)
    tela.blit(texto, [10, 10])

def selecionar_velocidade(tecla, velocidade_x, velocidade_y):
    if tecla == pygame.K_DOWN:
        if velocidade_y != -tamanho_quadrado:
            velocidade_x = 0
            velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        if velocidade_y != tamanho_quadrado:
            velocidade_x = 0
            velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        if velocidade_x != -tamanho_quadrado:
            velocidade_x = tamanho_quadrado
            velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        if velocidade_x != tamanho_quadrado:
            velocidade_x = -tamanho_quadrado
            velocidade_y = 0
    return velocidade_x, velocidade_y

def fim_de_jogo(pontuacao, capturas_verdes, capturas_azuis, capturas_amarelas):
    fim_jogo = True
    while fim_jogo:
        tela.fill(preta)

        fonte = pygame.font.SysFont("Helvetica", 60)
        fonte_menor = pygame.font.SysFont("Helvetica", 40)
        fonte_captura = pygame.font.SysFont("Helvetica", 25)

        mensagem = fonte.render("Fim de Jogo", True, vermelha)
        capturas_verdes_texto = fonte_captura.render(f"EASY: {capturas_verdes}", True, verde)
        captura_azuis_texto = fonte_captura.render(f"HARD: {capturas_azuis}", True, azul)
        captura_amarelas_texto = fonte_captura.render(f"MEDIUM: {capturas_amarelas}", True, amarelo)
        pontuacao_texto = fonte_menor.render(f"Pontuação: {pontuacao}", True, branca)
        reiniciar = fonte_menor.render("Pressione ENTER para Jogar Novamente", True, branca)

        tela.blit(mensagem, (largura / 2 - mensagem.get_width() / 2, altura / 4.5))
        tela.blit(capturas_verdes_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2.75))
        tela.blit(captura_azuis_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2.5))
        tela.blit(captura_amarelas_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2.25))
        tela.blit(pontuacao_texto, (largura / 2 - pontuacao_texto.get_width() / 2, altura / 2))
        tela.blit(reiniciar, (largura / 2 - reiniciar.get_width() / 2, altura / 1.5))

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    fim_jogo = False
                    from main import SnakeGame
                    SnakeGame.menu_principal()
