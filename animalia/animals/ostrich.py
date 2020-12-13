#!/usr/bin/env python3

from birds  import  aves

class Ostrict(aves.Aves):
    def __init__(self):
        super().__init__()

     
    def feeding(self):
        return "Omnivores"
    
    def habitat(self):
        return "Terrestial"

    def movement(self):
        return "Running"

    def sound(self):
        return "Boom" 
