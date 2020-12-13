#!/usr/bin/env python3
from reptiles import reptilia

class Crocodile(reptilia.Reptilia):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Canivores"
    
    def habitat(self):
        return "Aquatic"

    def movement(self):
        return "Swimming"

    def sound(self):
        return "Gakker" 

