import pygame

pygame.init()

def Window(title, width, height):
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    return screen

screen = Window("AMETOSIGMAHUI", 400, 400)

def image(path):
    img = pygame.image.load(path)
    return img

def Paint(screen, img, x, y):
    screen.blit(img, (x, y))

    pass
Texture = image('Grass.jpg')
Paint(screen, Texture, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # render/update here
    pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()