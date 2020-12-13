#!/usr/bin/env python3
from reptiles import reptilia

class Cobra(reptilia.Reptilia):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Canivores"
    
    def habitat(self):
        return "Terrestial"

    def movement(self):
        return "Rectilinear Locomotion"

    def sound(self):
        return "Hizz" 
