## Factory Method pattern
https://refactoring.guru/design-patterns/factory-method

## 🧩 Elaborated Definition of Factory Design Pattern

Creational Design Pattern that defines an interface or abstract class for creating an object, but lets the subclasses or internal logic decide which class to instantiate. Rather than instantiating objects directly using a constructor (e.g., new in Java, or ClassName() in Python), the creation logic is encapsulated in a separate method, often
called a "factory method".

This decouples the code that uses the object from the code that creates the object, leading to a system that is more modular, extensible, and easier to maintain.

## 🧠 Core Principles Behind the Definition

1. Encapsulation of Object Creation
The object creation logic (which class to instantiate, with what parameters, under what conditions) is moved into a separate component — the factory.

This hides complex instantiation logic from the client code.

2. Abstraction via Interfaces or Base Classes
The client only interacts with interfaces or abstract classes, not concrete implementations.

This promotes programming to an interface, not to an implementation.

3. Flexibility and Extensibility
You can introduce new product types without changing the code that uses the factory.

The factory method can be extended to create new objects without modifying the existing code — respecting the Open/Closed Principle (SOLID).

## 🧪 Technical Reformulation

A factory pattern provides a method (factory method) or a class (factory class) that returns instances of a common superclass or interface, where the exact type of the object is determined at runtime based on input parameters, configuration, or logic.

## 🔄 Comparison With Direct Instantiation

| Aspect          | Without Factory                               | With Factory Pattern                    |
| --------------- | --------------------------------------------- | --------------------------------------- |
| Object Creation | Done directly in client code                  | Done via a separate factory             |
| Coupling        | High (client is tightly bound to classes)     | Low (client depends only on interfaces) |
| Maintainability | Low (must edit client code to change objects) | High (change logic in factory only)     |
| Flexibility     | Low                                           | High (easy to add new types)            |


## 📌 Example in Words

Suppose you’re building a notification system that sends Email, SMS, or Push notifications.

Without a factory:
You must use if/else or switch in the client code to create the right object.

With a factory:
You simply pass "email" or "sms" to a factory, and it gives you the correct Notification object.
The client has no idea which concrete class was created — and it doesn’t need to.