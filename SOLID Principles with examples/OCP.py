# Open/Closed Principle
# Definition: Software entity should be open for extension but closed for modification
# The design and writing of the code should be in a way that implementation of new functionality should be added with minimum changes in the existing code
# The design should be done in a way to allow adding of new functionalities as classes, keeping as much as possible existing code unchanged
# This principle helps to create a code where one need not to worry about the type specifics when it comes to developing something that is generic and reusable
# Whenever something new is added there are no changes to existing code.

# Bad example

class Operation(object):
    def performOperation(num1, num2, operation_type: str):
        if operation_type == 'sum':
            return num1 + num2
        elif operation_type == 'sub':
            return num1 - num2


# Good example
from abc import ABC, abstractmethod
class Operation(ABC):
    @abstractmethod
    # A decorator indicating abstract methods.

    # Requires that the metaclass is ABCMeta or derived from it. A
    # class that has a metaclass derived from ABCMeta cannot be
    # instantiated unless all of its abstract methods are overridden.
    # The abstract methods can be called using any of the normal
    # 'super' call mechanisms. abstractmethod() may be used to declare
    # abstract methods for properties and descriptors.
    def performOperation(num1, num2):
        pass

class Summation(Operation):
    def performOperation(self, num1, num2):
        return num1 + num2

class Subtraction(Operation):
    def performOperation(self, num1, num2):
        return num1 - num2

class Calculator:
    def __init__(self, operation: Operation):
        self.operation = operation

    def performOperation(self, num1, num2):
        return self.operation.performOperation(num1, num2)
    
def main():
    print(Calculator(Subtraction()).performOperation(1,2))
    print(Calculator(Summation()).performOperation(1,2))

main()