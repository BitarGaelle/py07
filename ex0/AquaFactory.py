from .CreatureFactory import CreatureFactory
from .creatures import Aquabub, Torragon


class AquaFactory(CreatureFactory):

    def create_base(self) -> Aquabub:
        aquabub = Aquabub()
        return (aquabub)

    def create_evolved(self) -> Torragon:
        torragon = Torragon()
        return (torragon)
