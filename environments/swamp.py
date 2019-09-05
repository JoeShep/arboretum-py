from interfaces import IStagnant
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Swamp(IStagnant, IContainsAnimals, IContainsPlants):

    def __init__(self):
        IStagnant.__init__(self)
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)

    def animal_count(self):
        return "This place has a bunch of animals in it"

    def __str__(self):
        return self.id
