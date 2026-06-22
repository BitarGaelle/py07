#!/usr/bin/env python3
from ex0.CreatureFactory import CreatureFactory
from ex0.creature import Creature
from ex0.AquaFactory import AquaFactory
from ex0.FlameFactory import FlameFactory
from ex1.HealingFactory import HealingCreatureFactory
from ex1.TransformFactory import TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)

flamefact = FlameFactory()
aquafact = AquaFactory()
healfact = HealingCreatureFactory()
transfact = TransformCreatureFactory()

normal = NormalStrategy()
aggressive = AggressiveStrategy()
defensive = DefensiveStrategy()


list_o1 = [(flamefact, normal), (healfact, defensive)]
list_o2 = [(flamefact, aggressive), (healfact, defensive)]
list_o3 = [(aquafact, normal), (healfact, defensive), (transfact, aggressive)]


def battle(list_op: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    if len(list_op) <= 1:
        raise ValueError("Need minimum 2 opponents to fight!")

    fighters: list[tuple[Creature, BattleStrategy]] = []

    for creatfact, strategy in list_op:
        creature = creatfact.create_base()
        fighters.append((creature, strategy))

    for i in range(len(list_op)):
        for j in range(i+1, len(list_op)):
            c1, s1 = fighters[i]
            c2, s2 = fighters[j]
            print("*** Tournament ***")
            print(f"{len(list_op)} opponents involved\n")
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            s1.is_valid(c1)
            s2.is_valid(c2)
            s1.act(c1)
            s2.act(c2)
            print()


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    try:
        battle(list_o1)
    except ValueError as v:
        print(f"Battle error, aborting tournament: {v}\n")

    print("Tournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    try:
        battle(list_o2)
    except ValueError as v:
        print(f"Battle error, aborting tournament: {v}\n")

    print("Tournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    try:
        battle(list_o3)
    except ValueError as v:
        print(f"Battle error, aborting tournament: {v}\n")
