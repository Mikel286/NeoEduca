
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap

import data
import pokemon
from random import randint

class MiVentana(QWidget):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.width = 400
        self.height = 400

        self.backend_information()
        self.init_gui()

    def backend_information(self):
        url = "config/data.txt"
        with open(url, "r", encoding = "utf-8") as file:
            self.pokedex = []
            for _ in range(150):
                name, type, id = data.line_decompress(line = data.data_read(file = file))
                pokemon_objetc = pokemon.Pokemon(id, name, type)
                self.pokedex.append(pokemon_objetc)

    def generate_img(self, pokemon_objetc):

        label = QLabel(self)
        label.setGeometry(200, 200, 100, 100)
        pixeles = QPixmap(pokemon_objetc.img)
        label.setPixmap(pixeles)
        label.setScaledContents(True)
        return label

    def init_gui(self) -> None:

        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowTitle('Pokedex')

        pokemon_objetc = self.pokedex[randint(0,150)]
        self.label = self.generate_img(pokemon_objetc)
        

        self.show()

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec())