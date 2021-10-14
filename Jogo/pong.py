from PPlay.window import *
from PPlay.sprite import *
#INICIALIZACAO
#velocidade bola
velocidade_y_bola = -390
velocidade_x_bola = 390

#velocidade pad
velocidade_pad = 250
velocidade_pad_AI = 200  #dificuldade

janela = Window(1000, 600)
janela.set_title("FIFA 22 Alpha - R$ 349,99 acesso antecipado - Ultimate Edition Mega Plus")
teclado = Window.get_keyboard()

bola = Sprite ("jabulani.png", 1)
bola.x = janela.width/2
bola.y = janela.height/2

pad_esquerda = Sprite ("pad_brasil.png", 1)
pad_esquerda.x = 5
pad_direita = Sprite ("pad_argentina.png", 1)
pad_direita.x = janela.width - pad_direita.width - 5

#placar
placar1, placar2 = 0,0
pontuacao_time1 = "0"
pontuacao_time2 = "0"

while(1):

    if (teclado.key_pressed("UP")):
        if (pad_esquerda.y > 0):
            pad_esquerda.y -= velocidade_pad * janela.delta_time()
    if (teclado.key_pressed("DOWN")):
        if ((pad_esquerda.y + pad_direita.height) < janela.height):
            pad_esquerda.y += velocidade_pad * janela.delta_time()

    #velocidade da bola
    bola.x += velocidade_x_bola * janela.delta_time()
    bola.y += velocidade_y_bola * janela.delta_time()

    #gol
    if (bola.x > janela.width - bola.width):
        bola.x = janela.width/2
        bola.y = janela.height/2

        placar1 += 1
        pontuacao_time1 = str(placar1)

    if(bola.x < 0):
        bola.x = janela.width / 2
        bola.y = janela.height / 2

        placar2 += 1
        pontuacao_time2 = str(placar2)

    #bola bater no chao ou teto
    if (bola.y > janela.height - bola.height) or (bola.y < 0):
        velocidade_y_bola *= -1

    #BOT
    if(bola.x > janela.width/2):
        if (bola.y > pad_direita.y):
            if ((pad_direita.y + pad_direita.height) < janela.height):
                pad_direita.y += velocidade_pad_AI * janela.delta_time()

        if (bola.y < pad_direita.y):
            if (pad_direita.y > 0):
                pad_direita.y -= velocidade_pad_AI * janela.delta_time()

    #colisao com os pads
    if bola.collided(pad_esquerda) or bola.collided(pad_direita):
        velocidade_x_bola *= -1

    #DESENHO
    janela.set_background_color((67, 107, 45))

    janela.draw_text("BRASIL", 220, 5, 20,(255,255,255),"Arial",True,False)
    janela.draw_text(pontuacao_time1, 85 + 220, 5, 20, (255, 255, 255), "Arial", True, False)

    janela.draw_text("ARGENTINA", 2*(janela.width/3), 5, 20, (255, 255, 255), "Arial", True, False)
    janela.draw_text(pontuacao_time2, 130 + 2*(janela.width / 3), 5, 20, (255, 255, 255), "Arial", True, False)

    pad_esquerda.draw()
    pad_direita.draw()
    bola.draw()
    janela.update()

#end