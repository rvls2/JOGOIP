# bomb.py

import pygame
import random
from settings import *

class Bomb:
    def __init__(self, pixels, retangulo_comida):
        tamanho_por_imagem = 64
        self.img = sprite_sheet_bomba.subsurface((0, 0), (tamanho_por_imagem, tamanho_por_imagem))
        self.img = pygame.transform.scale(self.img, (tamanho_por_imagem * 1, tamanho_por_imagem * 1))
        self.bomba_x, self.bomba_y = self.gerar_bomba(pixels, retangulo_comida)

    def gerar_bomba(self, pixels, retangulo_comida):
        retangulos_cobra = [[pixel[0], pixel[1], tamanho_quadrado, tamanho_quadrado] for pixel in pixels]
        self.rect = self.img.get_rect()
        self.bomba_x = round(random.randrange(127, largura - 128 - tamanho_quadrado) / 64.0) * 64.0
        self.bomba_y = round(random.randrange(63, altura - 64 - tamanho_quadrado) / 64.0) * 64.0
        self.rect.topleft = (self.bomba_x, self.bomba_y)
        while (self.rect.collidelist(retangulos_cobra) != -1) or (pygame.Rect.colliderect(self.rect, retangulo_comida)):
            self.bomba_x = round(random.randrange(127, largura - 128 - tamanho_quadrado) / 64.0) * 64.0
            self.bomba_y = round(random.randrange(63, altura - 64 - tamanho_quadrado) / 64.0) * 64.0
            self.rect.topleft = (self.bomba_x, self.bomba_y)
        return self.bomba_x, self.bomba_y

    def desenhar(self):
        tela.blit(self.img, [self.bomba_x, self.bomba_y])
