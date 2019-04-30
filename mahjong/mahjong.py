#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import random
import os
from src import *

if __name__ == '__main__':
    graphics = graphic_system()
    jeu_mahjong = mahjong_board(graphics)

    for player in range(4):
        for tile in range(13):
            jeu_mahjong.pioche(player, refresh=False)
        jeu_mahjong.refresh_player_gfx(player)
    jeu_mahjong.refresh_mur_gfx()

    mouse_underlay = mouse_cursor_underlay()

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_underlay.rect.x = event.pos[0]
                    mouse_underlay.rect.y = event.pos[1]
                    selected_sprites = pygame.sprite.spritecollide(mouse_underlay, graphics.all_sprites, False)

        jeu_mahjong.next_step()

        graphics.screen.fill(white)
        graphics.draw_game()

        clock.tick(30)

        pygame.display.flip()

    pygame.quit()
