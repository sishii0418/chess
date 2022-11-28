import sys
import pygame

from engine import GameState, piece
from typing import Optional

pygame.init()

size: tuple[int, int] = 480, 480 # (width, height)
black: tuple[int, int, int] = 0, 0, 0
white: tuple[int, int, int] = 255, 255, 255
khaki: tuple[int, int, int] = 240, 230, 140
golden_rod: tuple[int, int, int] = 218, 165, 32
red: tuple[int, int, int] = 255, 0, 0
light_salmon: tuple[int, int, int] = (255,160,122)

bB: pygame.surface.Surface = pygame.image.load("images/bB.png")
bK: pygame.surface.Surface = pygame.image.load("images/bK.png")
bN: pygame.surface.Surface = pygame.image.load("images/bN.png")
bP: pygame.surface.Surface = pygame.image.load("images/bP.png")
bQ: pygame.surface.Surface = pygame.image.load("images/bQ.png")
bR: pygame.surface.Surface = pygame.image.load("images/bR.png")
wB: pygame.surface.Surface = pygame.image.load("images/wB.png")
wK: pygame.surface.Surface = pygame.image.load("images/wK.png")
wN: pygame.surface.Surface = pygame.image.load("images/wN.png")
wP: pygame.surface.Surface = pygame.image.load("images/wP.png")
wQ: pygame.surface.Surface = pygame.image.load("images/wQ.png")
wR: pygame.surface.Surface = pygame.image.load("images/wR.png")

pieces_dict: dict[piece, pygame.surface.Surface] = {"bB": bB, "bK": bK, "bN": bN, "bP": bP, "bQ": bQ, "bR": bR,
               "wB": wB, "wK": wK, "wN": wN, "wP": wP, "wQ": wQ, "wR": wR}

screen = pygame.display.set_mode(size)


selected_cell: Optional[tuple[int, int]] = None
possible_destinations: Optional[set[tuple[int, int]]] = None
selected_piece: Optional[tuple[int, int]] = None
whites_turn: bool = True

def switch(x: tuple[int, int]) -> tuple[int, int]:
    return (x[1], x[0])

gs = GameState()
# gs.board = [[None, "bP", None, None, None, None, None, None],
#             ["wP", None, "wP", None, None, None, None, None],
#             ["bP", None, "bP", "bP", "bP", "bP", "bP", "bP"],
#             ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
#             [None, None, None, None, None, None, None, None],
#             [None, None, None, None, None, None, None, None],
#             ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
#             [None, "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if pygame.mouse.get_pressed()[0]:
        cursor_pos: tuple[int, int] = pygame.mouse.get_pos()
        selected_cell = (cursor_pos[0]//60, cursor_pos[1]//60)

        if possible_destinations is None: # 初回選択
            selected_piece = switch(selected_cell)
            possible_destinations = gs.towhere(selected_piece, whites_turn)
        else: # ピース選択中に別のセルをクリック
            if switch(selected_cell) in possible_destinations: # 移動可能
                gs.move(selected_piece, switch(selected_cell))
                selected_piece = None
                possible_destinations = None
                selected_cell = None
                whites_turn = not whites_turn
            # elif gs.coor(switch(selected_cell)) is not None: # 移動不可
            else:
                selected_piece = switch(selected_cell)
                possible_destinations = gs.towhere(selected_piece, whites_turn)

    for i in range(8):
        for j in range(8):
            cell = pygame.Rect(60*j, 60*i, 60, 60)
            if (j, i) == selected_cell:
                colour = red
            elif (i+j) % 2 == 0:
                colour = khaki
            elif (i+j) % 2 == 1:
                colour = golden_rod
            if possible_destinations != None:
                if (j, i) in map(switch, possible_destinations):
                    colour = light_salmon
            pygame.draw.rect(screen, colour, cell)
            if gs.board[i][j] != None:
                screen.blit(pieces_dict[gs.board[i][j]], (60*j, 60*i))

    pygame.display.flip()