from ex0.CreatureFactory import CreatureFactory
from .creatures import Shiftling, Morphagon


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Shiftling:
        return (Shiftling())

    def create_evolved(self) -> Morphagon:
        return (Morphagon())
