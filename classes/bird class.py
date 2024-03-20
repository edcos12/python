class bird:
    def __init__(self, species, canfly, nocternal, beak):
        self.species = species 
        self.canfly = canfly
        self.nocternal = nocternal 
        self.beak = beak

    def set_species(self):
         self.species = self.species

    def get_species(self):
         return self.species

class owl(bird):
    def __init__(self, lifespan, type, species, canfly, nocternal):
        super().__init__(species, canfly, nocternal)
        self.lifespan = lifespan
        self.type = type
        self.species = "owl"

    def hoo(self):
        return "hoo"
                 
class dodo(bird):
    def __init__(self, gender, species, canfly, nocternal):
        super().__init__(species, canfly, nocternal)
        self.gender = gender
        self.species = "dodo"

    def squark(self):
         return "squark"
    
tuna = dodo
dodo.set_species(tuna)
print(dodo.get_species(tuna))