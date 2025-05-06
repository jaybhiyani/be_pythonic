
# 🧙‍♂️ Python Dunder (Magic) Methods

This document provides a comprehensive reference to all Python **dunder (double underscore)** methods, with explanations and examples.

---

## 📦 Object Creation and Initialization

### `__new__(cls, [...])`
Creates and returns a new instance. Used before `__init__`.

```python
class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### `__init__(self, [...])`
Initializes the object after it’s created.

```python
class Person:
    def __init__(self, name):
        self.name = name
```

### `__del__(self)`
Destructor called when the object is about to be destroyed.

```python
class File:
    def __del__(self):
        print("Object destroyed")
```

---

## 🔤 String Representations

### `__str__(self)`
Returns a readable string (`str(obj)`, `print(obj)`).

```python
def __str__(self):
    return "Human readable"
```

### `__repr__(self)`
Returns official string representation (`repr(obj)`).
__repr__ stands for representation. It’s a special method used to define what string should be shown when you inspect an object or use repr(obj).

Its primary goal is to provide an unambiguous and developer-friendly string representation of an object—ideally, one that could be used to recreate the object.

```python
def __repr__(self):
    return "ClassName(attribute=value)"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

p = Person("Alice", 30)
print(p)         # Person(name='Alice', age=30)
repr(p)          # Person(name='Alice', age=30)

```

---

## ➕ Arithmetic Operators

| Operator | Method         |
|----------|----------------|
| `+`      | `__add__`      |
| `-`      | `__sub__`      |
| `*`      | `__mul__`      |
| `/`      | `__truediv__`  |
| `//`     | `__floordiv__` |
| `%`      | `__mod__`      |
| `**`     | `__pow__`      |
| `+=`     | `__iadd__`     |
| `-=`     | `__isub__`     |

Example:
```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __repr__(self):
        return f"Number({self.value})"
```

---

## 🔁 Comparison Operators

| Operator | Method     |
|----------|------------|
| `==`     | `__eq__`   |
| `!=`     | `__ne__`   |
| `<`      | `__lt__`   |
| `<=`     | `__le__`   |
| `>`      | `__gt__`   |
| `>=`     | `__ge__`   |

Example:
```python
def __eq__(self, other):
    return self.value == other.value
```

---

## 📚 Container/Collection Behavior

| Method            | Description                       |
|-------------------|-----------------------------------|
| `__len__`         | Length via `len(obj)`             |
| `__getitem__`     | Indexing via `obj[key]`           |
| `__setitem__`     | Assignment via `obj[key] = val`   |
| `__delitem__`     | Deletion via `del obj[key]`       |
| `__contains__`    | Membership via `x in obj`         |
| `__iter__`        | Returns iterator                  |
| `__next__`        | Next item in iterator             |
| `__reversed__`    | Called by `reversed(obj)`         |

Example:
```python
def __getitem__(self, index):
    return self.data[index]
```

---

## 📞 Callable Objects

### `__call__(self, [...])`
Makes an instance callable.
intercepts the initialization process of the class
When we write
```
obj = MyClass()
```
python internally does
```
obj = type.__call__(MyClass, *args, **kwargs)
```
which then calls
MyClass.__new__() — allocates memory.

MyClass.__init__() — initializes the instance.

```python
def __call__(self, *args, **kwargs):
    print("Called like a function")
```

---

### Basic example

```python
class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")

greet = Greeter()
greet("Alice")  # Output: Hello, Alice!
```

### Stateful Callable example
```python
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
```

### Real world Logger Decorator example

```python
class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.func.__name__} with {args}, {kwargs}")
        return self.func(*args, **kwargs)

@Logger
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

```
output

