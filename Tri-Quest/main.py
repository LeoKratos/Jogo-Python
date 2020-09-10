import pygame
pygame.init()
clock = pygame.time.Clock()
menu_inicial = pygame.image.load('imagem\menu.png')
botao = pygame.image.load('imagem\começar.png')
x = 0
y = 150

#imagens
janela = pygame.display.set_mode((800, 600))
janela.blit(menu_inicial, (0,0))
janela.blit(botao, (0,150))
pygame.display.flip()
pygame.display.set_caption('Tri-Quest')

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if botao.get_rect().collidepoint(x, y):
                print('apertou')

    pygame.display.update()

pygame.quit()
