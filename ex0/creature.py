from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, creature_name: str, creature_type: str) -> None:
        self.creature_name = creature_name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.creature_name} is a {self.creature_type} Creature"
