import pygame
import random
from PIL import Image
import sys

def start_puzzle():
    pygame.init()

    WIDTH = 300
    HEIGHT = 300
    TILE = 100
    ROWS = 3

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Image Puzzle")

    img = Image.open("images/captured.jpg")
    img = img.resize((WIDTH, HEIGHT))

    tiles = []
    for y in range(0, HEIGHT, TILE):
        for x in range(0, WIDTH, TILE):
            tile = img.crop((x, y, x+TILE, y+TILE))
            tiles.append(tile)

    correct = tiles.copy()
    random.shuffle(tiles)

    def draw():
        for i, tile in enumerate(tiles):
            x = (i % ROWS) * TILE
            y = (i // ROWS) * TILE
            mode = tile.mode
            data = tile.tobytes()
            surface = pygame.image.fromstring(data, tile.size, mode)
            screen.blit(surface, (x, y))
        pygame.display.update()

    selected = None
    running = True

    while running:
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                index = (y // TILE) * ROWS + (x // TILE)

                if selected is None:
                    selected = index
                else:
                    tiles[selected], tiles[index] = tiles[index], tiles[selected]
                    selected = None

                if tiles == correct:
                    print("✅ Puzzle Solved!")
                    pygame.time.delay(1000)
                    running = False

    pygame.quit()