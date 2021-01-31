import pygame
from random import randrange


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        # images
        self.image = pygame.image.load("data/bomb2.png")
        self.image_boom = pygame.image.load("data/boom.png")
        # transforms
        pygame.transform.scale(self.image, img_size)
        pygame.transform.scale(self.image, img_size)
        # rects
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width - img_size[0] * 2)
        self.rect.y = randrange(height - img_size[-1] * 2)
        print(self.rect)
        # check colliders
        while pygame.sprite.spritecollideany(self, coords):
            self.rect.x = randrange(width - img_size[0] * 2)
            self.rect.y = randrange(height - img_size[-1] * 2)

        coords.add(self)

    def check(self):
        if self.rect.collidepoint(event.pos):
            self.image = self.image_boom


if __name__ == '__main__':
    pygame.init()
    width, height = 500, 500
    img_size = 50, 50
    size = width, height
    screen = pygame.display.set_mode(size)
    # groups
    group_bombs = pygame.sprite.Group()
    coords = pygame.sprite.Group()
    for i in range(10):
        Bomb(group_bombs)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in group_bombs:
                    bomb.check()
        screen.fill(pygame.Color('black'))
        group_bombs.draw(screen)
        pygame.display.flip()
    pygame.quit()
