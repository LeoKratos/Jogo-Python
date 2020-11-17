import pygame

pygame.init()

janela = pygame.display.set_mode((800, 600))
jogo = pygame.image.load('imagem/gameplay.png')
janela.blit(jogo, (0, 0))



janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    mouse = pygame.mouse.get_pos()

    if 150 + 500 > mouse[0] > 150 and 390 + 50 > mouse[1] > 390:
        pygame.draw.rect(janela, (255, 0, 0), (150, 390, 500, 50))
    else:
        pygame.draw.rect(janela, (200, 0, 0), (150, 390, 500, 50))

    pygame.display.update()

pygame.quit()
quit()