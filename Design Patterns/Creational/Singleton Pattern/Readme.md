Singleton pattern ensures a class has only one instance and provides a global point of access to it.
It is used when exactly one object is needed to coordinate actions across the system.
Example: Database connection, Logger, Configuration settings

https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide/
https://refactoring.guru/design-patterns/singleton/python/example

"""
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
"""

Singleton ensures that:
Only one instance of a class is created.
That instance is globally accessible.
It is often used in:
Config managers
Logging
Database connections
Caches

Ways of implementing Singleton in Python:
1. Using a class variable
2. Using a decorator
3. Using a metaclass


Key Concepts of Singleton Pattern
Single Instance: Only one object of the class is created during the lifetime of the application.

Global Access Point: The object is accessible globally (often via a static method).

Controlled Access: The class itself controls the instantiation logic, usually by:

    Making the constructor private or protected (in languages like C++, Java).

    Using a class method or property to return the single instance (in Python).


| Concept    | Role in Singleton via Metaclass                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------ |
| `type`     | Built-in metaclass. All classes are instances of `type`.                                               |
| `__call__` | Controls what happens when you **instantiate a class**. This is where the singleton logic is enforced. |
| Metaclass  | Custom class (subclass of `type`) that overrides `__call__`.                                           |


| Method     | Defined In              | Purpose                                | Can Return Object?  | Level of Control        |
| ---------- | ----------------------- | -------------------------------------- | ------------------- | ----------------------- |
| `__call__` | Metaclass (e.g. `type`) | Controls instantiation logic (`cls()`) | ✅ (indirectly)      | Very High (entry point) |
| `__new__`  | Class                   | Allocates and **returns** new object   | ✅ Yes               | Medium (creation)       |
| `__init__` | Class                   | Initializes existing object            | ❌ No (returns None) | Low (setup)             |
