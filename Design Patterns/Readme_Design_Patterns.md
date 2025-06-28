## Important website
https://refactoring.guru/design-patterns/

## Definition

Design patterns are solutions to commonly occuring problems in sofware designs. They are like pre-made blueprints that one can modify as per their design problem

Patterns are often confused with algorithms, because both concepts describe typical solutions to some known problems. While an algorithm always defines a clear set of actions that can achieve some goal, a pattern is a more high-level description of a solution. The code of the same pattern applied to two different programs may be different.

## Classification

The most universal and high-level patterns are architectural patterns. Developers can implement these patterns in virtually any language. Unlike other patterns, they can be used to design the architecture of an entire application.

1. Creational patterns provide object creation mechanisms that increase flexibility and reuse of existing code.

```
Focus: How objects are created, instantiated, and abstracted from their concrete implementations.
```
#### 🔧 Technical Aspects:

Encapsulate object creation logic.

Promote loose coupling by decoupling client code from object creation logic.

Often use abstract classes, interfaces, and inheritance.

Useful when instantiating objects is complex, conditional, or resource-intensive.


2. Structural patterns explain how to assemble objects and classes into larger structures, while keeping these structures flexible and efficient.

```
Focus: How classes and objects are composed to form larger structures.
```
#### 🔧 Technical Aspects:

Compose objects to gain new functionality rather than inheriting.

Helps manage interface mismatches or adapt different APIs.

Heavily uses aggregation, composition, interfaces, and decorators.

Promotes code reuse and flexibility.


3. Behavioral patterns take care of effective communication and the assignment of responsibilities between objects.

```
Focus: Object interaction, communication, and responsibility delegation.
```
#### 🔧 Technical Aspects:

Encapsulate algorithms, communication logic, and workflows.

Often use delegation, composition, observer interfaces, and callbacks.

Helps reduce tight coupling between communicating objects.
