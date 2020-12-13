#!/usr/bin/env python3

from reptiles import reptilia

class Frog(reptilia.Reptilia):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Canivores"
    
    def habitat(self):
        return "Aqautic and Terrestial"

    def movement(self):
        return "Walking and Swimming"

    def sound(self):
        return "Croak" 

    def skin_covering(self):
        return "Macus"
