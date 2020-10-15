import pygame

pygame.init()
cinza = (115, 115, 115)

janela = pygame.display.set_mode((800, 600))

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    janela.fill(cinza)
    pygame.display.update()

pygame.quit()
quit()