import pygame

pygame.init()
# variaveis
menu_inicial = pygame.image.load('imagem\menu.png')
botao = pygame.image.load('imagem/começar.png')


# imagens
janela = pygame.display.set_mode((800, 600))
janela.blit(menu_inicial, (0, 0))
janela.blit(botao, (0, 150))
pygame.display.flip()
pygame.display.set_caption('Tri-Quest')

# musica
pygame.mixer.music.load('musica/musica_menu.mp3')
pygame.mixer.music.play(-1)

# efeitos sonoros
click = pygame.mixer.Sound('musica/mouse.wav')

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False



    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        if menu_inicial.get_rect().collidepoint(x, y):
            print('apertou')
    mouse = pygame.mouse.get_pos()
    print(mouse)
    pygame.display.update()

pygame.quit()

"""   
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
   emcima do botao             click.play()
"""