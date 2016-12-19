import pyautogui as pgui
import time

class MyTyping:

    def typing(self, player_name, BIN):
        self.jogador(player_name)
        self.setBIN(BIN)

    def select(self):
        pgui.keyDown('ctrl')
        pgui.keyDown('a')
        pgui.keyUp('a')
        pgui.keyUp('ctrl')

    def write(self, valor):
        pgui.typewrite(str(valor))


    def jogador(self, player_name):
        pgui.click(523, 429) ## limpa o jogados
        time.sleep(1)
        pgui.click(317, 428)  ## seleciona campo de texto
        self.write(player_name)
        time.sleep(2)
        pgui.click(322, 468)

    def setMaxPrice(self):
        pgui.click(492, 564)
        self.select()
        self.write('100000')

    def setBIN(self, valor):
        pgui.click(492, 667)
        self.select()
        self.write(valor)


"""
if __name__ == "__main__":
    typ = Typing()
    time.sleep(5)
    typ.typing('Kevin Kampl', 1100)
"""