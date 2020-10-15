import pygame

pygame.init()
seleçao = pygame.image.load('imagem\selecao.png')
x = 1
y = 150

janela = pygame.display.set_mode((800, 600))
janela.blit(seleçao, (0, 0))
pygame.display.flip()
pygame.display.set_caption('Tri-Quest')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if seleçao.get_rect().collidepoint(x, y):
                print('apertou')