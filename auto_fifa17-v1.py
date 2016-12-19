import gtk.gdk
from PIL import Image
import time
from MyTyping import MyTyping
from pymouse import PyMouse
import pandas as pd

## CRIANDO LISTA DE JOGADO, PRECO DE BUSCA, PRECO DE VENDA e PRECO VENDA RAPIDA


m   = PyMouse()
typ = MyTyping()


def is_pixel_white(x,y):
    time.sleep(2)
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

def search_player():
    time.sleep(10)
    m.click(562, 565,1)
    time.sleep(2)
    m.click(506, 737,1)

def buy():
    print "buying"

    if(is_pixel_white(249, 607)):
        time.sleep(1)
        m.click(301, 642,1)## select first player

    time.sleep(2)
    m.click(1026, 461,1) ## buy now
    time.sleep(2)
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
    ##time.sleep(2)
    ##m.click(439, 539, 1)

def marketplace():
    ##click transfer
    time.sleep(3)
    m.click(708, 283, 1)
    time.sleep(1)
    m.click(588, 309,1)


if __name__ == "__main__":

    player_name = 'Bakambu'
    BIN    = 1400
    SellPrice  = 1700

    time.sleep(10)
    contToReList = 0;
    marketplace()
    typ.typing(player_name, BIN)

    while True:

        time.sleep(10)
        search_player()
        if is_pixel_white(690,565):
            buy()
            sell(SellPrice)
            marketplace()
        else:
            m.click(714, 568,1) ## player not found (click OK)


        if (contToReList >= 20):
            relist()
            contToReList = 0
            marketplace()
            typ.typing(player_name, BIN)
        else:
            contToReList=contToReList+1
