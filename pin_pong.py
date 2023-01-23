import pygame
from pygame.locals import *
from random import randint

pygame.init()

largura = 1000
altura = 580
x_jogador = (altura - 80) / 2
x_rival = (altura - 80) / 2

#escolher aonde a bola vai começa
escolhar_codernada = randint(0, 1)
lista_y = [400, 700]
lista_x = [54, 54]

# o eixo x e y da bola
x_bola = lista_x[escolhar_codernada]
y_bola = lista_y[escolhar_codernada]

#os pontos que o rival e o jogador fazem
pontos_jogador = 0
pontos_rival = 0

#quando borda for igual a um significa que x_rival deve aumenta e igual a 54
#ser for um e igual a 500 deve diminuir
borda = randint(0, 1)

fonte = pygame.font.SysFont("arial", 30, True, False)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Ping Pong')

#o portado_bola ou portado da bola e um dado que vai ajudar
#a progama a fisica do rival quando ele jogar a bola e ela
#bate na parede já que sera o caminho inverso do jogador
#quando o jogado estive com a bola portado_bola = 0
#quando o rival estive com a bola portado_bola = 1
portado_bola = 0
#ver ser foi o jogador ou o rival que jogou a bola
rival_bola = 0
# zero ser a bola for para baixo e um para cima
baixo = 0
#em qual objeto a bola colidiu
posicao = 0
#script da bola
def bola1():
    global posicao
    global y_bola
    global x_bola
    global largura
    global altura
    global baixo
    global portado_bola

    # velocidade da bola
    velocidade = randint(7, 9)
    velocidade = '0.' + str(velocidade)
    velocidade = float(velocidade)

    #quando a bola e lançada no começo da partida ou após um ponto
    if posicao == 0:
        y_bola -= velocidade
        x_bola += velocidade

    #quando a bola bate na parede1 o numero de posicao vira um
    elif posicao == 1:
        if portado_bola == 0:
            if baixo == 1:
                y_bola += velocidade
                x_bola += velocidade

            elif baixo == 0:
                y_bola += velocidade
                x_bola += velocidade
        
        else:
            if baixo == 1:
                y_bola -= velocidade
                x_bola += velocidade

            elif baixo == 0:
                y_bola -= velocidade
                x_bola -= velocidade

    #quando a bola bate na parede2 o numero de posicao vira dois
    elif posicao == 2:
        if portado_bola == 0:
            if baixo == 1:
                y_bola -= velocidade
                x_bola -= velocidade

            else:
                y_bola += velocidade
                x_bola -= velocidade

        else:
            if baixo == 1:
                y_bola += velocidade
                x_bola += velocidade

            else:
                y_bola -= velocidade
                x_bola -= velocidade
    
    #quando a bola bate no jogador
    elif posicao == 3:
        if baixo == 1:
            y_bola += velocidade
            x_bola -= velocidade
        
        else:
            y_bola -= velocidade
            x_bola += velocidade

    #quando a bola bate no rival
    elif posicao == 4:
        if baixo == 1:
            y_bola -= velocidade
            x_bola += velocidade
        
        else:
            y_bola -= velocidade
            x_bola += velocidade

# uma inpreçisão dos dados do rival ou ana

presicao = 0

while True:

    bola1()

    mensagem_jogador = fonte.render(f'Jogador {pontos_jogador}', True, [255, 255, 255])
    mensagem_rival = fonte.render(f'Ana {pontos_rival}', True, [255, 255, 255])

    pygame.Surface.fill(tela, [0, 0, 0])

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if x_jogador <= altura - 80 and pygame.key.get_pressed()[K_s] or x_jogador <= altura - 80 and pygame.key.get_pressed()[K_DOWN]:
        x_jogador += 0.5

    elif x_jogador >= 54 and pygame.key.get_pressed()[K_w] or x_jogador >= 54 and pygame.key.get_pressed()[K_UP]:
        x_jogador -= 0.5

    # script da movimentação do rival

    if x_rival <= altura - 80 and x_bola - presicao > x_rival:
        presicao = randint(0, 135)
        x_rival += 0.5
    
    elif x_rival >= 54 and x_bola - presicao < x_rival:
        presicao = randint(0, 135)
        x_rival -= 0.5

    # colocando o rival e o player na tela

    jogador = pygame.draw.rect(tela, [255, 255, 255], [0, x_jogador, 20, 80])
    rival = pygame.draw.rect(tela, [255, 255, 255], [largura - 20, x_rival, 20, 80])
    bola = pygame.draw.rect(tela, [255, 255, 255], [y_bola , x_bola , 20, 20])
    parede2 = pygame.draw.rect(tela, [0, 0, 0], [0, altura - 1 , largura, 54])

    if y_bola <= -20:
        pontos_rival += 1
        escolhar_codernada = randint(0, 1)
        x_bola = lista_x[escolhar_codernada]
        y_bola = lista_y[escolhar_codernada]

    elif y_bola >= largura + 20:
        pontos_jogador += 1
        escolhar_codernada = randint(0, 1)
        x_bola = lista_x[escolhar_codernada]
        y_bola = lista_y[escolhar_codernada]

    #verificar ser colidiu com a parede2
    if parede2.colliderect(bola):
        posicao = 2
        if largura - y_bola > y_bola:
            posicao = 2
            baixo = 1
        
        else:
            posicao = 2
            baixo = 0

    #verificar ser colidiu com o jogador
    elif jogador.colliderect(bola):
        portado_bola = 0
        if altura - x_bola > x_bola:
            posicao = 3
            baixo = 0
        
        else:
            posicao = 3
            baixo = 1

    #verificar ser colidiu com o rival

    elif rival.colliderect(bola):
        portado_bola = 1
        if altura - x_bola > x_bola:
            posicao = 4
            baixo = 0
        
        else:
            posicao = 4
            baixo = 1

    parede1 = pygame.draw.rect(tela, [0, 0, 0], [0, 0 , largura, 54])

    #verificar ser colidiu com a parede1
    if parede1.colliderect(bola):
        posicao = 1
        if largura - y_bola > y_bola:
            posicao = 1
            baixo = 1
        
        else:
            posicao = 1
            baixo = 0

    #colocar as mensagens na tela
    tela.blit(mensagem_jogador, [250, 0])
    tela.blit(mensagem_rival, [largura - 250, 0])

    pygame.display.update()