Calling say_hello with ('Alice',), {}
Hello, Alice!
```

| Method     | Defined In              | Purpose                                | Can Return Object?  | Level of Control        |
| ---------- | ----------------------- | -------------------------------------- | ------------------- | ----------------------- |
| `__call__` | Metaclass (e.g. `type`) | Controls instantiation logic (`cls()`) | ✅ (indirectly)      | Very High (entry point) |
| `__new__`  | Class                   | Allocates and **returns** new object   | ✅ Yes               | Medium (creation)       |
| `__init__` | Class                   | Initializes existing object            | ❌ No (returns None) | Low (setup)             |



## 🧼 Context Management

### `__enter__()` and `__exit__()`
Used in `with` blocks.

```python
def __enter__(self):
    print("Entering context")
    return self

def __exit__(self, exc_type, exc_val, exc_tb):
    print("Exiting context")
```

### Example 1: Database Connection Manager
Imagine you have a database class that needs to connect, execute queries, and then close the connection—even if something fails.

```python

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        print(f"Connecting to {self.db_name}...")
        self.connection = f"Connection({self.db_name})"  # Simulated DB connection
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        self.connection = None
        if exc_type:
            print(f"Error: {exc_type.__name__} - {exc_val}")
        return False  # Let exceptions propagate

    def execute(self, query):
        if not self.connection:
            raise Exception("No active connection")
        print(f"Executing query: {query}")

try:
    with DatabaseConnection("my_db") as db:
        db.execute("SELECT * FROM users")
        # raise RuntimeError("Simulated error!")  # Uncomment to test error handling
except Exception as e:
    print(f"Caught exception: {e}")
```

Output

```

Connecting to my_db...
Executing query: SELECT * FROM users
Closing connection to my_db

```

If you uncomment the exception line:

```
Connecting to my_db...
Executing query: SELECT * FROM users
Closing connection to my_db
Error: RuntimeError - Simulated error!
Caught exception: Simulated error!

```

### Example 2: Thread Lock Manager
Let’s say you’re dealing with threading and want to ensure that a lock is always released—even if an error occurs.

```python
import threading

class LockedSection:
    def __init__(self, lock):
        self.lock = lock

    def __enter__(self):
        print("Acquiring lock...")
        self.lock.acquire()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Releasing lock...")
        self.lock.release()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False

lock = threading.Lock()

try:
    with LockedSection(lock):
        print("Inside critical section")
        # raise ValueError("Oops!")  # Simulate an error
except Exception as e:
    print(f"Handled: {e}")

```

Output

```

Acquiring lock...
Inside critical section
Releasing lock...

```

---

## 🧠 Attribute Access

| Method             | Description                          |
|--------------------|--------------------------------------|
| `__getattr__`      | Called for missing attributes        |
| `__getattribute__` | Called for all attribute access      |
| `__setattr__`      | Called for attribute assignment      |
| `__delattr__`      | Called for attribute deletion        |

Example:
```python
def __getattr__(self, name):
    return f"{name} not found"
```

---

## 🔍 Introspection and Metadata

| Method         | Description                           |
|----------------|---------------------------------------|
| `__dir__`      | Customizes `dir(obj)`                 |
| `__sizeof__`   | Returns size of object in bytes       |

---

## 🔢 Type Conversion

| Method         | Description                   |
|----------------|-------------------------------|
| `__int__`      | `int(obj)`                    |
| `__float__`    | `float(obj)`                  |
| `__complex__`  | `complex(obj)`                |
| `__bool__`     | `bool(obj)`                   |
| `__index__`    | Integer representation for slicing |

---

## 🔣 Format and Hashing

| Method         | Description                   |
|----------------|-------------------------------|
| `__format__`   | `format(obj, spec)`           |
| `__hash__`     | `hash(obj)`                   |

---

## ⛓️ Bitwise Operators

| Operator | Method         |
|----------|----------------|
| `&`      | `__and__`      |
| `|`      | `__or__`       |
| `^`      | `__xor__`      |
| `~`      | `__invert__`   |
| `<<`     | `__lshift__`   |
| `>>`     | `__rshift__`   |

---

## 📝 Summary

Python's dunder methods allow objects to behave like built-in types. They enable custom classes to be powerful, flexible, and Pythonic.

---

## 📄 License

MIT License
