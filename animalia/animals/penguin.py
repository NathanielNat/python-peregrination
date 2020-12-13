#!/usr/bin/env python3
from birds  import  aves

class Penguin(aves.Aves):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Canivores"
    
    def habitat(self):
        return "Terrestial"

    def movement(self):
        return "Walking and Swimming"

    def sound(self):
        return "Gakker" 