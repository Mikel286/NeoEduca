
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QTimer, Qt, QThread

import data
import pokemon
from random import randint

class MainScreen(QWidget):
    
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.width = 400
        self.height = 400
        self.bkcolor = "#000000"
        self.primary_color = "transparent"
        self.secundary_color = "#ffffff"

        self.init_screen()
    
    def generate_button(self, text, width, height, function):
        boton = QPushButton(text, self)
        boton.setFixedSize(width, height)
        boton.setStyleSheet(f"""background-color: {self.primary_color}; color: {self.secundary_color}; border: 2px solid {self.secundary_color};""")
        boton.clicked.connect(function)
        return boton

    def init_screen(self) -> None:

        self.setGeometry(100, 100, self.width, self.height)
        self.setStyleSheet(f"background-color: {self.bkcolor}")
        self.setWindowTitle('PokeDuca')

        self.explore = self.generate_button("Explore", 100, 50, self.open_explore)
        self.pokedex = self.generate_button("Pokedex", 100, 50, self.open_pokedex)

        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.explore)
        self.buttons.addWidget(self.pokedex)
        self.buttons.setSpacing(10)
        self.buttons.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.main_layout = QVBoxLayout()
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.buttons)
        self.main_layout.addStretch()

        self.setLayout(self.main_layout)      

        self.show()

    def open_explore(self):
        self.expore_screen = ExploreScreen()

    def open_pokedex(self):
        self.pokedex_screen = PokedexScreen() 

class ExploreScreen(QWidget):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.width = 400
        self.height = 400
        self.bkcolor = "#FFFFFF"
        self.primary_color = "transparent"
        self.secundary_color = "#ffffff"

        self.backend_information()
        self.init_screen()

    def backend_information(self):
        url = "config/data.txt"
        with open(url, "r", encoding = "utf-8") as file:
            self.pokedex = []
            for _ in range(150):
                name, type, id = data.line_decompress(line = data.data_read(file = file))
                pokemon_objetc = pokemon.Pokemon(id, name, type)
                self.pokedex.append(pokemon_objetc)
    
    def start_search(self):

        self.points = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.animate_points)
        self.timer.start(400)

        QTimer.singleShot(4000, self.show_pokemon)

    def animate_points(self):
        self.points = (self.points + 1) % 4
        self.loading.setText("Buscando Pokemon" + "." * self.points)
        self.loading.adjustSize()

    def show_pokemon(self):
        self.timer.stop()
        self.loading.hide()
        print("Pokemon Encontrado")

        self.pokemon_img.show()
        self.pokemon_sound.start()

    def generate_img(self, src, width, height, x, y):

        label = QLabel(self)
        label.setGeometry(x, y, width, height)
        pixeles = QPixmap(src)
        label.setPixmap(pixeles)
        label.setScaledContents(True)
        return label
    
    def init_screen(self):

        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowTitle('Explorer')
        self.setStyleSheet(f"background-color: {self.bkcolor}")

        self.loading = QLabel("Buscando Pokemon", self)
        self.loading.move(200, 200)
        
        self.pokemon_objetc = self.pokedex[randint(0,150)]
        self.pokemon_sound = ExploreSound(self.pokemon_objetc)
        self.pokemon_img = self.generate_img(self.pokemon_objetc.img, 200, 200, 100, 100)
        self.pokemon_img.hide()
        
        self.start_search()

        self.show()

class ExploreSound(QThread):

    def __init__(self, object):
        super().__init__()
        self.object = object
    def run(self):
        self.object.pokemon_shout()

class PokedexScreen(QWidget):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.width = 400
        self.height = 400
        self.bkcolor = "#000000"
        self.primary_color = "transparent"
        self.secundary_color = "#ffffff"

        self.backend_information()
        self.init_screen()

    def backend_information(self):
        url = "config/data.txt"
        with open(url, "r", encoding = "utf-8") as file:
            self.pokedex = []
            for _ in range(150):
                name, type, id = data.line_decompress(line = data.data_read(file = file))
                pokemon_objetc = pokemon.Pokemon(id, name, type)
                self.pokedex.append(pokemon_objetc)

    def init_screen(self):

        self.setGeometry(100, 100, self.width, self.height)
        self.setWindowTitle('Pokedex')

        self.show()
    

if __name__ == '__main__':
    def hook(type, value, traceback) -> None:
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    ventana = MainScreen()
    sys.exit(app.exec())