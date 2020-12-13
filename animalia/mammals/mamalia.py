import animalia.animals as animals

class Mamalia(animals.Animalia):
    def __init__(self):
        super().__init__()

    def birth_method(self):
        return "Paturition"

    def skin_covering(self):
        return "Fur"

    def blood_type(self):
        return "Warm blooded"
    