from animales import *
from random import choice
class Tienda:
    def __init__(self):
        self.animales= []

    def agragar_animal(self,animal):
        self.animales.append(animal)

    def entragar_animal(self):
        return choice (self.animales)
