_This project has been created as part of the 42 curriculum by gbitar_

# DataDeck

## Summary

DataDeck is a Python project focused on advanced Object-Oriented Programming, abstraction, and software design patterns. The goal is to build a modular creature card system while applying professional architecture principles such as factories, capabilities, and strategies.

## Concepts Covered

* Abstract Classes (ABC)
* Inheritance & Polymorphism
* Multiple Inheritance
* Abstract Factory Pattern
* Strategy Pattern
* Interface-Based Design
* Package Architecture
* Type Annotations (MyPy)
* Flake8 Compliance
* Exception Handling

## Exercise 0 — Creature Factory

Implementation of the **Abstract Factory Pattern**.

### Features

* Creation of an abstract `Creature` base class.
* Creation of concrete creature families.
* Creation of an abstract `CreatureFactory`.
* Concrete factories responsible for creating base and evolved creatures.
* Encapsulation of object creation behind factory interfaces.
* Package exposure limited to factories only.

### Concepts Practiced

* Abstract classes
* Factory pattern
* Polymorphism
* Package exports

---

## Exercise 1 — Capabilities

Extension of the creature system through independent capabilities.

### Features

* Creation of the `HealCapability` interface.
* Creation of the `TransformCapability` interface.
* Multiple inheritance combining creatures and capabilities.
* Persistent transformation state affecting creature behavior.
* New factory families for healing and transforming creatures.
* Reuse of the architecture from Exercise 0.

### Concepts Practiced

* Multiple inheritance
* Interface-based design
* Separation of concerns
* State-dependent behavior
* Code extensibility

---

## Exercise 2 — Abstract Strategy

Implementation of the **Strategy Pattern** to manage creature actions during battles.

### Features

* Creation of an abstract `BattleStrategy`.
* Implementation of:

  * `NormalStrategy`
  * `AggressiveStrategy`
  * `DefensiveStrategy`
* Capability validation through strategy compatibility checks.
* Tournament system capable of handling multiple creature types.
* Dedicated exception handling for invalid strategy-creature combinations.

### Concepts Practiced

* Strategy pattern
* Runtime behavior selection
* Decoupling behavior from objects
* Validation through interfaces
* Error handling

## Learning Outcomes

* Design flexible object-oriented architectures.
* Apply multiple design patterns together.
* Build reusable and maintainable Python packages.
* Use abstraction to reduce coupling between components.
* Create extensible systems capable of evolving without major redesign.

## AI Usage

AI was used for concept clarification, debugging assistance, architecture discussions, and understanding design patterns. All generated suggestions were reviewed, adapted, tested, and fully understood before integration.
