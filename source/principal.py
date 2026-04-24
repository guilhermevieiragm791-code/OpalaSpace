import pygame

try:
    # inicializa o jogo
    pygame.init()
    except:
        #encerra o jogo
        pygame.quit()
#largura e altura da janela
largura = 1280
altura = 720

#configura a janela e o texto do jogo
screen = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Jogo Opala Space')


pygame.display.update()