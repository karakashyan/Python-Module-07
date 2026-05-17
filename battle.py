from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    base1 = factory1.create_base()
    print(base1.describe())
    print("vs.")
    base2 = factory2.create_base()
    print(base2.describe())
    print("fight!")
    print(base1.attack())
    print(base2.attack())


test_factory(FlameFactory())
test_factory(AquaFactory())
battle(FlameFactory(), AquaFactory())
