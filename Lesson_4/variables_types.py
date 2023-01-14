import sys

# Initialize 3 immutable type variables
var_1 = (1, 2, 3)
var_2 = (1, 2, 3)
var_3 = (1, 2, 3)

# Initialize 2 mutable type variables
var_4 = {1, 2, 3}
var_5 = {1, 2, 3}

# Check variables ID
print(f'ID: {id(var_1)}, {id(var_2)}, {id(var_3)}. Variables have same id: {var_1 is var_2 is var_3}')
print(f'ID: {id(var_4)}, {id(var_5)}. Variables have same id: {var_4 is var_5}')

# Convert variables to a set
var_1 = set(var_1)
var_2 = set(var_2)
var_3 = set(var_3)

# Convert variables to a str
var_4 = sys.intern(str(var_4))
var_5 = sys.intern(str(var_5))

# Check variables ID
print(f'ID: {id(var_1)}, {id(var_2)}, {id(var_3)}. Variables have same id: {var_1 is var_2 is var_3}')
print(f'ID: {id(var_4)}, {id(var_5)}. Variables have same id: {var_4 is var_5}')

# Convert to a tuple without using sys.intern and have same id
# In this code fragment I didn't reuse var_1-var_3 because I didn't see the need for it.
var_4 = {}
var_5 = {}

print(f'ID: {id(var_4)}, {id(var_5)}. Variables have same id: {var_4 is var_5}')

var_4 = tuple(var_4)
var_5 = tuple(var_5)

print(f'ID: {id(var_4)}, {id(var_5)}. Variables have same id: {var_4 is var_5}')

# Convert to a bool without using sys.intern and have same id
var_4 = {1, 2, 3}
var_5 = {1, 2, 3}

print(f'ID: {id(var_4)}, {id(var_5)}. Variables have same id: {var_4 is var_5}')

var_4 = bool(var_4)
var_5 = bool(var_5)

print(f'ID: {id(var_4)}, {id(var_5)}. Variables have same id: {var_4 is var_5}')

# TODO Think about other methods to convert variables types in the same id
