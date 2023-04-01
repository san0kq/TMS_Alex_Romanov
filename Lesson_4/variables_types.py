import sys
from typing import Any

# Initialize 3 immutable type variables
var_1: tuple[int, ...] = (1, 2, 3)
var_2: tuple[int, ...] = (1, 2, 3)
var_3: tuple[int, ...] = (1, 2, 3)

# Initialize 2 mutable type variables
var_4: set[int] = {1, 2, 3}
var_5: set[int] = {1, 2, 3}

# Check variables ID
print(f'ID: {id(var_1)}, {id(var_2)}, {id(var_3)}. '
      f'Variables have same id: {var_1 is var_2 is var_3}')
print(f'ID: {id(var_4)}, {id(var_5)}. '
      f'Variables have same id: {var_4 is var_5}')

# Convert variables to a set
var_6: set[int] = set(var_1)
var_7: set[int] = set(var_2)
var_8: set[int] = set(var_3)

# Convert variables to a str
var_9: str = sys.intern(str(var_4))
var_10: str = sys.intern(str(var_5))

# Check variables ID
print(f'ID: {id(var_6)}, {id(var_7)}, {id(var_8)}. '
      f'Variables have same id: {var_6 is var_7 is var_8}')
print(f'ID: {id(var_9)}, {id(var_10)}. '
      f'Variables have same id: {var_9 is var_10}')

# Convert to a tuple without using sys.intern and have same id
# In this code fragment I didn't reuse var_1-var_3
# because I didn't see the need for it.
var_11: dict[Any, Any] = {}
var_12: dict[Any, Any] = {}

print(f'ID: {id(var_11)}, {id(var_12)}. '
      f'Variables have same id: {var_11 is var_12}')

var_13: tuple[int, ...] = tuple(var_4)
var_14: tuple[int, ...] = tuple(var_5)

print(f'ID: {id(var_13)}, {id(var_14)}. '
      f'Variables have same id: {var_13 is var_14}')

# Convert to a bool without using sys.intern and have same id
var_15: set[int] = {1, 2, 3}
var_16: set[int] = {1, 2, 3}

print(f'ID: {id(var_15)}, {id(var_16)}. '
      f'Variables have same id: {var_15 is var_16}')

var_17: bool = bool(var_4)
var_18: bool = bool(var_5)

print(f'ID: {id(var_17)}, {id(var_18)}. '
      f'Variables have same id: {var_17 is var_18}')

# TODO Think about other methods to convert variables types in the same id
