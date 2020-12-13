#!/usr/bin/env python3

from mammals import mamalia

class Dolphin(mamalia.Mamalia):
    def __init__(self):
        super().__init__()

    def feeding(self):
        return "Omnivores"
    
    def habitat(self):
        return "Aquatic"

    def movement(self):
        return "Swimming"
    
    def sound(self):
        return "Squeaks"