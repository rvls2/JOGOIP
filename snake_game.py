# snake_game.py

import pygame
from settings import *
from sprites import Food
from functions import fim_de_jogo, desenhar_cobra, desenhar_pontuacao, selecionar_velocidade
from bomb import Bomb

class SnakeGame:
    def __init__(self):
        self.fim_jogo = False
        self.x = largura / 2
        self.y = altura / 2
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.tamanho_cobra = 1
        self.pixels = []
        self.pontuacao = 0
        self.capturas_verdes = 0
        self.capturas_azuis = 0
        self.capturas_amarelas = 0
        self.todas_sprites = pygame.sprite.Group()
        self.comida = Food(self.pixels)
        self.todas_sprites.add(self.comida)
        self.bomba = Bomb(self.pixels, self.comida.rect)
        
    def rodar_jogo(self):
        while not self.fim_jogo:
            tela.blit(bg, [0,0])
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    self.velocidade_x, self.velocidade_y = selecionar_velocidade(evento.key, self.velocidade_x, self.velocidade_y)
            self.update()
            self.desenhar()
            pygame.display.update()
            relogio.tick(velocidade_jogo)
        fim_de_jogo(self.pontuacao, self.capturas_verdes, self.capturas_azuis, self.capturas_amarelas)

    def update(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y
        if self.x < 128 or self.x >= largura - 128 or self.y < 64 or self.y >= altura - 64:
            self.fim_jogo = True
        self.pixels.append([self.x, self.y])
        if len(self.pixels) > self.tamanho_cobra:
            del self.pixels[0]
        for pixel in self.pixels[:-1]:
            if pixel == [self.x, self.y]:
                self.fim_jogo = True
        if pygame.Rect.colliderect(self.comida.rect, [self.pixels[-1][0], self.pixels[-1][1], tamanho_quadrado, tamanho_quadrado]):
            self.comer_comida()
        if pygame.Rect.colliderect(self.bomba.rect, [self.pixels[-1][0], self.pixels[-1][1], tamanho_quadrado, tamanho_quadrado]):
            self.fim_jogo = True

    def desenhar(self):
        self.bomba.desenhar()
        desenhar_cobra(tamanho_quadrado, self.pixels)
        desenhar_pontuacao(self.pontuacao)
        self.todas_sprites.draw(tela)
        self.todas_sprites.update()

    def comer_comida(self):
        self.tamanho_cobra += 1
        if self.comida.tipo_comida['cor'] == verde:
            self.capturas_verdes += 1
        elif self.comida.tipo_comida['cor'] == azul:
            self.capturas_azuis += 1
        elif self.comida.tipo_comida['cor'] == amarelo:
            self.capturas_amarelas += 1
        self.pontuacao += self.comida.tipo_comida['pontos']
        self.todas_sprites.remove(self.comida)
        self.comida = Food(self.pixels)
        self.todas_sprites.add(self.comida)
        self.bomba = Bomb(self.pixels, self.comida.rect)

    @staticmethod
    def menu_principal():
        menu = True
        while menu:
            tela.fill(preta)
            fonte = pygame.font.SysFont("Helvetica", 50)
            titulo = fonte.render("Jogo Snake Python", True, verde)
            jogar = fonte.render("Pressione ENTER para Jogar", True, branca)
            tela.blit(titulo, (largura / 2 - titulo.get_width() / 2, altura / 3))
            tela.blit(jogar, (largura / 2 - jogar.get_width() / 2, altura / 2))
            pygame.display.update()
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        menu = False
        jogo = SnakeGame()
        jogo.rodar_jogo()
