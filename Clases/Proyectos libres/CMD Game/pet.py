
class Pet:

    def __init__(self, nombre):
        self.nombre = nombre
        self.__hambre = 0
        self.__felicidad = 100

    def __str__(self):
        texto = f"""
        Nombre: {self.nombre}
        Hambre: {self.hambre}
        Felicidad: {self.felicidad}\n"""
        return texto

    @property
    def hambre(self):
        return self.__hambre

    @property
    def felicidad(self):
        return self.__felicidad

    @hambre.setter
    def hambre(self, hambre):
        if hambre < 0:
            self.__hambre =  0
        elif hambre > 100:
            self.__hambre = 100
        else:
            self.__hambre = hambre

    @felicidad.setter
    def felicidad(self, felicidad):
        if felicidad > 100:
            self.__felicidad = 100
        elif felicidad < 0:
            self.__felicidad = 0
        else:
            self.__felicidad = felicidad