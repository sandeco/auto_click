from PIL import Image
import pytesseract


class MyOCR():

    def toNumber(image):
        return pytesseract.image_to_string(Image.open('moedas.png'))





