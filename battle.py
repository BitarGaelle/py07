from ex0 import CreatureFactory, AquaFactory, FlameFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    base2 = factory2.create_base()

    print(base1.describe())

    print(" vs.")

    print(base2.describe())

    print(" fight!")

    print(base1.attack())
    print(base2.attack())


if __name__ == "__main__":
    flamefact = FlameFactory()
    aquafact = AquaFactory()

    test_factory(flamefact)
    print()
    test_factory(aquafact)
    print()
    battle(flamefact, aquafact)
