# typing.Callable is used to specify the type of a callable object, such as a function, method, or class instance that has a __call__ method. 
# It takes a list of argument types and a return type as its parameters, using the syntax Callable[[Arg1Type, Arg2Type, ...], ReturnType]. 
# If no arguments are expected, an empty list is used: Callable[[], ReturnType]. To declare a return type without specifying the call signature, 
# an ellipsis can be used: Callable[..., ReturnType]
# The Callable type is useful for type hinting and static type checking, allowing you to specify that a variable or parameter is expected to be a callable object.
# It is part of the typing module, which provides support for type hints in Python 3.5 and later.
# The typing module is used to provide type hints and static type checking in Python.

from typing import Callable, List

fn = Callable[[list[int]], int]

def mergeSort(arr: List[int]):
    # mergeSort logic
    pass

def quickSort(arr: List[int]):
    # quickSort logic
    pass

def sort(arr: List[int], sort_algo: fn) -> int:
    return sort_algo(arr)