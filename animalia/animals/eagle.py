#!/usr/bin/env python3

from birds  import  aves

class Eagle(aves.Aves):
    def __init__(self):
        super().__init__()
    
    def feeding(self):
        return "Canivores"
    
    def habitat(self):
        return "Terrestial"

    def movement(self):
        return "Flying"

    def sound(self):
        return "Scream" 