import pygame

pygame.init()
selecao = pygame.image.load('imagem\selecao.png')
x = 1
y = 150


janela = pygame.display.set_mode((800, 600))
janela.blit(selecao, (0, 0))
pygame.display.flip()
pygame.display.set_caption('Tri-Quest')

#musica
pygame.mixer.music.load('musica/tema.mp3')
pygame.mixer.music.play(-1)

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if selecao.get_rect().collidepoint(x, y):
                print('apertou')