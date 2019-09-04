<<<<<<< HEAD
import sys
sys.path.append('../')

from animals.animal import Animal
from interfaces.movements import ISwimming
from interfaces.habitats import IBrackish
from interfaces.habitats import ICoastal
=======
from animals import Animal
from interfaces import ISwimming
from interfaces import IAquatic
>>>>>>> menu

class RiverDolphin(Animal, ISwimming, IBrackish, ICoastal):

    def __init__(self):
        self.active_hours = "morning"
