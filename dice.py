# src/dice.py
import random

class Dice:
    def roll(self):
        # Lanza un dado y retorna un número aleatorio entre 1 y 6
        return random.randint(1, 6)
