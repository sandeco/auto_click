import gtk.gdk
from PIL import Image
import time

import pyautogui as pyaut


## CRIANDO LISTA DE JOGADO, PRECO DE BUSCA, PRECO DE VENDA e PRECO VENDA RAPIDA

def is_pixel_white(x,y):
    time.sleep(2)
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
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



if __name__ == "__main__":

    ##print is_pixel_white(690,565)
    img = pyaut.screenshot()


