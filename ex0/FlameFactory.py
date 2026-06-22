from .CreatureFactory import CreatureFactory
from .creatures import Flameling, Pyrodon


class FlameFactory(CreatureFactory):

    def create_base(self) -> Flameling:
        flameling = Flameling()
        return (flameling)

    def create_evolved(self) -> Pyrodon:
        pyrodon = Pyrodon()
        return (pyrodon)
