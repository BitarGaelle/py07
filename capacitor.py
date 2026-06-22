from ex1 import HealingCreatureFactory, TransformCreatureFactory


def testing_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal("itself"))

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal("itself and other \
for a large amount"))


def testing_tranform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    healingfac = HealingCreatureFactory()
    tranformfact = TransformCreatureFactory()

    testing_healing(healingfac)
    print()
    testing_tranform(tranformfact)
