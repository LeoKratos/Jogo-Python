import pygame


pygame.init()

janela = pygame.display.set_mode((800, 600))
vermelho_claro = (200, 0, 0)

def vetor():
    teste = []
    teste.append(['animal', 'baleia', 'dino', 'onca', 'baleia'])
    teste.append(['comida', 'banana', 'laranja', 'maça', 'banana'])
    teste.append(['doce', 'bala', 'chiclete', 'bolo', 'chiclete'])

    return teste


def text_objects(text, font):
    textsurface = font.render(text, True, (0, 0, 0))
    return textsurface, textsurface.get_rect()


def button(msg, x, y, w, h, ci, ca, acao=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(janela, ci, (x, y, w, h))
        if click[0] == 1 and acao != None:
            if acao == f'{t[1]}':
                if f'{t[1]}' == f'{t[4]}':
                    print('acertou')
                else:
                    print('errou')
            elif acao == f'{t[2]}':
                if f'{t[2]}' == f'{t[4]}':
                    print('acertou')
                else:
                    print('errou')
            elif acao == f'{t[3]}':
                if f'{t[3]}' == f'{t[4]}':
                    print('acertou')
                else:
                    print('errou')


    else:
        pygame.draw.rect(janela, ca, (x, y, w, h))

    texto = pygame.font.Font('freesansbold.ttf', 20)
    textsurf, textrect = text_objects(msg, texto)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    janela.blit(textsurf, textrect)


sub = vetor()

janela_aberta = True
while janela_aberta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False


    for t in sub:
        button(f'{t[1]}', 150, 390, 500, 50, (255, 0, 0), (200, 0, 0), f'{t[1]}')
        button(f'{t[2]}', 150, 460, 500, 50, (0, 255, 0), (0, 200, 0), f'{t[2]}')
        button(f'{t[3]}', 150, 530, 500, 50, (0, 0, 255), (0, 0, 200), f'{t[3]}')

    pygame.display.update()
