#!/usr/bin/env python3

# import animalia.mammals.mamalia
from mammals import mamalia


class Bat(mamalia.Mamalia):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Omnivores"
    
    def habitat(self):
        return "Terrestial"

    def movement(self):
        return "Flying"

    def sound(self):
        return "Clicks"
