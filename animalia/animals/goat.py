#!/usr/bin/env python3

from mammals import mamalia

class Goat(mamalia.Mamalia):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Hebivores"
    
    def habitat(self):
        return "Terrestial"

    def movement(self):
        return "Walking"
    def sound(self):
        return "Bleat"