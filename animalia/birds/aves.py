import animalia.animals as animals
class Aves(animals.Animalia):
    """class aves generally describes the characteristics of birds """
    def __init__(self):
        super().__init__()

    def birth_method(self):
        return "Laying of eggs"

    def skin_covering(self):
        return "Feathers"

    def blood_type(self):
        return "Warm blooded"
