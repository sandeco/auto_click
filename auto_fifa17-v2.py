import gtk.gdk
from PIL import Image
import time
from MyTyping import MyTyping
from pymouse import PyMouse
import random
import pandas as pd

## CRIANDO LISTA DE JOGADO, PRECO DE BUSCA, PRECO DE VENDA e PRECO VENDA RAPIDA


m   = PyMouse()
typ = MyTyping()

def is_player_found(x,y):
    time.sleep(1)
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])


    if (pb != None):
        pb.save("screenshot.png","png")

        img = Image.open("screenshot.png").convert('L')

        x = img.getpixel((x,y))

        if x <100:
            return False
        else:
            return True
    else:
        return False

def search_player(player):
    marketplace()
    typ.typing(player[1],player[2])
    time.sleep(1)
    m.click(562, 565,1)
    time.sleep(1)
    m.click(506, 737,1)

def buy():
    print "buying"

    if(is_player_found(249, 607)):
        time.sleep(1)
        m.click(301, 642,1)## select first player

    time.sleep(1)
    m.click(1026, 461,1) ## buy now
    time.sleep(1)
    m.click(670, 569,1)  ## buy now (OK)
    time.sleep(1)
    m.click(447, 538,1)  ## back to window to search


def sell(BIN):

    ## click in UNASSIGNED itens
    time.sleep(1)
    m.click(1133, 286, 1)

    ## select firts player
    time.sleep(1)
    m.click(333, 650,1)

    ## click quick list
    time.sleep(1)
    m.click(475, 423,1)

    ## define start price
    time.sleep(1)
    m.click(895, 436,1)
    typ.select()
    typ.write(BIN-100)

    ## define BIN
    time.sleep(1)
    m.click(897, 481,1)
    typ.select()
    typ.write(BIN)

    ## click OK
    m.click(661, 654,1)


def relist():
    print "relisting"
    ##reload
    time.sleep(2)
    m.click(162, 38, 1)
    time.sleep(2)
    m.click(982, 10, 1)

    ##click transfer
    time.sleep(30)
    m.click(708, 283, 1)

    ##click transfer list
    time.sleep(1)
    m.click(837, 313, 1)

    ## relist
    time.sleep(15)
    m.click(1114, 536, 1)

    ## remove sold
    time.sleep(1)
    m.click(439, 539, 1)


def marketplace():
    ##click transfer
    time.sleep(1)
    m.click(708, 283, 1)
    time.sleep(1)
    m.click(588, 309,1)


if __name__ == "__main__":

    time.sleep(10)
    contToReList = 0;


    df = pd.read_csv('players.csv')

    df = df.loc[df['BIN']<=3000]

    marketplace()
    typ.setMaxPrice()

    while True:
        time.sleep(random.randint(15, 16))  ##RETIRAR ISSO AQUI

        for player in df.itertuples():

            onemore = True ## habilita compra para varias cartas do mesmo jogador. Se encontrar.
            while onemore:

                search_player(player)
                if is_player_found(690,565):
                    if player[3]>0:
                        buy()
                        sell(player[2]+200)
                        marketplace()
                else:
                    onemore = False ## proximo jogador do dataset
                    m.click(714, 568,1) ## player not found (click OK)


        if (contToReList >= 10):
            relist()
            contToReList = 0
            marketplace()
            typ.setMaxPrice()
        else:
            contToReList=contToReList+1
