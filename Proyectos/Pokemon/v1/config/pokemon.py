
from winsound import PlaySound, SND_FILENAME

class Pokemon: 

    def __init__(self, id, name, type):
        
        self.id = id
        self.name = name
        self.type = type
        self.img = f"assets/png/Generation_1/{id}.png"
        self.mp3 = f"assets/mp3/1st_Generation/{id}.wav"

    def __str__(self):
        return f"{self.name} pokemon {self.id} de la Pokedex de tipo {self.type}"

    def pokemon_shout(self):
        PlaySound(self.mp3, SND_FILENAME)

if __name__ == "__main__":

    Charmander = Pokemon("001", "Charmander","fire")
    print(Charmander)
    Charmander.pokemon_shout()