from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex0.creature import CreatureFactory
from ex1.creature import HealCapability, TransformCapability


def test_healing(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print("base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, HealCapability):
        print(base.heal())
    evolved = factory.create_evolved()
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, HealCapability):
        print(evolved.heal())


def test_transform(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print("base:")
    print(base.describe())
    print(base.attack())
    if isinstance(base, TransformCapability):
        print(base.transform())
        print(base.attack())
        print(base.revert())
    evolved = factory.create_evolved()
    print("evolved:")
    print(evolved.describe())
    print(evolved.attack())
    if isinstance(evolved, TransformCapability):
        print(evolved.transform())
        print(evolved.attack())
        print(evolved.revert())


print("Testing Creature with healing capability")
test_healing(HealingCreatureFactory())
print()
print("Testing Creature with transform capability")
test_transform(TransformCreatureFactory())
